#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.input = ""
params.outdir = "results"

process LongReadQC {
    publishDir "${params.outdir}/nanoplot", mode: 'copy'

    input:
    path reads

    output:
    path "*"

    script:
    """
    NanoPlot -t 2 --fastq ${reads} -o .
    """
}

process CalculateReadStats {
    publishDir "${params.outdir}/stats", mode: 'copy'

    input:
    path reads

    output:
    path "read_stats.csv"

    script:
    """
    python3 /workspace/read_stats.py -i ${reads} -o read_stats.csv
    """
}

process PlotReadStats {
    publishDir "${params.outdir}/plots", mode: 'copy'

    input:
    path stats_csv

    output:
    path "*"

    script:
    """
    python3 /workspace/plot_stats.py -i ${stats_csv} -o .
    """
}

workflow {
    if (params.input == "") {
        exit 1, "Please provide an input fastq file using --input"
    }
    
    fastq_file = file(params.input)
    
    LongReadQC(fastq_file)
    stats_csv = CalculateReadStats(fastq_file)
    PlotReadStats(stats_csv)
}
