# Aadhaar Pulse AI 
### *Predictive Lifecycle Analytics & Dynamic Resource Optimization for Aadhaar*

**Aadhaar Pulse AI** is an intelligent decision support system designed to shift Aadhaar operations from *reactive* management to *predictive* optimization. By analyzing enrolment trends, biometric updates, and demographic shifts, the system forecasts demand, detects migration clusters, and optimizes Seva Center placement in real-time.

---

##  Key Innovations (Patent-Pending Logic)

This project introduces 5 core modules that redefine how identity infrastructure is managed:

### 1. Age-Transition Biometric Prediction Engine
*   **Problem:** 60% of mandatory biometric updates (at age 5 and 15) are missed due to lack of awareness or access.
*   **Solution:** Uses historical 0-5 enrolment data to predict exactly when and where the 5-17 update surge will hit 5 years later.
*   **Impact:** Zero-delay biometric updates for children.

### 2. Aadhaar Update Stress Index (AUSI)
*   **Problem:** Static centers often sit empty while mobile camps are overwhelmed.
*   **Solution:** A normalized "Pressure Score" for every district calculated as: 
    c:\Users\Kaustab das\Desktop\Aadhaar Pulse AI\README.md \text{AUSI} = \frac{\text{Daily Updates (Bio + Demo)}}{\text{Cumulative Enrolment Base}} c:\Users\Kaustab das\Desktop\Aadhaar Pulse AI\README.md
*   **Impact:** Real-time identification of overburdened infrastructure.

### 3. Migration & Urban Shift Detector (Growth Matrix)
*   **Problem:** Migrant workers struggle to update addresses, leading to exclusion.
*   **Solution:** Classifies districts into growth quadrants (e.g., "Migration Hub" vs "Organic Growth") by comparing Demographic Inflow vs Birth Rates.
*   **Impact:** Proactive deployment of "Address Update Kiosks" in high-inflow zones.

### 4. Fraud & Anomaly Radar
*   **Problem:** Unusual spikes in updates can indicate operator fraud or data entry errors.
*   **Solution:** Uses **Isolation Forest** algorithms to detect statistical outliers in daily volume vectors (e.g., 500% spike in updates in a rural pincode).
*   **Impact:** Immediate fraud alerts.

### 5. Smart Aadhaar Seva Center Planner
*   **Problem:** Centers are allocated based on static population, not dynamic load.
*   **Solution:** An AI-driven clustering engine (K-Means) that recommends:
    *    **New Permanent Center:** High Volume + High Stress.
    *    **Mobile Van (Migration):** Sporadic Load + High Migration Flux.
    *    **Monitor:** Stable zones.

---

## 📂 Project Structure

```bash
Aadhaar-Pulse-AI/
├── data/                       # Raw and Processed Datasets
├── notebooks/                  # Interactive Analysis & Reports
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_trend_analysis.ipynb
│   ├── 05_anomaly_detection.ipynb
│   ├── 06_prediction_models.ipynb
│   ├── 07_insights_generation.ipynb
│   └── 08_dashboard_visualization.ipynb   <-- (New) Professional Dashboard
├── src/                        # Core Analytical Engine
│   ├── analytics/              # Business Logic (Migration, Enrolment)
│   ├── metrics/                # Custom Metrics (AUSI)
│   ├── models/                 # ML Models (Isolation Forest, Ranking, Forecasting)
│   └── preprocessing/          # ETL Pipelines
├── run_pipeline.py             # Main ETL entry point
├── test_src_all.py             # Unit/Integration Tests
├── dashboard/                  # Streamlit Interactive App
│   └── app.py
├── reports/                    # Generated CSV exports
└── README.md
```

---

## 🛠 Tech Stack
*   **Language:** Python 3.9+
*   **Data Processing:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn (Isolation Forest, K-Means, Linear Regression)
*   **Visualization:** Plotly Express, Seaborn, Matplotlib
*   **Dashboarding:** Streamlit, Jupyter Notebooks
*   **Pipeline:** Custom Python ETL scripts

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python installed. Install dependencies:
```bash
pip install pandas numpy scikit-learn plotly streamlit seaborn matplotlib statsmodels nbformat
```

### 2. Run the Data Pipeline (ETL)
This script processes the raw CSV files from split folders, merges them, and creates the master dataset.
```bash
python run_pipeline.py
```
*Output:* `data/processed/merged_master_table.csv`

### 3. Verify System Health (Testing)
Run the test suite to ensure all analytics, metrics, and models are functioning correctly.
```bash
python test_src_all.py
```

### 4. Interactive Analysis
Open the notebooks in VS Code or Jupyter Lab to explore specific insights:
*   **Start with:** `notebooks/08_dashboard_visualization.ipynb` for the executive summary.
*   **Deep Dive:** Use `notebooks/04_trend_analysis.ipynb` or `notebooks/05_anomaly_detection.ipynb`.

### 5. Launch the Web Dashboard
Start the interactive Streamlit command center:
```bash
streamlit run dashboard/app.py
```

---

##  Future Roadmap
*   **Geospatial Integration:** Plotting specific Seva Center lat/long coordinates.
*   **Real-time API:** Integration with UIDAI real-time distinct count APIs.
*   **LLM Assistant:** A chatbot to query district stats in natural language (e.g., "Which districts in UP need vans today?").
