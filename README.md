# 🇮🇳 Aadhaar Pulse AI
### *Predictive Lifecycle Analytics & Dynamic Resource Optimization for Digital Identity*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)](https://streamlit.io/)
[![Prophet](https://img.shields.io/badge/AI-Prophet%20Forecasting-orange)](https://facebook.github.io/prophet/)
[![Plotly](https://img.shields.io/badge/Viz-Mapbox%20Geospatial-green)](https://plotly.com/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aadhaar-pulse-ai-roka94p7fkfh6tvy4jvo54.streamlit.app/)

**Aadhaar Pulse AI** is an intelligent decision support system designed to shift national identity infrastructure from *reactive* management to *predictive* optimization. By analyzing enrolment trends, biometric updates, and demographic shifts, the system forecasts demand, detects migration clusters, and optimizes Seva Center placement in real-time.

---

## 🚀 Key Innovations (Hackathon Winning Features)

This project introduces 5 core modules that redefine how identity infrastructure is managed:

### 1. 🌍 Geospatial War Room (New!)
*   **Visually Intuitive:** Real-time **Mapbox Heatmaps** visualize the **Aadhaar Update Stress Index (AUSI)** across districts.
*   **Actionable:** Instantly identifies "Red Zones" where infrastructure is overwhelmed vs. "Green Zones" underutilized.

### 2. 🔮 Age-Transition Biometric Prediction Engine
*   **Problem:** 60% of mandatory biometric updates (at age 5 and 15) are missed due to lack of planning.
*   **Tech Stack:** Uses **Facebook Prophet** (Time-Series AI) to forecast exactly when the 5-17 age cohort surge will hit specific districts 90 days in advance.
*   **Impact:** Zero-delay biometric updates for children by pre-positioning kits.

### 3. 🤖 AI Narrative Insights
*   **Problem:** Executives don't have time to interpret complex charts.
*   **Solution:** An **Automated Narrative Engine** that converts data patterns into plain text alerts (e.g., *"🚨 Critical Alert: Patna facing 15% unexpected surge in biometric demand"*).

### 4. 🚚 Migration & Urban Shift Detector
*   **Insight:** Classifies districts into growth quadrants (e.g., "Migration Hub" vs "Organic Growth") by correlating Demographic Inflows vs. Birth Rates.
*   **Impact:** Proactive deployment of "Address Update Kiosks" in high-migration corridors before queues form.

### 5. ⚖️ Fraud & Anomaly Radar
*   **Tech Stack:** Uses **Isolation Forest** algorithms to detect statistical outliers in daily volume frequency.
*   **Use Case:** Flags suspicious activity like 500% spike in updates in a rural pincode (potential operator fraud).

---

## 📊 Dashboard Features
The project includes a fully interactive Executive Dashboard (`dashboard/app.py`):

1.  **Executive Summary:** KPI Cards, Time-Series Area Charts, and **Geospatial Heatmaps**.
2.  **Migration Matrix:** Scatter plot identifying "Urban Booms" vs "Stagnant" regions.
3.  **Fraud Radar:** Visual anomaly detection bubbles.
4.  **Simulation & Forecasting:** Run specific "what-if" scenarios for any district using the Prophet model.
5.  **Smart Planner:** Cluster-based recommendations for opening **New Centers** vs. deploying **Mobile Vans**.

---

## 📂 Project Structure

```bash
Aadhaar-Pulse-AI/
├── dashboard/                  
│   └── app.py                  # 🚀 MAIN ENTRY POINT: Streamlit Executive Dashboard
├── src/
│   ├── analytics/              # Business Logic (Migration, Insights)
│   ├── metrics/                # AUSI Calculation Logic
│   ├── models/                 # AI Models (Prophet, Isolation Forest, K-Means)
│   ├── preprocessing/          # ETL Pipelines
│   └── utils/                  # Geo-utilities & Helpers
├── data/                       # Raw & Processed Data
├── notebooks/                  # Experimental Jupyter Notebooks
├── generate_missing_data.py    # Synthetic Data Generator (Jan-Feb 2025)
├── run_pipeline.py             # ETL Trigger Script
└── requirements.txt            # Dependencies
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Data (Optional)
If running for the first time, generate the full year dataset:
```bash
python generate_missing_data.py
python run_pipeline.py
```

### 4. Launch Dashboard 🚀
```bash
streamlit run dashboard/app.py
```

---

## 🧠 Tech Stack
*   **Frontend:** Streamlit, Plotly Express, Mapbox
*   **AI/ML:** Facebook Prophet (Forecasting), Scikit-Learn (Isolation Forest, K-Means)
*   **Data Engineering:** Pandas, NumPy
*   **Analytics:** Geographic Clustering, Time-Series Decomposition

---

> *Built for the [Hackathon Name] to empower UIDAI with next-gen intelligence.*
