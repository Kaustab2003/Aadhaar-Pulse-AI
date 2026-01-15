from sklearn.cluster import KMeans
import pandas as pd

def cluster_districts(df):
    """
    Clusters districts based on AUSI and Total Load to recommend center types.
    Updates: Now considers Migration Flux if available for targeted Mobile Van deployment.
    """
    # Aggregate data by district
    agg_dict = {
        'ausi_score': 'mean',
        'total_updates': 'sum',
        'total_enrolment': 'sum'
    }
    
    # If migration_flux is in df, include its mean in aggregation
    if 'migration_flux' in df.columns:
        agg_dict['migration_flux'] = 'mean'
        
    district_summary = df.groupby(['state', 'district']).agg(agg_dict).reset_index()
    
    # Features for K-Means (Strictly Load & Stress)
    X = district_summary[['ausi_score', 'total_updates']]
    
    # Check if we have enough data points for 3 clusters
    n_samples = len(district_summary)
    
    if n_samples < 3:
        # Fallback for small datasets: Rule-based assignment
        # If we filter down to just 1 or 2 districts, clustering fails.
        def simple_rule(row):
            # Fallback thresholds: High stress > 60, Medium > 30
            if row['ausi_score'] > 60 or row['total_updates'] > 10000:
                return 'New Center Required'
            elif row['ausi_score'] > 30:
                return 'Mobile Van Required'
            else:
                return 'Monitor'
                
        district_summary['recommendation'] = district_summary.apply(simple_rule, axis=1)
        district_summary['cluster'] = 0 # Dummy
    else:
        # K-Means Clustering (3 Clusters: Low, Medium, High Priority)
        kmeans = KMeans(n_clusters=3, random_state=42)
        district_summary['cluster'] = kmeans.fit_predict(X)
        
        # Map clusters to recommendations
        centroids = kmeans.cluster_centers_
        # Sum of centroid coords to determine intensity
        intensity = centroids.sum(axis=1)
        cluster_mapping = {i: val for i, val in enumerate(intensity)}
        sorted_clusters = sorted(cluster_mapping, key=cluster_mapping.get)
        
        # Base Map: 0 -> Low (Monitor), 1 -> Medium (Mobile Van), 2 -> High (New Center)
        base_map = {
            sorted_clusters[0]: 'Monitor',
            sorted_clusters[1]: 'Mobile Van Required',
            sorted_clusters[2]: 'New Center Required'
        }
        
        district_summary['recommendation'] = district_summary['cluster'].map(base_map)
    
    # REFINEMENT: Logic 5 - Smart Aadhaar Seva Center Planner
    # "Recommend Mobile Vans for sporadic high spikes (Migration zones)"
    if 'migration_flux' in district_summary.columns:
        # Use 90th percentile of migration flux as threshold for "High Migration Zone"
        mig_threshold = district_summary['migration_flux'].quantile(0.90)
        
        # If a district is marked as 'Monitor' but has HIGH migration flux, upgrade to 'Mobile Van'
        mask_mig = (district_summary['recommendation'] == 'Monitor') & (district_summary['migration_flux'] > mig_threshold)
        district_summary.loc[mask_mig, 'recommendation'] = 'Mobile Van Required (Migration Hub)'
        
    # IMPACT SCORE CALCULATION (For Prioritization)
    # Impact = Stress (AUSI) * Volume (Total Updates)
    # This helps decide WHICH 'New Center' to build first.
    district_summary['impact_score'] = district_summary['ausi_score'] * (district_summary['total_updates'] + 1)
    
    # Normalize Impact Score for readability (0-100)
    max_impact = district_summary['impact_score'].max()
    district_summary['impact_score'] = (district_summary['impact_score'] / max_impact) * 100
        
    return district_summary
