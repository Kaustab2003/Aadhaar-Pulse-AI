import nbformat as nbf
import os

def create_notebook(filename, cells):
    nb = nbf.v4.new_notebook()
    nb['cells'] = cells
    with open(filename, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Created {filename}")

def main():
    notebooks_dir = os.path.join(os.getcwd(), 'notebooks')
    os.makedirs(notebooks_dir, exist_ok=True)
    
    # Common imports cell
    imports_cell = nbf.v4.new_code_cell("""import sys
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

print(f"Project Root: {project_root}")
""")

    load_processed_cell = nbf.v4.new_code_cell("""# Load Processed Data
processed_path = os.path.join(project_root, 'data', 'processed', 'merged_master_table.csv')
if os.path.exists(processed_path):
    df = pd.read_csv(processed_path)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    print(f"Data Loaded: {df.shape}")
else:
    print("Error: Processed data not found. Please run run_pipeline.py first.")
""")

    # -------------------------------------------------------------------------
    # 01. Data Understanding
    # -------------------------------------------------------------------------
    nb1_cells = [
        nbf.v4.new_markdown_cell("# 01. Data Understanding & Profiling"),
        imports_cell,
        nbf.v4.new_code_cell("""from src.preprocessing.data_loader import load_all_datasets

data_dir = os.path.join(project_root, 'data', 'raw')
print(f"Loading raw datasets from: {data_dir}")

datasets = load_all_datasets(data_dir)

if datasets['enrolment'] is not None:
    print("Enrolment Data:")
    display(datasets['enrolment'].head())
    display(datasets['enrolment'].info())
"""),
        nbf.v4.new_markdown_cell("## Biometric Data Profiling"),
        nbf.v4.new_code_cell("""if datasets['biometric'] is not None:
    display(datasets['biometric'].head())
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '01_data_understanding.ipynb'), nb1_cells)

    # -------------------------------------------------------------------------
    # 02. Data Cleaning
    # -------------------------------------------------------------------------
    nb2_cells = [
        nbf.v4.new_markdown_cell("# 02. Data Merging & Consolidation"),
        imports_cell,
        nbf.v4.new_markdown_cell("This notebook demonstrates the pipeline logic interactively."),
        nbf.v4.new_code_cell("""from src.preprocessing.data_loader import load_all_datasets
from src.preprocessing.feature_engineering import create_master_table

data_dir = os.path.join(project_root, 'data', 'raw')
datasets = load_all_datasets(data_dir)

# Create Master Table
try:
    master_df = create_master_table(datasets)
    print("Master table created successfully.")
    display(master_df.head())
    
    # Check for missing values
    print("Missing Values Summary:")
    print(master_df.isnull().sum())
except Exception as e:
    print(f"Error: {e}")
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '02_data_cleaning.ipynb'), nb2_cells)

    # -------------------------------------------------------------------------
    # 03. Exploratory Analysis
    # -------------------------------------------------------------------------
    nb3_cells = [
        nbf.v4.new_markdown_cell("# 03. Exploratory Data Analysis (EDA)"),
        imports_cell,
        nbf.v4.new_code_cell("import seaborn as sns\nimport matplotlib.pyplot as plt\nimport plotly.express as px"),
        load_processed_cell,
        nbf.v4.new_markdown_cell("## 3.1 Demographic Analysis using Source Analytics"),
        nbf.v4.new_code_cell("""from src.analytics import enrolment_analysis

# State Statistics
state_stats = enrolment_analysis.get_state_enrolment_stats(df)
display(state_stats.head())

# Plot Top 10 States by Enrolment
plt.figure(figsize=(12, 6))
sns.barplot(data=state_stats.head(10), x='total_enrolment', y='state', palette='viridis')
plt.title('Top 10 States by Total Enrolment')
plt.show()
"""),
        nbf.v4.new_markdown_cell("## 3.2 Age Group Distribution"),
        nbf.v4.new_code_cell("""age_dist = enrolment_analysis.get_age_group_distribution(df)
print(age_dist)

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(age_dist.values(), labels=age_dist.keys(), autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Enrolment Age Distribution')
plt.show()
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '03_exploratory_analysis.ipynb'), nb3_cells)

    # -------------------------------------------------------------------------
    # 04. Trend Analysis
    # -------------------------------------------------------------------------
    nb4_cells = [
        nbf.v4.new_markdown_cell("# 04. Trend Analysis"),
        imports_cell,
        nbf.v4.new_code_cell("import plotly.express as px"),
        load_processed_cell,
        nbf.v4.new_markdown_cell("## 4.1 Daily Trends"),
        nbf.v4.new_code_cell("""# Aggregating daily
daily_trend = df.groupby('date')[['total_enrolment', 'total_bio_updates', 'total_demo_updates']].sum().reset_index()

fig = px.line(daily_trend, x='date', y=['total_enrolment', 'total_bio_updates', 'total_demo_updates'], 
              title="National Daily Updates Trend")
fig.show()
"""),
        nbf.v4.new_markdown_cell("## 4.2 Biometric Update Lag Analysis"),
        nbf.v4.new_code_cell("""from src.analytics import biometric_update_analysis

corr = biometric_update_analysis.analyze_mandatory_update_lag(df)
print(f"Correlation between 0-5 Enrolments and 5-15 Biometric Updates: {corr:.4f}")

forecast_simple = biometric_update_analysis.forecast_bio_demand_simple(df)
display(forecast_simple.tail())
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '04_trend_analysis.ipynb'), nb4_cells)

    # -------------------------------------------------------------------------
    # 05. Anomaly Detection
    # -------------------------------------------------------------------------
    nb5_cells = [
        nbf.v4.new_markdown_cell("# 05. Anomaly Detection"),
        imports_cell,
        load_processed_cell,
        nbf.v4.new_markdown_cell("## 5.1 Running Isolation Forest"),
        nbf.v4.new_code_cell("""from src.models.anomaly_detection import detect_anomalies, specific_fraud_rules

# Detect
df_anom = detect_anomalies(df, contamination=0.01)
df_anom = specific_fraud_rules(df_anom)

anomalies = df_anom[df_anom['is_anomaly'] == True]
print(f"Total Anomalies Detected: {len(anomalies)}")

display(anomalies[['date', 'state', 'district', 'total_updates', 'anomaly_score']].head(10))
"""),
        nbf.v4.new_markdown_cell("## 5.2 Visualizing Anomalies"),
        nbf.v4.new_code_cell("""import plotly.express as px

# Subsample for plotting if too large
plot_data = df_anom.sample(n=min(5000, len(df_anom)), random_state=42)

fig = px.scatter(plot_data, x="total_enrolment", y="total_updates", color="is_anomaly", 
                 title="Anomaly Detection: Enrolment vs Updates",
                 color_discrete_map={True: 'red', False: 'blue'})
fig.show()
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '05_anomaly_detection.ipynb'), nb5_cells)

    # -------------------------------------------------------------------------
    # 06. Prediction Models
    # -------------------------------------------------------------------------
    nb6_cells = [
        nbf.v4.new_markdown_cell("# 06. Prediction Models (Forecasting)"),
        imports_cell,
        nbf.v4.new_code_cell("import matplotlib.pyplot as plt"),
        load_processed_cell,
        nbf.v4.new_markdown_cell("## 6.1 District-level Demand Forecasting"),
        nbf.v4.new_code_cell("""from src.models.forecasting import predict_biometric_demand

# Pick a district with enough data
district_list = df['district'].unique()
sample_district = district_list[0]
print(f"Forecasting for: {sample_district}")

hist_data, forecast = predict_biometric_demand(df, sample_district, days_ahead=60)

if forecast is not None:
    plt.figure(figsize=(12, 6))
    plt.plot(hist_data['date'], hist_data['total_bio_updates'], label='Historical', color='blue')
    plt.plot(forecast['date'], forecast['predicted_demand'], label='Forecast', color='orange', linestyle='--')
    plt.title(f"Biometric Update Demand Forecast: {sample_district}")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    display(forecast.head())
else:
    print("Insufficient data for this district.")
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '06_prediction_models.ipynb'), nb6_cells)

    # -------------------------------------------------------------------------
    # 07. Insights Generation
    # -------------------------------------------------------------------------
    nb7_cells = [
        nbf.v4.new_markdown_cell("# 07. Strategic Insights & Clustering"),
        imports_cell,
        load_processed_cell,
        nbf.v4.new_markdown_cell("## 7.1 Aadhaar Update Stress Index (AUSI)"),
        nbf.v4.new_code_cell("""from src.metrics.stress_index import calculate_ausi

df = calculate_ausi(df)
top_stress = df.sort_values('ausi_score', ascending=False)[['state', 'district', 'date', 'ausi_score']].head(10)
print("Districts with Peak AUSI:")
display(top_stress)
"""),
        nbf.v4.new_markdown_cell("## 7.2 Migration Analysis"),
        nbf.v4.new_code_cell("""from src.analytics.migration_analysis import calculate_migration_score

df = calculate_migration_score(df)
# Top Migration Flux districts
top_mig = df.groupby(['state', 'district'])['migration_flux'].mean().sort_values(ascending=False).head(10)
print("Top Migration Hubs:")
print(top_mig)
"""),
        nbf.v4.new_markdown_cell("## 7.3 Infrastructure Recommendations (Clustering)"),
        nbf.v4.new_code_cell("""from src.models.clustering import cluster_districts

recommendations = cluster_districts(df)

print("Infrastructure Recommendations Count:")
print(recommendations['recommendation'].value_counts())

print("\nTop 10 High Priority New Centers Required:")
new_centers = recommendations[recommendations['recommendation'] == 'New Center Required']
display(new_centers.sort_values('impact_score', ascending=False).head(10))
""")
    ]
    create_notebook(os.path.join(notebooks_dir, '07_insights_generation.ipynb'), nb7_cells)

if __name__ == "__main__":
    main()
