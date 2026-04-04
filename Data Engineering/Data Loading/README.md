# Data Loading Pipeline

## Overview
This directory serves as the initial ingestion point for the Influencer Marketing ROI project. It houses the raw, untouched 150,000-row dataset and the foundational script required to load and verify the data before it passes downstream into the cleaning and augmentation pipelines.

## Directory Contents
* `original_raw_dataset.csv`: The base 150,000-row dataset sourced for the performance audit.
* `data_downloader.py`: The ingestion and validation script.

## What `data_downloader.py` Does
This script is designed for safe, verifiable data ingestion. Its primary functions are:
1. **Environment Configuration:** Suppresses unnecessary runtime warnings and explicitly sets `matplotlib` to a non-interactive backend (`Agg`) to ensure the script runs smoothly on any server or local environment without hanging on plot renderings.
2. **Data Ingestion:** Loads the raw CSV into a Pandas DataFrame utilizing explicit ASCII encoding and comma delimiters to prevent parsing errors.
3. **Ingestion Validation:** Performs a foundational sanity check by outputting the dataset's dimensional shape, schema information (`df.info()`), and a sample preview (`df.head()`). This guarantees the data was successfully loaded before being handed off to `data_cleaner.py`.
