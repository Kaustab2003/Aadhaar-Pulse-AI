import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_random_dates(start_date, end_date, n=10):
    start_u = start_date.value // 10**9
    end_u = end_date.value // 10**9
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

def get_demo_districts():
    """
    Returns a list of realistic District/State pairs for fully synthetic generation.
    Used when no reference data is available.
    """
    return [
        {'state': 'Bihar', 'district': 'Patna', 'pincode': '800001'},
        {'state': 'Bihar', 'district': 'Gaya', 'pincode': '823001'},
        {'state': 'Uttar Pradesh', 'district': 'Lucknow', 'pincode': '226001'},
        {'state': 'Uttar Pradesh', 'district': 'Kanpur Nagar', 'pincode': '208001'},
        {'state': 'Maharashtra', 'district': 'Mumbai', 'pincode': '400001'},
        {'state': 'Maharashtra', 'district': 'Pune', 'pincode': '411001'},
        {'state': 'Karnataka', 'district': 'Bengaluru Urban', 'pincode': '560001'},
        {'state': 'Delhi', 'district': 'South Delhi', 'pincode': '110001'},
        {'state': 'Tamil Nadu', 'district': 'Chennai', 'pincode': '600001'},
        {'state': 'West Bengal', 'district': 'Kolkata', 'pincode': '700001'}
    ]

def generate_data(force_synthetic=False):
    print("Generating data (Hackathon Mode)...")
    
    # Base paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define start dates
    start_date = pd.to_datetime('2025-01-01')
    end_date = pd.to_datetime('2025-12-31')
    
    # 1. Enrolment Data
    enrol_dir = os.path.join(base_dir, 'api_data_aadhar_enrolment')
    os.makedirs(enrol_dir, exist_ok=True)
    enrol_file = os.path.join(enrol_dir, 'api_data_aadhar_enrolment_synthetic.csv')

    # Try to find reference, else synthetic
    locations = pd.DataFrame(get_demo_districts())
    
    # Check if we have any existing CSVs to learn locations from
    existing_files = [f for f in os.listdir(enrol_dir) if f.endswith('.csv') and 'synthetic' not in f]
    
    if existing_files and not force_synthetic:
        print(f"Found existing data in {enrol_dir}, using locations from there.")
        try:
            df_ref = pd.read_csv(os.path.join(enrol_dir, existing_files[0]))
            locations = df_ref[['state', 'district', 'pincode']].drop_duplicates()
        except Exception as e:
            print(f"Error reading reference: {e}. Using default locations.")

    # Generate Weekly Data
    print(f"Generating synthetic enrolment data for {len(locations)} locations...")
    new_rows = []
    current_date = start_date
    while current_date <= end_date:
        # 80% chance of activity per location per week
        loc_sample = locations.sample(frac=0.8, replace=True) 
        
        for _, row in loc_sample.iterrows():
            new_rows.append({
                'date': current_date.strftime('%d-%m-%Y'),
                'state': row['state'],
                'district': row['district'],
                'pincode': row['pincode'],
                'age_0_5': np.random.randint(5, 50),
                'age_5_17': np.random.randint(10, 100),
                'age_18_greater': np.random.randint(5, 40)
            })
        current_date += timedelta(days=7)
    
    df_new = pd.DataFrame(new_rows)
    df_new.to_csv(enrol_file, index=False)
    print(f"Saved {len(df_new)} rows to {enrol_file}")


    # 2. Biometric Data
    bio_dir = os.path.join(base_dir, 'api_data_aadhar_biometric')
    os.makedirs(bio_dir, exist_ok=True)
    bio_file = os.path.join(bio_dir, 'api_data_aadhar_biometric_synthetic.csv')
    
    print("Generating synthetic biometric data...")
    new_rows = []
    current_date = start_date
    while current_date <= end_date:
        loc_sample = locations.sample(frac=0.8, replace=True)
        for _, row in loc_sample.iterrows():
            new_rows.append({
                'date': current_date.strftime('%d-%m-%Y'),
                'state': row['state'],
                'district': row['district'],
                'pincode': row['pincode'],
                'bio_age_5_17': np.random.randint(50, 300),
                'bio_age_17_': np.random.randint(100, 500)
            })
        current_date += timedelta(days=7)
                
    df_new = pd.DataFrame(new_rows)
    df_new.to_csv(bio_file, index=False)


    # 3. Demographic Data
    demo_dir = os.path.join(base_dir, 'api_data_aadhar_demographic')
    os.makedirs(demo_dir, exist_ok=True)
    demo_file = os.path.join(demo_dir, 'api_data_aadhar_demographic_synthetic.csv')

    print("Generating synthetic demographic data...")
    new_rows = []
    current_date = start_date
    while current_date <= end_date:
        loc_sample = locations.sample(frac=0.8, replace=True)
        for _, row in loc_sample.iterrows():
            new_rows.append({
                'date': current_date.strftime('%d-%m-%Y'),
                'state': row['state'],
                'district': row['district'],
                'pincode': row['pincode'],
                'demo_age_5_17': np.random.randint(20, 150),
                'demo_age_17_': np.random.randint(200, 1000)
            })
        current_date += timedelta(days=7)
        
    df_new = pd.DataFrame(new_rows)
    df_new.to_csv(demo_file, index=False)
    print("Synthetic data generation complete.")

if __name__ == "__main__":
    generate_data()
