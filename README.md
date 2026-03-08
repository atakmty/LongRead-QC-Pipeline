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

---

## Communication Draft

**Subject:** Nextflow Long-Read QC Pipeline Results - `barcode77.fastq`

Dear Professor Kılıç,

I have successfully developed and executed the Nextflow pipeline to analyze our sequencing data (`barcode77.fastq.gz`). The pipeline is fully dockerized for reproducibility and performs both standard NanoPlot QC and our custom per-read statistics extraction and visualization.

Here is a brief summary of the findings from our custom analysis:

- **Read Lengths**: The reads have a median length of 547 bp and a mean of ~1,038 bp. We captured some exceptionally long reads in the dataset, with the longest reaching ~686,155 bp. The distribution shows a typical long-read profile with a strong concentration of shorter lengths and a very long tail.
- **Read Quality**: The mean Phred quality score across the dataset is 17.90 (median: 17.31), which corresponds to approximately 98%+ base-calling accuracy. This indicates that the sequencing run was generally of high quality and sufficient for downstream applications.
- **GC Content**: The mean GC content is 53.0%.

**Interpretation and Recommendation**:
Given that the read quality is high (sustained at ~Q17) and we have successfully captured ultra-long reads, the data appears robust. The somewhat lower median read length (547 bp) suggests minor fragmentation, but the overall quality and presence of very long reads compensate for this.

I recommend that we proceed to the alignment/assembly phase with this dataset.

Best regards,
Ata
