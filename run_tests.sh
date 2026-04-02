#!/bin/bash
# run_tests.sh — runs the mutation rate calculator on the example FASTA file

set -e

echo "=== Test 1: Basic output to stdout ==="
python main.py example.fasta reference

echo ""
echo "=== Test 2: Save results to CSV ==="
python main.py example.fasta reference --output results.csv
cat results.csv

echo ""
echo "=== Test 3: Missing FASTA file (should error gracefully) ==="
python main.py nonexistent.fasta reference || echo "Exit code: $?"

echo ""
echo "=== Test 4: Reference not in file (should error gracefully) ==="
python main.py example.fasta bad_reference || echo "Exit code: $?"

echo ""
echo "All tests done."

# Clean up Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
echo "Cleaned __pycache__."
