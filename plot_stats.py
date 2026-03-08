#!/usr/bin/env python3

import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_and_summarize(csv_path, out_dir):
    """
    Reads the stats CSV, calculates summary statistics, and generates plots.
    """
    # Load data
    df = pd.read_csv(csv_path)
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    # 1. Calculate and print summary statistics
    metrics = ['gc_content', 'read_length', 'mean_quality']
    
    summary_file = os.path.join(out_dir, "summary_statistics.txt")
    with open(summary_file, 'w') as f:
        f.write("Summary Statistics\n")
        f.write("==================\n\n")
        
        for metric in metrics:
            mean_val = df[metric].mean()
            median_val = df[metric].median()
            min_val = df[metric].min()
            max_val = df[metric].max()
            
            stats_str = (
                f"{metric.replace('_', ' ').title()}:\n"
                f"  Mean:   {mean_val:.2f}\n"
                f"  Median: {median_val:.2f}\n"
                f"  Min:    {min_val:.2f}\n"
                f"  Max:    {max_val:.2f}\n\n"
            )
            print(stats_str)
            f.write(stats_str)
            
    # 2. Generate plots
    sns.set_theme(style="whitegrid")
    
    # GC Content distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['gc_content'], bins=50, kde=True, color='skyblue')
    plt.title('GC Content Distribution')
    plt.xlabel('GC Content (%)')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(out_dir, 'gc_content_dist.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Read Length distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['read_length'], bins=50, kde=True, color='lightgreen')
    plt.title('Read Length Distribution')
    plt.xlabel('Read Length (bp)')
    plt.ylabel('Frequency')
    plt.yscale('log') # often useful for long reads
    plt.savefig(os.path.join(out_dir, 'read_length_dist.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Mean Quality Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['mean_quality'], bins=50, kde=True, color='salmon')
    plt.title('Mean Quality Score Distribution')
    plt.xlabel('Mean Quality Score (Phred)')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(out_dir, 'mean_quality_dist.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Summary saved to {summary_file}")
    print(f"Plots saved to {out_dir}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot stats and generate summary.")
    parser.add_argument("-i", "--input", required=True, help="Input CSV file from read_stats.py")
    parser.add_argument("-o", "--outdir", required=True, help="Output directory for plots and summary")
    args = parser.parse_args()
    
    plot_and_summarize(args.input, args.outdir)
