import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.analytics import enrolment_analysis
from src.analytics import biometric_update_analysis
from src.analytics import demographic_update_analysis
from src.analytics import migration_analysis

def main():
    print("Running Analytics Tests...")
    
    # 1. Load Data
    data_path = os.path.join('data', 'processed', 'merged_master_table.csv')
    if not os.path.exists(data_path):
        print(f"Error: Processed data not found at {data_path}. Please run run_pipeline.py first.")
        return

    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # Ensure date is datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    print(f"Data Loaded. Shape: {df.shape}")
    print("-" * 30)

    # 2. Test Enrolment Analysis
    print("Testing Enrolment Analysis...")
    state_stats = enrolment_analysis.get_state_enrolment_stats(df)
    print(f"State Enrolment Stats (Top 5):\n{state_stats.head()}")
    
    age_dist = enrolment_analysis.get_age_group_distribution(df)
    print(f"Age Group Distribution: {age_dist}")
    print("-" * 30)

    # 3. Test Biometric Update Analysis
    print("Testing Biometric Update Analysis...")
    correlation = biometric_update_analysis.analyze_mandatory_update_lag(df)
    print(f"Enrolment-Update Correlation: {correlation}")
    
    forecast = biometric_update_analysis.forecast_bio_demand_simple(df)
    print(f"Biometric Demand Forecast (Top 5):\n{forecast.head()}")
    print("-" * 30)

    # 4. Test Demographic Update Analysis
    print("Testing Demographic Update Analysis...")
    ranked_districts = demographic_update_analysis.rank_districts_by_updates(df)
    print(f"Top 5 Districts by Updates:\n{ranked_districts.head()}")
    
    high_ratio = demographic_update_analysis.analyze_demo_vs_enrolment(df)
    print(f"Districts with High Update Ratio (Top 5):\n{high_ratio.head()}")
    print("-" * 30)

    # 5. Test Migration Analysis
    print("Testing Migration Analysis...")
    hubs = migration_analysis.identify_migration_corridors(df)
    print(f"Potential Migration Hubs (Top 5):\n{hubs.head()}")
    
    growth_patterns = migration_analysis.classify_growth_patterns(df)
    print(f"Growth Pattern Classification (Top 5):\n{growth_patterns.head()}")
    print("-" * 30)

    print("All tests completed successfully.")

if __name__ == "__main__":
    main()
