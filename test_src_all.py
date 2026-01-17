import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.metrics import stress_index
from src.models import anomaly_detection, clustering, forecasting
from src.analytics import migration_analysis

def main():
    print("Running Full Source Test...")
    
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
    
    # 2. Test Stress Index (AUSI)
    print("\n--- Testing Metrics: AUSI ---")
    try:
        df = stress_index.calculate_ausi(df)
        print(f"AUSI Calculated. Head:\n{df[['date', 'district', 'ausi_score']].head()}")
    except Exception as e:
        print(f"FAILED AUSI: {e}")

    # 3. Test Anomaly Detection
    print("\n--- Testing Models: Anomaly Detection ---")
    try:
        df = anomaly_detection.detect_anomalies(df)
        df = anomaly_detection.specific_fraud_rules(df)
        anomalies = df[df['is_anomaly']]
        print(f"Anomalies Detected: {len(anomalies)} / {len(df)}")
        print(f"High Volume Spikes: {df['high_volume_spike'].sum()}")
    except Exception as e:
        print(f"FAILED Anomaly Detection: {e}")

    # 4. Prepare for Clustering (Need Migration Flux)
    print("\n--- Preparing Migration Flux ---")
    try:
        df = migration_analysis.calculate_migration_score(df)
        print("Migration Flux added.")
    except Exception as e:
        print(f"FAILED Migration Flux: {e}")

    # 5. Test Clustering
    print("\n--- Testing Models: Clustering ---")
    try:
        # Clustering aggregates by district, so we get a summary df back
        clusters = clustering.cluster_districts(df)
        print(f"Clustering Complete. Found {clusters['cluster'].nunique()} clusters if applicable.")
        print(clusters[['district', 'recommendation', 'impact_score']].head())
    except Exception as e:
        print(f"FAILED Clustering: {e}")

    # 6. Test Forecasting
    print("\n--- Testing Models: Forecasting ---")
    try:
        district_name = df['district'].iloc[0] # Pick first available district
        print(f"Forecasting for district: {district_name}")
        history, forecast = forecasting.predict_biometric_demand(df, district_name)
        if forecast is not None:
            print(f"Forecast generated for {len(forecast)} days.")
            print(forecast.head())
        else:
            print("Not enough data for forecasting.")
    except Exception as e:
        print(f"FAILED Forecasting: {e}")

    print("\nAll tests completed.")

if __name__ == "__main__":
    main()
