#!/usr/bin/env python3

import os
import sys
import argparse
import gzip
from Bio import SeqIO
import csv

def calculate_stats(fastq_path, output_csv):
    """
    Reads a FASTQ file and calculates GC content, read length, and mean quality score
    for each read. Saves the results to a CSV file.
    """
    results = []
    
    # Handle gzip compressed fastq
    if fastq_path.endswith('.gz'):
        handle = gzip.open(fastq_path, "rt")
    else:
        handle = open(fastq_path, "r")
        
    try:
        for record in SeqIO.parse(handle, "fastq"):
            # length
            length = len(record.seq)
            
            # GC content
            gc = sum(1 for x in record.seq if x in 'GCgc')
            gc_content = (gc / length) * 100 if length > 0 else 0
            
            # Mean quality score
            # Phred quality scores are in record.letter_annotations["phred_quality"]
            qualities = record.letter_annotations["phred_quality"]
            mean_quality = sum(qualities) / len(qualities) if len(qualities) > 0 else 0
            
            results.append({
                'read_id': record.id,
                'gc_content': round(gc_content, 2),
                'read_length': length,
                'mean_quality': round(mean_quality, 2)
            })
    finally:
        handle.close()
        
    print(f"Processed {len(results)} reads.")
    
    # Write to CSV
    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['read_id', 'gc_content', 'read_length', 'mean_quality'])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate stats from a FASTQ file.")
    parser.add_argument("-i", "--input", required=True, help="Input FASTQ file (can be .gz)")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file")
    args = parser.parse_args()
    
    calculate_stats(args.input, args.output)
