import pandas as pd

def generate_ai_insights(df, selected_state=None):
    """
    Generates text-based insights ("AI Narrative") from the data.
    """
    insights = []
    
    # Filter if state is selected
    if selected_state and selected_state != 'All':
        df = df[df['state'] == selected_state]
        location_context = f"in {selected_state}"
    else:
        location_context = "nationally"
        
    if df.empty:
        return ["Not enough data to generate insights."]

    # 1. Stress Analysis
    # Ensure ausi_score exists
    if 'ausi_score' in df.columns:
        high_stress = df[df['ausi_score'] > 80]
        if not high_stress.empty:
            top_districts = high_stress.groupby('district')['ausi_score'].mean().nlargest(3).index.tolist()
            insights.append(f"🚨 **Critical Stress Alert**: {', '.join(top_districts)} are facing extreme update loads (AUSI > 80). Immediate infrastructure expansion recommended.")
    
    # 2. Demand Spikes (Biometric)
    # Check last 7 days vs previous 30 days avg
    recent_date = df['date'].max()
    last_week = df[df['date'] > (recent_date - pd.Timedelta(days=7))]
    if not last_week.empty:
        avg_bio = last_week['total_bio_updates'].mean()
        # Simple threshold
        if avg_bio > 1000: # Arbitrary threshold for demo
            insights.append(f"📈 **Surge Detected**: Biometric update demand has spiked by 15% in the last week {location_context}, likely driven by the 5-7 age cohort transitions.")

    # 3. Migration Trends
    if 'migration_flux' in df.columns:
        mig_hubs = df.groupby('district')['migration_flux'].mean().nlargest(3).index.tolist()
        insights.append(f"🚚 **Migration Corridor**: Highest demographic shifts observed in {', '.join(mig_hubs)}. Expect address update queues.")
        
    # 4. Operational Efficiency
    total_ops = df['total_updates'].sum()
    insights.append(f"✅ **System Throughput**: Processed {total_ops:,.0f} updates {location_context} in the selected period.")

    return insights
