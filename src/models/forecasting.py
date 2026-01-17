from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def predict_biometric_demand(df, district_name, days_ahead=30):
    """
    Simple regression model to forecast biometric updates for a specific district.
    Uses 'age_0_5' enrolments (lagged) if available, otherwise uses trend.
    """
    
    district_data = df[df['district'] == district_name].copy()
    district_data = district_data.sort_values('date')
    
    if len(district_data) < 10:
        return None, None
        
    # Feature: Time ordinal
    district_data['time_idx'] = pd.to_datetime(district_data['date']).apply(lambda x: x.toordinal())
    
    X = district_data[['time_idx']]
    y = district_data['total_bio_updates']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Future dates
    last_date = district_data['date'].max()
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, days_ahead + 1)]
    future_ordinals = [d.toordinal() for d in future_dates]
    
    # Create DataFrame for prediction to match feature names
    X_future = pd.DataFrame({'time_idx': future_ordinals})
    
    predictions = model.predict(X_future)
    
    results = pd.DataFrame({
        'date': future_dates,
        'predicted_demand': predictions
    })
    
    # Ensure no negative predictions
    results['predicted_demand'] = results['predicted_demand'].apply(lambda x: max(0, x))
    
    return district_data, results
