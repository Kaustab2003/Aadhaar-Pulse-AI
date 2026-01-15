import pandas as pd
import numpy as np

def calculate_ausi(df, window=7):
    """
    Calculates Aadhaar Update Stress Index (AUSI).
    
    Formula:
    AUSI = (Biometric Updates + Demographic Updates) / (Cumulative Enrolment Base)
    
    Note: Since we don't have total historical base, we use a running cumulative sum of enrolments 
    plus a base smooth factor to avoid division by zero.
    """
    
    # Ensure data is sorted
    df = df.sort_values('date')
    
    # Calculate Cumulative Enrolment (Proxy for Aadhaar Base in that region)
    # Adding a small constant to simulate existing base if data starts from 0
    df['cumulative_base'] = df.groupby(['state', 'district'])['total_enrolment'].cumsum() + 1000 
    
    # Calculate Daily Stress
    df['ausi_daily'] = df['total_updates'] / df['cumulative_base']
    
    # Apply Rolling Average for smoothness (7-day window)
    df['ausi_smooth'] = df.groupby(['state', 'district'])['ausi_daily'].transform(
        lambda x: x.rolling(window, min_periods=1).mean()
    )
    
    # Normalize AUSI to 0-100 scale for easier interpretation
    # Using 95th percentile as max reference to avoid outliers skewing the graph
    max_ref = df['ausi_smooth'].quantile(0.95)
    df['ausi_score'] = (df['ausi_smooth'] / max_ref) * 100
    df['ausi_score'] = df['ausi_score'].clip(0, 100) # Cap at 100
    
    return df
