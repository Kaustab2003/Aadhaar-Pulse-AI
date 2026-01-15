import pandas as pd

def calculate_migration_score(df):
    """
    Calculates a 'Migration Score' acting as a proxy for movement.
    Logic: High Volume of Demographic Updates (Address Changes) relative to New Enrolments.
    """
    df = df.copy()
    # Adding 1 to denominator to handle zero division
    df['migration_flux'] = df['total_demo_updates'] / (df['total_enrolment'] + 1)
    return df

def identify_migration_corridors(df, threshold_percentile=0.90):
    """
    Identifies districts that are potential migration hubs based on the Migration Score.
    """
    df_scored = calculate_migration_score(df)
    
    # Aggregate by district
    dist_scores = df_scored.groupby(['state', 'district'])['migration_flux'].mean().reset_index()
    
    threshold = dist_scores['migration_flux'].quantile(threshold_percentile)
    hubs = dist_scores[dist_scores['migration_flux'] > threshold].sort_values('migration_flux', ascending=False)
    
    return hubs

def classify_growth_patterns(df):
    """
    Classifies districts into growth quadrants based on Migration Flux vs Organic Growth.
    Returns the dataframe with a 'growth_category' column.
    """
    df = calculate_migration_score(df)
    
    # Organic Growth Rate: Proportion of new child enrolments (0-5)
    # Using a small epsilon to avoid division by zero
    df['organic_growth_rate'] = df['age_0_5'] / (df['total_enrolment'] + 1)
    
    # Calculate thresholds (Median) to classify
    # We aggregate by district first to get the classification per district
    dist_summary = df.groupby(['state', 'district']).agg({
        'migration_flux': 'mean',
        'organic_growth_rate': 'mean',
        'total_enrolment': 'sum',
        'total_updates': 'sum'
    }).reset_index()
    
    flux_median = dist_summary['migration_flux'].median()
    growth_median = dist_summary['organic_growth_rate'].median()
    
    def get_category(row):
        high_flux = row['migration_flux'] > flux_median
        high_growth = row['organic_growth_rate'] > growth_median
        
        if high_flux and high_growth:
            return "Urban Boom (High Flow + High Births)"
        elif high_flux and not high_growth:
            return "Migration Hub (Inflow Dominant)"
        elif not high_flux and high_growth:
            return "Organic Growth (Birth Dominant)"
        else:
            return "Stable / Stagnant"
            
    dist_summary['growth_category'] = dist_summary.apply(get_category, axis=1)
    
    return dist_summary
