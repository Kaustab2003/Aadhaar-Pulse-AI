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

##  Project Structure

`ash
Aadhaar-Pulse-AI/
 data/                   # Raw and Processed Datasets
 notebooks/              # Jupyter Notebooks for Deep Dive Analysis
    01_data_understanding.ipynb
    02_data_cleaning.ipynb
    03_exploratory_analysis.ipynb
    ...
    07_insights_generation.ipynb
 src/                    # Core Analytical Engine
    analytics/          # Migration & Enrolment Logic
    metrics/            # AUSI Calculation
    models/             # Forecasting, Anomaly Det, Clustering
    preprocessing/      # Data Pipelines
 dashboard/              # Streamlit Interactive App
    app.py
 reports/                # Generated CSV exports
 README.md
`

---

##  Tech Stack
*   **Language:** Python 3.9+
*   **Analysis:** Pandas, NumPy, Scikit-Learn (Isolation Forest, K-Means, Linear Regression)
*   **Visualization:** Plotly Express, Seaborn
*   **Dashboard:** Streamlit
*   **DevOps:** VS Code, Git

---

##  Quick Start

### 1. Prerequisites
Ensure you have Python installed. Install dependencies (if equirements.txt exists, otherwise install manually):
`ash
pip install pandas numpy scikit-learn plotly streamlit seaborn matplotlib
`

### 2. Run the Data Pipeline
Execute the notebooks in order to process raw data and generate models:
*   Run 
otebooks/01_data_understanding.ipynb
*   Run 
otebooks/02_data_cleaning.ipynb (Creates merged_master_table.csv)
*   Run 
otebooks/07_insights_generation.ipynb (Generates Reports)

### 3. Launch the Dashboard
Start the interactive command center:
`ash
streamlit run dashboard/app.py
`

---

##  Future Roadmap
*   **Geospatial Integration:** Plotting specific Seva Center lat/long coordinates.
*   **Real-time API:** Integration with UIDAI real-time distinct count APIs.
*   **LLM Assistant:** A chatbot to query district stats in natural language (e.g., "Which districts in UP need vans today?").
