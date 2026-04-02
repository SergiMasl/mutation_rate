# Mutation Rate Calculator

Calculates the mutation rate of each sequence in a FASTA file relative to a user-selected reference sequence.

## Usage

```bash
python main.py <fasta_file> <reference_name> [--output results.csv]
```

## Example

```bash
python main.py example.fasta reference --output results.csv
```

Expected output:

```
sequence  mutation_rate
    seq1       0.000000
    seq2       0.012821
    seq3       0.012821
    seq4       0.025641

Results saved to results.csv
```

To run all tests:

```bash
bash run_tests.sh
```

## Setup (Anaconda)

```bash
conda env create -f environment.yml
conda activate mutation_rate
```

## Project Structure

```
mutation_rate/
├── main.py              # Main script: argument parsing, MutationRateCalculator class
├── mut_calc/
│   ├── __init__.py      # Package init
│   ├── fasta_parser.py  # FastaParser class: reads and parses FASTA files
│   └── mutation.py      # compute_mutation_rate(): compares sequences to reference
├── example.fasta        # Example input file with 4 sequences
├── run_tests.sh         # Bash script that runs all test cases
├── environment.yml      # Conda environment definition
└── LICENSE
```

## Algorithm

The mutation rate is calculated by direct pairwise comparison of aligned sequences:

1. Parse the FASTA file and load all sequences.
2. Identify the reference sequence by name.
3. For each non-reference sequence:
   - Compare it position-by-position to the reference.
   - Count the number of positions where the nucleotides differ.
   - Divide by the total sequence length:

```
mutation_rate = number_of_differences / sequence_length
```

4. Return results as a Pandas DataFrame (sequence name + mutation rate).

> Sequences must be pre-aligned and of equal length for comparison.

## References

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [argparse — Python Standard Library](https://docs.python.org/3/library/argparse.html)
- [FASTA Format — NCBI](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/)
- [Needleman–Wunsch Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)

## Requirements

- Python 3.10+
- pandas

## License

MIT License

## Author

Sergey Maslinikov — smaslini@charlotte.edu
