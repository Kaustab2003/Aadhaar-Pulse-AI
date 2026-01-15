import pandas as pd

def get_state_enrolment_stats(df):
    """
    Aggregates enrolment data by State.
    Returns a dataframe with total enrolments per state.
    """
    if df is None or df.empty:
        return pd.DataFrame()
        
    stats = df.groupby('state')[['age_0_5', 'age_5_17', 'age_18_greater', 'total_enrolment']].sum().reset_index()
    stats = stats.sort_values('total_enrolment', ascending=False)
    return stats

def get_age_group_distribution(df):
    """
    Calculates the percentage distribution of enrolments across age groups.
    """
    total = df['total_enrolment'].sum()
    if total == 0:
        return {}
        
    dist = {
        '0-5 Years': (df['age_0_5'].sum() / total) * 100,
        '5-17 Years': (df['age_5_17'].sum() / total) * 100,
        '18+ Years': (df['age_18_greater'].sum() / total) * 100
    }
    return dist
