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

## Setup (Anaconda)

```bash
conda env create -f environment.yml
conda activate mutation_rate
```

## Requirements

- Python 3.10+
- pandas
