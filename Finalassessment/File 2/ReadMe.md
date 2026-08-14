Task 2: US Hospitals Clustering

Dataset
USA Hospitals dataset (HIFLD) — 7,570 hospitals with location, bed count, ownership, and type data.

Objective
Group hospitals into clusters based on size and location using unsupervised learning.

Steps
- Loaded and inspected data; identified `-999` as a placeholder for missing values
- Dropped `TTL_STAFF` column (99.9% missing/placeholder)
- Removed rows where `BEDS` was `-999` (~650 rows), reducing dataset to 6,919 usable hospitals
- Scaled `BEDS`, `LATITUDE`, `LONGITUDE` using StandardScaler
- Used the elbow method to determine optimal cluster count (k=4)
- Trained KMeans and evaluated using silhouette score
- Visualized clusters geographically and by bed count distribution

Results
Silhouette score of 0.355 (moderate separation). Three clusters represented small-to-mid-size hospitals grouped roughly by US region (Midwest, West, South, ~95–120 avg beds). One cluster stood out as large regional medical centers (649 hospitals, ~570 avg beds), spread across multiple regions.

Limitation
Clustering was based only on bed count and location; adding features like hospital type or ownership could reveal more nuanced groupings.