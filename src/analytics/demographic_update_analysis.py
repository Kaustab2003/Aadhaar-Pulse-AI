import pandas as pd

def rank_districts_by_updates(df, top_n=10):
    """
    Ranks districts based on total demographic updates.
    """
    if 'total_demo_updates' not in df.columns:
        return pd.DataFrame()
        
    ranked = df.groupby(['state', 'district'])['total_demo_updates'].sum().reset_index()
    ranked = ranked.sort_values('total_demo_updates', ascending=False).head(top_n)
    return ranked

def analyze_demo_vs_enrolment(df):
    """
    Compares demographic updates against enrolments to find anomalies.
    Returns rows where updates exceed enrolments significantly (indicative of heavy correction/migration load).
    """
    # Group to avoid daily noise
    # Only sum numeric columns relevant to the analysis to avoid datetime errors
    cols_to_sum = ['total_demo_updates', 'total_enrolment']
    grouped = df.groupby(['state', 'district'])[cols_to_sum].sum().reset_index()
    
    # Avoid division by zero
    grouped['update_ratio'] = grouped['total_demo_updates'] / (grouped['total_enrolment'] + 1)
    
    # Filter for high ratio
    high_ratio = grouped[grouped['update_ratio'] > 2.0].sort_values('update_ratio', ascending=False)
    return high_ratio
