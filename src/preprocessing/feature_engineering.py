import pandas as pd

def create_master_table(datasets):
    """
    Merges Enrolment, Biometric, and Demographic datasets into a single master table.
    grouped by date and district (or pincode if granular enough).
    """
    # Extract dfs
    enrol = datasets.get('enrolment')
    bio = datasets.get('biometric')
    demo = datasets.get('demographic')

    if enrol is None or bio is None or demo is None:
        raise ValueError("One or more datasets are missing.")

    # Note: We do NOT fillna(0) here to preserve missing data patterns for anomaly detection.
    # enrol = enrol.fillna(0)
    # bio = bio.fillna(0)
    # demo = demo.fillna(0)

    # Merge strategy: Outer join on keys
    keys = ['date', 'state', 'district', 'pincode']
    
    # Merge Enrol + Bio
    merged = pd.merge(enrol, bio, on=keys, how='outer', suffixes=('_enrol', '_bio'))
    
    # Merge + Demo
    merged = pd.merge(merged, demo, on=keys, how='outer')
    
    # Note: We do NOT fillna(0) after merge either.
    # merged = merged.fillna(0)
    
    # Feature Engineering
    # We use sum(axis=1, min_count=0) to treat NaNs as 0 during sum, but the logic 
    # ensures that if all are NaN, it might return 0. 
    # For anomaly detection, input columns remain NaN, but Total columns will be calculated.

    # Total Enrolments
    merged['total_enrolment'] = merged[['age_0_5', 'age_5_17', 'age_18_greater']].sum(axis=1)
    
    # Total Biometric Updates
    merged['total_bio_updates'] = merged[['bio_age_5_17', 'bio_age_17_']].sum(axis=1)
    
    # Total Demographic Updates
    merged['total_demo_updates'] = merged[['demo_age_5_17', 'demo_age_17_']].sum(axis=1)
    
    # Total Updates
    merged['total_updates'] = merged[['total_bio_updates', 'total_demo_updates']].sum(axis=1)
    
    # Lat/Long placeholder (In a real app, join with a Pincode master DB)
    # We will simulate migration signals here if needed
    
    return merged

def aggregate_by_district(df):
    """Aggregates the master dataframe by Date and District."""
    numeric_cols = [c for c in df.columns if c not in ['date', 'state', 'district', 'pincode']]
    
    # Group by Date, State, District
    grouped = df.groupby(['date', 'state', 'district'])[numeric_cols].sum().reset_index()
    
    return grouped
