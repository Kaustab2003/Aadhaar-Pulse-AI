# System Architecture

## 1. Raw Data Layer (The Zero-Loss Pipeline)
*   **Ingestion**: Direct consumption of disparate CSV streams (Biometric, Demographic, Enrolment) via a custom merge strategy.
*   **Preservation Logic**: Unlike standard ETL (Extract-Transform-Load) pipelines, this layer employs a "Tag-and-Keep" strategy for anomalies. Missing values and duplicates are flagged with metadata tags (`is_duplicate_signal`, `biometric_failure_event`) rather than being dropped, preserving them for the anomaly detection engines.

## 2. Intelligence Core (Python/Scikit-Learn)
*   **Growth Matrix Engine**: A vector classification model that analyzes the ratio of `New Enrolments` (Births) to `Updates` (Migration) to classify every district into one of four quadrants (e.g., "High-Growth Migration Hub").
*   **Seva District Planner**:
    *   *Algorithm*: K-Means Clustering tailored for geospatial optimization.
    *   *Constraint Handling*: Incorporates a fallback logic system (Rule-Based Assignment) for low-sample districts where statistical clustering is mathematically unstable (N < 3), ensuring 100% coverage even for rural outliers.

## 3. Visualization "Command Center" (Streamlit)
*   **Architecture**: Single-Page Application (SPA) built on Streamlit `st.experimental_fragment` for high performance.
*   **Interface**: Custom CSS implementation mimicking enterprise BI tools (Tableau/PowerBI) with a focus on high-contrast "Dark Mode" aesthetics for government operations centers.
*   **Interactivity**: Real-time cross-filtering where a selection in the "Executive Summary" propagates constraints to the "Cluster Map" and "Anomaly Stream" instantly.
