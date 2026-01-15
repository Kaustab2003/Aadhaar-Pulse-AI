import pandas as pd
import numpy as np

def analyze_mandatory_update_lag(df):
    """
    Analyzes the relationship between past child enrolments (0-5) 
    and current mandatory biometric updates (5-15).
    
    Note: In a real temporal dataset, we would shift the enrolment column by ~5 years.
    Here we look for direct correlation in valid date ranges.
    """
    # Simple correlation matrix
    cols = ['age_0_5', 'bio_age_5_17']
    correlation = df[cols].corr().iloc[0, 1]
    return correlation

def forecast_bio_demand_simple(df, growth_rate=0.05):
    """
    Simple projection of biometric demand based on current volumes.
    """
    df_ts = df.groupby('date')['total_bio_updates'].sum().reset_index()
    df_ts['projected'] = df_ts['total_bio_updates'] * (1 + growth_rate)
    return df_ts
