from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df, contamination=0.01):
    """
    Detects anomalies in update volumes using Isolation Forest.
    
    Features used:
    - total_enrolment
    - total_bio_updates
    - total_demo_updates
    """
    
    # Features for detection
    features = ['total_enrolment', 'total_bio_updates', 'total_demo_updates']
    
    # Handle NaNs just in case
    data_for_model = df[features].fillna(0)
    
    # Fit model
    iso_forest = IsolationForest(contamination=contamination, random_state=42)
    df['anomaly_score'] = iso_forest.fit_predict(data_for_model)
    
    # Map -1 to "Anomaly" and 1 to "Normal"
    df['is_anomaly'] = df['anomaly_score'].apply(lambda x: True if x == -1 else False)
    
    return df

def specific_fraud_rules(df):
    """
    Rule-based fraud detection on top of ML.
    Example: Biometric updates > 5x Demographic updates (Unusual)
    """
    df['suspicious_bio_ratio'] = df['total_bio_updates'] > (df['total_demo_updates'] * 5)
    
    # High volume single day check
    threshold = df['total_updates'].quantile(0.99)
    df['high_volume_spike'] = df['total_updates'] > threshold
    
    return df
