import pandas as pd
import os

import glob

def load_dataset(filepath):
    """
    Load a dataset and parse the 'date' column.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_csv(filepath)
    # Standardize column names if necessary (strip spaces)
    df.columns = [c.strip() for c in df.columns]
    
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
    
    return df

def load_from_folder(folder_path):
    """
    Loads and concatenates all CSV files from a directory.
    """
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))
    if not all_files:
        return None
        
    print(f"Found {len(all_files)} files in {folder_path}. Merging...")
    dfs = []
    for f in all_files:
        try:
            dfs.append(load_dataset(f))
        except Exception as e:
            print(f"Warning: Failed to load {f}: {e}")
            
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return None

def load_all_datasets(data_dir):
    """
    Loads all three primary datasets.
    Prioritizes split folders (api_data_*) in the project root.
    Falls back to single files in data_dir.
    """
    # Map key -> (single_filename_in_data_dir, folder_name_in_root)
    sources = {
        'enrolment': ('aadhaar_enrolment.csv', 'api_data_aadhar_enrolment'),
        'biometric': ('aadhaar_biometric_update.csv', 'api_data_aadhar_biometric'),
        'demographic': ('aadhaar_demographic_update.csv', 'api_data_aadhar_demographic')
    }
    
    datasets = {}
    
    # Robustly find project root relative to this script file
    # file matches: src/preprocessing/data_loader.py
    # dirname -> src/preprocessing
    # dirname -> src
    # dirname -> project_root
    try:
        current_script_path = os.path.abspath(__file__)
        src_dir = os.path.dirname(os.path.dirname(current_script_path))
        project_root = os.path.dirname(src_dir)
    except NameError:
        # Fallback if __file__ is not defined (e.g. interactive mode)
        project_root = os.getcwd()

    for key, (filename, foldername) in sources.items():
        parts = []
        
        # 1. Try loading from split folder in project root (Pure Merge, No Cleaning)
        folder_path = os.path.join(project_root, foldername)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            print(f"Loading {key} from split folder: {foldername}")
            ds_folder = load_from_folder(folder_path)
            if ds_folder is not None:
                parts.append(ds_folder)

        # 2. ALSO Load from single file in data_dir
        path = os.path.join(data_dir, filename)
        if os.path.exists(path):
            print(f"Loading {key} from file: {path}")
            ds_file = load_dataset(path)
            if ds_file is not None:
                parts.append(ds_file)
        
        if parts:
            print(f"Combining {len(parts)} sources for {key}")
            # Concatenate all found pieces (Folder parts + Single file)
            datasets[key] = pd.concat(parts, ignore_index=True)
        else:
            print(f"Warning: {key} data not found (checked {foldername} and {path})")
            datasets[key] = None
            
    return datasets
