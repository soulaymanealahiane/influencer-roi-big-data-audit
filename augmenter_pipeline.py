import pandas as pd
import numpy as np
import logging
from pathlib import Path

# Configure logging for professional tracking during execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def augment_data_with_noise(input_path: str, output_path: str, target_rows: int = 1000000, noise_std: float = 0.01):
    """
    Ingests a tabular dataset, cleans it for regression modeling, and scales 
    it to a specified row count using vectorized Gaussian noise injection.
    """
    
    # 1. Ingest Data
    logging.info(f"Loading original dataset from: {input_path}")
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        logging.error(f"Could not find {input_path}. Please check the file path.")
        return

    logging.info(f"Raw initial shape: {df.shape[0]} rows, {df.shape[1]} columns.")

    # 1.5. Data Cleaning (Pre-Augmentation)
    logging.info("Cleaning data: Dropping non-predictive date columns...")
    columns_to_drop = ['start_date', 'end_date']
    # List comprehension ensures it only drops them if they exist (prevents crash if run twice)
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    logging.info("Cleaning data: Dropping rows with missing values (NaN)...")
    pre_drop_rows = len(df)
    df.dropna(inplace=True)
    dropped_count = pre_drop_rows - len(df)
    
    if dropped_count > 0:
        logging.info(f"Dropped {dropped_count} incomplete rows.")
        
    # Recalculate rows after cleaning
    current_rows = len(df)
    logging.info(f"Cleaned shape ready for augmentation: {current_rows} rows, {df.shape[1]} columns.")

    if current_rows == 0:
        logging.error("Dataset is empty after dropping NaNs. Pipeline halted.")
        return
    elif current_rows >= target_rows:
        logging.warning(f"Dataset already has {current_rows} rows. No augmentation needed.")
        return

    rows_to_generate = target_rows - current_rows
    logging.info(f"Generating {rows_to_generate} synthetic rows...")

    # 2. Separate numerical and categorical columns
    # We only apply mathematical noise to continuous numerical data
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    # 3. Sample from the original distribution (with replacement)
    # This acts as the baseline for our synthetic data
    synthetic_base = df.sample(n=rows_to_generate, replace=True, random_state=42).reset_index(drop=True)

    # 4. Inject Vectorized Gaussian Noise
    if num_cols:
        logging.info(f"Applying Gaussian noise (std_dev={noise_std}) to {len(num_cols)} numerical columns.")
        
        # Calculate the standard deviation for each numerical column to scale the noise proportionately 
        col_stds = df[num_cols].std().values
        
        # Generate a matrix of random noise matching the shape of our synthetic numerical data
        # Formula: Noise = Random_Normal(0, 1) * Column_StdDev * noise_std
        noise_matrix = np.random.normal(loc=0.0, scale=1.0, size=(rows_to_generate, len(num_cols))) * col_stds * noise_std
        
        # Add the noise matrix to the sampled numerical data
        synthetic_base[num_cols] = synthetic_base[num_cols] + noise_matrix

    # 5. Concatenate and Shuffle
    logging.info("Merging original and synthetic datasets...")
    final_df = pd.concat([df, synthetic_base], ignore_index=True)
    
    # Optional: Shuffle the dataset so synthetic rows aren't all at the bottom
    final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # 6. Export to Disk
    logging.info(f"Exporting final dataset ({len(final_df)} rows) to: {output_path}")
    final_df.to_csv(output_path, index=False)
    
    logging.info("Pipeline execution complete.")

if __name__ == "__main__":
    # Find the folder where THIS script is actually saved
    script_dir = Path(__file__).resolve().parent
    
    # Go up one level to 'DATA ENGINEERING', then into 'Data Cleaning'
    # This matches your exact folder names: "Data Cleaning"
    INPUT_FILE = script_dir.parent / "Data Cleaning" / "cleaned_dataset.csv"
    
    # Save the output directly into the "Data Augmentation" folder
    OUTPUT_FILE = script_dir / "augmented_1_million_dataset.csv"
    
    # Log the resolved path so you can see exactly where it's looking
    logging.info(f"Resolved Input Path: {INPUT_FILE}")
    
    augment_data_with_noise(
        input_path=str(INPUT_FILE), 
        output_path=str(OUTPUT_FILE), 
        target_rows=1000000, 
        noise_std=0.01 
    )