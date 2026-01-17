import nbformat as nbf
import os

def create_dashboard_notebook():
    nb = nbf.v4.new_notebook()
    
    # Common imports and setup
    setup_code = """import sys
import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Set Plotly Template
import plotly.io as pio
pio.templates.default = "plotly_white"
"""

    load_data_code = """# Load Processed Data
processed_path = os.path.join(project_root, 'data', 'processed', 'merged_master_table.csv')
if os.path.exists(processed_path):
    df = pd.read_csv(processed_path)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    print(f"Data Loaded: {df.shape}")
else:
    print("Error: Processed data not found.")
"""

    kpi_code = """# 1. Executive KPI Summary
# Aggregate Totals
total_enrolment = df['total_enrolment'].sum()
total_updates = df['total_updates'].sum()
total_bio = df['total_bio_updates'].sum()
total_demo = df['total_demo_updates'].sum()

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = total_enrolment,
    title = {"text": "Total Enrolments"},
    domain = {'row': 0, 'column': 0}
))

fig.add_trace(go.Indicator(
    mode = "number",
    value = total_updates,
    title = {"text": "Total Updates"},
    domain = {'row': 0, 'column': 1}
))

fig.add_trace(go.Indicator(
    mode = "number",
    value = total_bio,
    title = {"text": "Biometric Updates"},
    domain = {'row': 1, 'column': 0}
))

fig.add_trace(go.Indicator(
    mode = "number",
    value = total_demo,
    title = {"text": "Demographic Updates"},
    domain = {'row': 1, 'column': 1}
))

fig.update_layout(
    grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
    title_text="Aadhaar Pulse: Key Performance Indicators",
    height=600
)
fig.show()
"""

    trend_code = """# 2. National Temporal Trends
# Aggregate daily
daily_df = df.groupby('date')[['total_enrolment', 'total_updates']].sum().reset_index()

fig = px.line(daily_df, x='date', y=['total_enrolment', 'total_updates'], 
              title="Daily Enrolment vs Updates Trend",
              labels={'value': 'Volume', 'variable': 'Metric'},
              color_discrete_sequence=['#1f77b4', '#ff7f0e'])

fig.update_layout(hovermode="x unified")
fig.show()
"""

    state_code = """# 3. State-wise Performance
state_df = df.groupby('state')[['total_enrolment', 'total_updates']].sum().reset_index()
state_df = state_df.sort_values('total_enrolment', ascending=False).head(15)

fig = px.bar(state_df, x='state', y=['total_enrolment', 'total_updates'],
             title="Top 15 States by Volume (Enrolment vs Updates)",
             barmode='group',
             labels={'value': 'Count', 'variable': 'Type'})
fig.show()
"""

    demographic_code = """# 4. Age Group Distribution
age_cols = ['age_0_5', 'age_5_17', 'age_18_greater']
age_sums = df[age_cols].sum()
labels = ['0-5 Years', '5-17 Years', '18+ Years']

fig = px.pie(values=age_sums, names=labels, 
             title="Enrolment Distribution by Age Group",
             hole=0.4,
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
"""

    stress_code = """# 5. Aadhaar Update Stress Index (AUSI) Analysis
from src.metrics.stress_index import calculate_ausi

# Calculate AUSI
df_ausi = calculate_ausi(df)

# Top 20 High Stress Districts
top_stress = df_ausi.groupby(['state', 'district'])['ausi_score'].mean().reset_index()
top_stress = top_stress.sort_values('ausi_score', ascending=False).head(20)

fig = px.bar(top_stress, y='district', x='ausi_score', color='ausi_score',
             orientation='h',
             title="Top 20 Districts by Average Stress Index (AUSI)",
             labels={'ausi_score': 'AUSI Score'},
             color_continuous_scale='Reds')
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()
"""

    anomaly_code = """# 6. Anomaly Detection Visualization
from src.models.anomaly_detection import detect_anomalies

# Run Detection on a sample to keep it fast for viz
# Aggregating to District level first to reduce noise
district_daily = df.groupby(['date', 'state', 'district'])[['total_enrolment', 'total_updates', 'total_bio_updates', 'total_demo_updates']].sum().reset_index()

# Detect Anomalies
df_anom = detect_anomalies(district_daily, contamination=0.01)

# Visualize
fig = px.scatter(df_anom, x="total_enrolment", y="total_updates", 
                 color="is_anomaly", 
                 hover_data=['state', 'district', 'date'],
                 title="Anomaly Detection: Total Updates vs Enrolments",
                 color_discrete_map={True: 'red', False: 'blue'},
                 opacity=0.6)
fig.show()
"""

    forecast_code = """# 7. Operational Demand Forecast
from src.models.forecasting import predict_biometric_demand

# Pick top district by volume
top_district = df.groupby('district')['total_bio_updates'].sum().idxmax()
print(f"Forecasting for High Volume District: {top_district}")

hist, forecast = predict_biometric_demand(df, top_district, days_ahead=45)

if forecast is not None:
    fig = go.Figure()
    
    # History
    fig.add_trace(go.Scatter(x=hist['date'], y=hist['total_bio_updates'], 
                             mode='lines', name='Historical Data'))
    
    # Forecast
    fig.add_trace(go.Scatter(x=forecast['date'], y=forecast['predicted_demand'], 
                             mode='lines+markers', name='Forecast',
                             line=dict(dash='dash', color='green')))
    
    fig.update_layout(title=f"45-Day Biometric Demand Forecast: {top_district}",
                      xaxis_title="Date", yaxis_title="Biometric Updates")
    fig.show()
"""

    cells = [
        nbf.v4.new_markdown_cell("# 08. Aadhaar Pulse AI: Professional Dashboard"),
        nbf.v4.new_markdown_cell("This notebook aggregates key insights into professional visualizations for executive reporting."),
        nbf.v4.new_code_cell(setup_code),
        nbf.v4.new_code_cell(load_data_code),
        nbf.v4.new_code_cell(kpi_code),
        nbf.v4.new_code_cell(trend_code),
        nbf.v4.new_code_cell(state_code),
        nbf.v4.new_code_cell(demographic_code),
        nbf.v4.new_code_cell(stress_code),
        nbf.v4.new_code_cell(anomaly_code),
        nbf.v4.new_code_cell(forecast_code)
    ]
    
    nb['cells'] = cells
    
    output_path = os.path.join(os.getcwd(), 'notebooks', '08_dashboard_visualization.ipynb')
    with open(output_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Created {output_path}")

if __name__ == "__main__":
    create_dashboard_notebook()
