#!/usr/bin/env python3
"""FASTA file parser for the mutation rate calculator."""

class FastaParser:
    """Parses a FASTA file and stores the resulting sequences."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.sequences: dict[str, str] = {}

    def parse(self) -> dict[str, str]:
        """Parse the FASTA file and return a dict of {header: sequence}."""
        self.sequences = {}
        current_header = None
        current_seq: list[str] = []

        with open(self.filepath, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    if current_header:
                        self.sequences[current_header] = "".join(current_seq)
                    current_header = line[1:]  # remove the ">"
                    current_seq = []
                else:
                    current_seq.append(line)
            if current_header:
                self.sequences[current_header] = "".join(current_seq)

        return self.sequences
