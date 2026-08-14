Task 4: FDA AI Medical Device Review Time Forecasting

Dataset
FDA AI Medical Devices dataset — 1,524 AI-enabled device authorizations (1995–2026), including decision dates and review durations.

Objective
Forecast device review time (review_days) using deep learning time series models (RNN, LSTM, GRU).

Steps
- Loaded data, parsed decision dates, sorted chronologically
- Performed EDA: review days over time, distribution, authorizations per year, review days by pathway
- Scaled `review_days` (0–1) and built sliding-window sequences (window size 15, smaller than Task 3 due to limited dataset size)
- Split data chronologically (80/20)
- Trained SimpleRNN, LSTM, and GRU models with identical architecture
- Evaluated using RMSE, MAE, and R²

Results
All three models performed poorly (R² near zero or slightly negative), indicating no meaningful sequence-based pattern in individual device review times — each device's review time depends on its own complexity and product type, not on preceding devices. As a supplementary check, monthly authorization volume was analyzed separately and showed a strong, clear upward trend (near 0/month in 2016 to 40+/month by 2026), confirming the dataset does contain real time-based structure — just not in the specific sequence modeled here.

Limitation
A feature-based regression model (using product code, pathway, specialty) would likely predict review time more effectively than a sequence-based approach for this dataset.