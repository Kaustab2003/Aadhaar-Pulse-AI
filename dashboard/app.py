import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
import numpy as np

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing.data_loader import load_all_datasets
from src.preprocessing.feature_engineering import create_master_table, aggregate_by_district
from src.metrics.stress_index import calculate_ausi
from src.models.anomaly_detection import detect_anomalies, specific_fraud_rules
from src.models.forecasting import predict_biometric_demand
from src.models.clustering import cluster_districts
from src.analytics.migration_analysis import classify_growth_patterns, calculate_migration_score

# --- Configuration & Styling ---
st.set_page_config(
    page_title="Aadhaar Pulse AI | Executive Dashboard", 
    page_icon="🇮🇳", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Tableau-like feel
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Metrics Cards */
    .metric-card {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: left;
        border-left: 6px solid #4e73df;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .metric-value {
        font-size: 32px;
        font-weight: 700;
        color: #2c3e50;
        margin-top: 8px;
    }
    .metric-label {
        font-size: 14px;
        color: #858796;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    /* Headers */
    h1 { color: #2c3e50; font-weight: 800; font-size: 2.2rem; }
    h2 { color: #4e73df; font-weight: 700; font-size: 1.8rem; }
    h3 { color: #5a5c69; font-weight: 600; font-size: 1.4rem; }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        padding-bottom: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 8px 8px 0px 0px;
        gap: 1px;
        padding: 10px 24px;
        border: 1px solid #e3e6f0;
        border-bottom: none;
        color: #858796;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4e73df !important;
        color: white !important;
        border: 1px solid #4e73df;
    }

    /* Chart Containers */
    .chart-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- Data Loading ---
@st.cache_data
def get_dashboard_data():
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    datasets = load_all_datasets(data_dir)
    # Master DF (no aggregation yet, raw merges)
    raw_master = create_master_table(datasets)
    # Aggregated for general charts (Summations treat NaNs as 0)
    dist_df = aggregate_by_district(raw_master)
    
    # Calculate global metrics once
    dist_df = calculate_ausi(dist_df)
    dist_df = detect_anomalies(dist_df)
    
    return raw_master, dist_df

try:
    with st.spinner("Connecting to Aadhaar Data Lake..."):
        raw_df, df = get_dashboard_data()
except Exception as e:
    st.error(f"Critical Data Error: {e}")
    st.stop()

# --- Sidebar Controls ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Aadhaar_Logo.svg/1200px-Aadhaar_Logo.svg.png", width=120)
    st.markdown("### Executive Controls", unsafe_allow_html=True)
    st.markdown("---")
    
    # Date Filter
    # Ensure pandas datetime conversion
    df['date'] = pd.to_datetime(df['date'])
    raw_df['date'] = pd.to_datetime(raw_df['date'])
    
    min_date = df['date'].min()
    max_date = df['date'].max()
    
    date_range = st.date_input(
        "Period Selection",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    st.markdown("---")
    
    # State Filter
    all_states = ['All Regions'] + sorted(df['state'].unique().astype(str).tolist())
    selected_state = st.selectbox("Geo-Filter: State", all_states)
    
    selected_district = "All Districts"
    if selected_state != "All Regions":
        districts = ['All Districts'] + sorted(df[df['state'] == selected_state]['district'].unique().astype(str).tolist())
        selected_district = st.selectbox("Geo-Filter: District", districts)
        
    st.markdown("---")
    st.caption("Aadhaar Pulse v2.0 | Pro Edition")

# --- Filtering Global Data ---
mask = (df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))
if selected_state != "All Regions":
    mask = mask & (df['state'] == selected_state)
if selected_district != "All Districts":
    mask = mask & (df['district'] == selected_district)

filtered_df = df[mask].copy()

# --- Header ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("🇮🇳 Aadhaar Pulse AI")
    st.markdown(f"**Analytics Command Center** • Data Integrity: *Raw Integrated Stream*")
with col_head2:
    if not filtered_df.empty:
        last_update = filtered_df['date'].max().strftime('%d %b %Y')
        st.markdown(f"<div style='text-align:right; color:gray; padding-top:20px'>Data updated: {last_update}</div>", unsafe_allow_html=True)

# Tabs Structure
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Executive Summary", 
    "🚚 Migration & Demographics", 
    "⚖️ Fraud & Integrity", 
    "🔮 Predictive Intelligence", 
    "🏥 Network Planning"
])

# Utility for Custom Metric Card
def render_metric(label, value, color="#4e73df", prefix=""):
    st.markdown(f"""
    <div class="metric-card" style="border-left: 6px solid {color};">
        <div class="metric-label" style="color:{color}">{label}</div>
        <div class="metric-value">{prefix}{value}</div>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 1: EXECUTIVE SUMMARY ---
with tab1:
    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    else:
        # 1. KPI Row
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        total_enrol = filtered_df['total_enrolment'].sum()
        total_updates = filtered_df['total_updates'].sum()
        total_bio = filtered_df['total_bio_updates'].sum()
        avg_ausi = filtered_df['ausi_score'].mean()
        
        with kpi1: render_metric("Total New Enrolments", f"{total_enrol:,.0f}", "#36b9cc")
        with kpi2: render_metric("Total Lifecycle Updates", f"{total_updates:,.0f}", "#4e73df")
        with kpi3: render_metric("Critical Bio-Updates", f"{total_bio:,.0f}", "#f6c23e")
        with kpi4: render_metric("Network Stress (AUSI)", f"{avg_ausi:.1f}", "#e74a3b")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 2. Main Visualizations
        col_viz1, col_viz2 = st.columns([2, 1])
        
        # A. Area Chart (Temporal Trend)
        with col_viz1:
            st.markdown("### 📈 Operational Volume Trends")
            daily_stats = filtered_df.groupby('date')[['total_enrolment', 'total_updates']].sum().reset_index()
            
            fig_trend = px.area(
                daily_stats, x='date', y=['total_enrolment', 'total_updates'],
                labels={'value': 'Transactions', 'date': 'Timeline', 'variable': 'Metric'},
                color_discrete_map={'total_enrolment': '#1cc88a', 'total_updates': '#4e73df'},
                template="plotly_white",
                height=400
            )
            fig_trend.update_layout(
                legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"),
                margin=dict(l=20, r=20, t=20, b=20),
                hovermode="x unified"
            )
            st.plotly_chart(fig_trend, use_container_width=True)
            
        # B. Hierarchical Sunburst
        with col_viz2:
            st.markdown("### 🗺️ Regional Composition")
            # If state selected, show districts. If All, show States.
            if selected_state == "All Regions":
                path = ['state']
                title = "Volume by State"
            else:
                path = ['district']
                title = "Volume by District"
                
            fig_sun = px.pie(
                filtered_df, 
                names=path[0], 
                values='total_updates',
                hole=0.5,
                color_discrete_sequence=px.colors.qualitative.Prism,
                height=400
            )
            fig_sun.update_traces(textposition='inside', textinfo='percent+label')
            fig_sun.update_layout(showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
            st.plotly_chart(fig_sun, use_container_width=True)

# --- TAB 2: MIGRATION & DEMOGRAPHICS ---
with tab2:
    st.markdown("### Urban Shift & Demographic Movement Analysis")
    
    if not filtered_df.empty:
        try:
            # Re-run classification on filtered subset
            df_mig = classify_growth_patterns(filtered_df)
            
            col_m1, col_m2 = st.columns([3, 1])
            
            with col_m1:
                # Growth Matrix Scatter
                fig_mig = px.scatter(
                    df_mig,
                    x='organic_growth_rate',
                    y='migration_flux',
                    color='growth_category',
                    size='total_updates',
                    hover_name='district',
                    hover_data=['state', 'total_enrolment'],
                    title="Growth Matrix: Migration Flux vs. Organic Growth",
                    labels={'organic_growth_rate': 'Organic Growth (Births)', 'migration_flux': 'Migration Inflow (Flux)'},
                    template="plotly_white",
                    color_discrete_map={
                        'Migration Hub': '#e74a3b', # Red
                        'Organic Growth': '#1cc88a', # Green
                        'Stagnant': '#858796', # Grey
                        'Balanced': '#4e73df'  # Blue
                    },
                    height=550
                )
                # Add Reference Lines
                fig_mig.add_shape(type="line", x0=df_mig['organic_growth_rate'].min(), y0=df_mig['migration_flux'].median(), x1=df_mig['organic_growth_rate'].max(), y1=df_mig['migration_flux'].median(),
                                line=dict(color="gray", width=1, dash="dash"))
                fig_mig.add_shape(type="line", x0=df_mig['organic_growth_rate'].median(), y0=df_mig['migration_flux'].min(), x1=df_mig['organic_growth_rate'].median(), y1=df_mig['migration_flux'].max(),
                                line=dict(color="gray", width=1, dash="dash"))
                
                st.plotly_chart(fig_mig, use_container_width=True)
            
            with col_m2:
                st.markdown("#### Top Migration Destinations")
                st.caption("Districts with highest inflow flux")
                
                hubs = df_mig[df_mig['growth_category'] == 'Migration Hub'].sort_values('migration_flux', ascending=False).head(10)
                
                # Custom HTML Table
                table_html = "<table style='width:100%; border-collapse: collapse;'>"
                table_html += "<tr style='border-bottom: 2px solid #ddd; text-align: left;'><th>District</th><th style='text-align: right;'>Flux Score</th></tr>"
                for _, row in hubs.iterrows():
                    table_html += f"<tr style='border-bottom: 1px solid #eee; height: 40px;'><td>{row['district']}</td><td style='text-align: right; font-weight: bold;'>{row['migration_flux']:.2f}</td></tr>"
                table_html += "</table>"
                
                st.markdown(table_html, unsafe_allow_html=True)
                
        except Exception as e:
            st.info("Insufficient data range for migration calculations.")

# --- TAB 3: FRAUD & RISK ---
with tab3:
    st.markdown("### ⚖️ Fraud Radar & Data Integrity")
    
    col_f1, col_f2 = st.columns([1, 1])
    
    # 1. Anomaly Radar
    with col_f1:
        st.markdown("#### Anomaly Detection Radar")
        st.caption("High volume operations vs Enrolments. Red bubbles indicate statistical outliers.")
        
        # Ensure is_anomaly exists
        if 'is_anomaly' in filtered_df.columns:
             # Convert boolean to string for categorical coloring
            filtered_df['Anomaly Status'] = filtered_df['is_anomaly'].apply(lambda x: "Anomaly" if x else "Normal")
            
            fig_anom = px.scatter(
                filtered_df,
                x='total_enrolment',
                y='total_updates',
                color='Anomaly Status',
                size='ausi_score',
                hover_name='district',
                color_discrete_map={"Anomaly": '#e74a3b', "Normal": '#d1d3e2'},
                template="plotly_white",
                height=450,
                log_x=True, log_y=True # Log scale often better for variances
            )
            st.plotly_chart(fig_anom, use_container_width=True)
        else:
            st.warning("Anomaly module did not return status.")
            
    # 2. Duplicate Report
    with col_f2:
        st.markdown("#### Data Integrity Report (Raw Stream)")
        st.caption("Direct integrity check on uncleaned data stream.")
        
        # Raw Data Check
        # Filter raw_df based on sidebar selection
        raw_mask = (raw_df['date'] >= pd.to_datetime(date_range[0])) & (raw_df['date'] <= pd.to_datetime(date_range[1]))
        if selected_state != "All Regions":
            raw_mask = raw_mask & (raw_df['state'] == selected_state)
        
        raw_view = raw_df[raw_mask]
        
        duplicates = raw_view.duplicated(subset=['date', 'state', 'district', 'pincode'])
        dup_count = duplicates.sum()
        
        # Display Metric
        st.markdown(f"""
        <div style="background-color: #fff3cd; border: 1px solid #ffeeba; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 20px;">
            <div style="font-size: 16px; color: #856404;">Suspected Duplicate Records</div>
            <div style="font-size: 36px; font-weight: bold; color: #856404;">{dup_count:,}</div>
            <div style="font-size: 12px; color: #856404;">Preserved for Fraud Analysis</div>
        </div>
        """, unsafe_allow_html=True)
        
        if dup_count > 0:
            st.markdown("**Sample Evidence Table (Raw):**")
            st.dataframe(
                raw_view[duplicates].head(50),
                height=250,
                use_container_width=True
            )

# --- TAB 4: FORECASTING ---
with tab4:
    st.markdown("### 🔮 Biometric Demand Forecast")
    
    col_pred1, col_pred2 = st.columns([1, 3])
    
    with col_pred1:
        st.markdown("""
        <div style="background-color: #e8f0fe; padding: 15px; border-radius: 8px; color: #0c5460;">
            <strong>Methodology</strong><br>
            Predictive model uses aging cohorts (children turning 5/15) to forecast mandatory biometric update surges.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        pred_state = st.selectbox("Select State", df['state'].unique(), key='ps')
        
        # Filter districts by state
        d_list = df[df['state'] == pred_state]['district'].unique()
        pred_dist = st.selectbox("Select District", d_list, key='pd')
        
        forecast_days = st.slider("Prediction Horizon (Days)", 15, 60, 30)
        
        run_btn = st.button("Generate Forecast", type="primary", use_container_width=True)
        
    with col_pred2:
        if run_btn:
            with st.spinner(f"Running Regression Model for {pred_dist}..."):
                hist, forecast = predict_biometric_demand(df, pred_dist, forecast_days)
                
                if hist is not None and not hist.empty:
                    fig_cast = go.Figure()
                    
                    # Historical Area
                    fig_cast.add_trace(go.Scatter(
                        x=hist['date'], y=hist['total_bio_updates'],
                        mode='lines', name='Historical Load',
                        line=dict(color='#4e73df', width=2),
                        fill='tozeroy', fillcolor='rgba(78, 115, 223, 0.1)'
                    ))
                    
                    # Forecast Line
                    fig_cast.add_trace(go.Scatter(
                        x=forecast['date'], y=forecast['predicted_demand'],
                        mode='lines+markers', name='AI Prediction',
                        line=dict(color='#e74a3b', width=3, dash='dash')
                    ))
                    
                    fig_cast.update_layout(
                        title=f"Demand Outlook: {pred_dist}, {pred_state}",
                        xaxis_title="Timeline",
                        yaxis_title="Biometric Updates",
                        template="plotly_white",
                        hovermode="x unified",
                        height=500
                    )
                    st.plotly_chart(fig_cast, use_container_width=True)
                    
                    # Insight
                    avg_load = forecast['predicted_demand'].mean()
                    if avg_load > 200:
                         st.error(f"⚠️ High Alert: Expecting avg {int(avg_load)} daily updates. Mobilize extra kits.")
                    else:
                        st.success(f"✅ Normal Load: Expecting avg {int(avg_load)} daily updates.")
                        
                else:
                    st.warning("Insufficient historical data points to generate forecast.")
        else:
            st.info("👈 Select parameters and click 'Generate Forecast' to visualize trends.")

# --- TAB 5: INFRASTRUCTURE ---
with tab5:
    st.markdown("### 🏥 Network Optimization & Seva Center Planning")
    
    # Recalculate clusters
    df_plan = calculate_migration_score(filtered_df)
    df_plan = cluster_districts(df_plan)
    
    col_infra1, col_infra2 = st.columns([2, 1])
    
    with col_infra1:
        fig_cluster = px.scatter(
            df_plan,
            x='total_updates',
            y='ausi_score',
            color='recommendation',
            size='impact_score',
            hover_name='district',
            title="Strategic Resource Allocation Matrix",
            color_discrete_map={
                'New Center Required': '#e74a3b', 
                'Mobile Van Required': '#f6c23e', 
                'Mobile Van Required (Migration Hub)': '#8e44ad',
                'Monitor': '#1cc88a'
            },
            template="plotly_white",
            height=550
        )
        st.plotly_chart(fig_cluster, use_container_width=True)
        
    with col_infra2:
        st.markdown("#### Strategic Recommendations")
        
        recs = df_plan['recommendation'].value_counts()
        
        # Modern Card List
        for rec_type, count in recs.items():
            color = "#1cc88a"
            icon = "✅"
            if "New Center" in rec_type: 
                color = "#e74a3b"
                icon = "🚨"
            elif "Mobile Van" in rec_type: 
                color = "#f6c23e"
                icon = "🚛"
            
            st.markdown(f"""
            <div style="display:flex; justify-content:space-between; align-items:center; padding: 12px; background:white; border-radius:8px; margin-bottom:10px; border-left: 4px solid {color}; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <div style="font-weight:600; color:#5a5c69;">{icon} {rec_type}</div>
                <div style="font-weight:bold; color:{color}; font-size:18px;">{count}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### Priority Districts")
        prio = df_plan[df_plan['recommendation'] != 'Monitor'].sort_values('impact_score', ascending=False).head(5)
        st.dataframe(prio[['district', 'ausi_score', 'recommendation']], use_container_width=True, hide_index=True)

