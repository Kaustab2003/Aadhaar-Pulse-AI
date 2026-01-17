import os
import pandas as pd
import sys

# Ensure src is in python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.preprocessing.data_loader import load_all_datasets
from src.preprocessing.feature_engineering import create_master_table

def main():
    print("Starting Aadhaar Pulse AI Pipeline...")
    
    # Define paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_root, 'data', 'raw')
    processed_dir = os.path.join(project_root, 'data', 'processed')
    
    os.makedirs(processed_dir, exist_ok=True)
    
    # 1. Load Data
    print("Loading datasets...")
    datasets = load_all_datasets(data_dir)
    
    # 2. Merge and Create Master Table
    print("Creating master table...")
    try:
        master_df = create_master_table(datasets)
    except Exception as e:
        print(f"Error creating master table: {e}")
        return

    # 3. Save
    output_path = os.path.join(processed_dir, 'merged_master_table.csv')
    print(f"Saving merged data to {output_path}...")
    master_df.to_csv(output_path, index=False)
    
    # Verification
    if not master_df.empty and 'date' in master_df.columns:
        print(f"Data range: {pd.to_datetime(master_df['date']).min()} to {pd.to_datetime(master_df['date']).max()}")
        print(f"Total records: {len(master_df)}")
    
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
