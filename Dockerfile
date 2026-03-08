FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    procps \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    biopython \
    nanoplot \
    pandas \
    matplotlib \
    seaborn

WORKDIR /workspace

COPY read_stats.py plot_stats.py /workspace/
