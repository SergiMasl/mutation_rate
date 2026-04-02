#!/usr/bin/env python3

import argparse
import sys
import pandas as pd
from mut_calc.fasta_parser import FastaParser
from mut_calc.mutation import compute_mutation_rate


class MutationRateCalculator:
    """Calculates mutation rates of sequences relative to a reference."""

    def __init__(self, fasta_path: str, reference_name: str):
        self.fasta_path = fasta_path
        self.reference_name = reference_name
        self.sequences: dict[str, str] = {}

    def load(self) -> None:
        """Load sequences from the FASTA file."""
        try:
            self.sequences = FastaParser(self.fasta_path).parse()
        except FileNotFoundError:
            sys.stderr.write(f"Error: file '{self.fasta_path}' not found.\n")
            sys.exit(1)
        if self.reference_name not in self.sequences:
            sys.stderr.write(f"Error: reference '{self.reference_name}' not found in FASTA.\n")
            sys.exit(1)

    def calculate(self) -> pd.DataFrame:
        """Calculate mutation rates and return a DataFrame."""
        ref_seq = self.sequences[self.reference_name]
        results = []

        for name, seq in self.sequences.items():
            if name == self.reference_name:
                continue
            try:
                rate = compute_mutation_rate(ref_seq, seq)
                results.append({"sequence": name, "mutation_rate": rate})
            except ValueError as e:
                sys.stderr.write(f"Warning: skipping '{name}' — {e}\n")

        return pd.DataFrame(results)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate mutation rates of sequences relative to a reference from a FASTA file.",
        epilog="Example: python main.py example.fasta reference --output results.csv",
    )
    parser.add_argument("fasta", metavar="FASTA_FILE", help="Path to the input FASTA file")
    parser.add_argument("reference", metavar="REFERENCE_NAME", help="Header name of the reference sequence")
    parser.add_argument("--output", metavar="CSV_FILE", help="Save results to a CSV file")
    args = parser.parse_args()

    calculator = MutationRateCalculator(args.fasta, args.reference)
    calculator.load()
    df = calculator.calculate()

    sys.stdout.write(df.to_string(index=False) + "\n")

    if args.output:
        df.to_csv(args.output, index=False)
        sys.stdout.write(f"\nResults saved to {args.output}\n")


if __name__ == "__main__":
    main()
