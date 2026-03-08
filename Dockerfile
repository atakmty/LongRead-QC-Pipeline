FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
RUN pip install --no-cache-dir \
    biopython \
    nanoplot \
    pandas \
    matplotlib \
    seaborn

# Set working directory
WORKDIR /workspace

# Copy pipeline scripts
COPY read_stats.py plot_stats.py /workspace/
