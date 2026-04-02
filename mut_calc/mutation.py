#!/usr/bin/env python3
"""Functions for computing mutation rates between aligned sequences."""

def compute_mutation_rate(ref: str, query: str) -> float:
    """Return the mutation rate between ref and query sequences."""
    if len(ref) != len(query):
        raise ValueError("Sequences must be the same length for comparison.")
    
    differences = sum(1 for a, b in zip(ref, query) if a != b)
    return differences / len(ref)