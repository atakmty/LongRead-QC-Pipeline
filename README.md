# Long-Read QC Nextflow Pipeline

This repository contains a reproducible, Dockerized Nextflow pipeline for processing and analyzing Long-Read sequencing data (e.g., Oxford Nanopore, PacBio).

## Pipeline Overview

The pipeline consists of three main processes:

1. **LongReadQC**: Uses `NanoPlot` to generate comprehensive quality control reports and plots directly from the FASTQ file.
2. **CalculateReadStats**: Uses a custom Python script (`read_stats.py`) powered by Biopython to calculate the GC content, read length, and mean Phred quality score for every read. The results are saved to a CSV file.
3. **PlotReadStats**: Uses another custom Python script (`plot_stats.py`) utilizing `pandas`, `matplotlib`, and `seaborn` to calculate summary statistics and generate high-quality distribution plots for the calculated metrics.

## Requirements

- **Docker**: The pipeline environment is fully containerized. Docker must be installed and running.
- **Nextflow**: Required to run the pipeline orchestration.

## How to Run

1. **Build the Docker Configuration Image:**
   Before running for the first time, build the pipeline's Docker image:

   ```bash
   docker build -t lr-qc-pipeline:latest .
   ```

2. **Execute the Pipeline:**
   Run the Nextflow pipeline, specifying the input FASTQ file (can be `.fastq` or `.fastq.gz`):

   ```bash
   nextflow run main.nf --input path/to/your/reads.fastq.gz
   ```

3. **Output:**
   The results will be published in the `results/` directory, organized as follows:
   - `results/nanoplot/`: NanoPlot HTML reports and QC plots.
   - `results/stats/`: The `read_stats.csv` containing per-read metrics.
   - `results/plots/`: The generated histograms (GC content, Read Length, Quality Score) and `summary_statistics.txt`.
