#!/usr/bin/env python3

import os
import sys
import argparse
import gzip
from Bio import SeqIO
import csv

def calculate_stats(fastq_path, output_csv):

    results = []
    
    if fastq_path.endswith('.gz'):
        handle = gzip.open(fastq_path, "rt")
    else:
        handle = open(fastq_path, "r")
        
    try:
        for record in SeqIO.parse(handle, "fastq"):

            length = len(record.seq)
            
            gc = sum(1 for x in record.seq.upper() if x in 'GC')
            gc_content = (gc / length) * 100 if length > 0 else 0
            
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
