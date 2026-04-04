# Import necessary libraries and suppress warnings
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')  # Ensuring non-interactive plotting backend
import matplotlib.pyplot as plt

import seaborn as sns


# Set plot style
sns.set_theme(style='whitegrid')

# Load dataset
data_path = r"C:\Users\pc\OneDrive - Al Akhawayn University in Ifrane\Desktop\BAI Final Project\original_dataset.csv"
df = pd.read_csv(data_path, encoding='ascii', delimiter=',')

# Quick look at the dataset
print('Dataset dimensions:', df.shape)
df.head()

# Print info and first few rows to understand the structure
print("--- Data Info ---")
print(df.info())
print("\n--- First 5 Rows ---")
print(df.head())


