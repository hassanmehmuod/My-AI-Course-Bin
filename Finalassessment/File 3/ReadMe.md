Task 3: UnitedHealth (UNH) Stock Price Forecasting

Dataset
Top 10 Healthcare Companies dataset — daily stock data (2000–2023). UnitedHealth Group (UNH) sheet used for this task.

Objective
Forecast next-day closing price using deep learning time series models (RNN, LSTM, GRU).

Steps
- Loaded UNH sheet, cleaned Date column (removed embedded Korean AM/PM text, parsed to datetime), sorted chronologically
- Performed EDA: price trend over time, price distribution, volume over time, correlation heatmap
- Scaled closing price (0–1) and built sliding-window sequences (60-day windows)
- Split data chronologically (80/20, no shuffling) to preserve time order
- Trained SimpleRNN, LSTM, and GRU models with identical architecture for fair comparison
- Evaluated using RMSE, MAE, and R² on the test set

Results
GRU performed best by far: RMSE $8.60, R² 0.9934. LSTM: RMSE $26.63, R² 0.9365. SimpleRNN: RMSE $31.22, R² 0.9127. GRU's predictions closely tracked actual price movement throughout the test period.

Limitation
Model only uses historical closing price; doesn't account for external factors like news, interest rates, or broader economic conditions.