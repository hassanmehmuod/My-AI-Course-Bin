import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense, Dropout

df = pd.read_excel(
    'D:\\Work\\Github\\My-AI-Course-Bin\\Finalassessment\\File 3\\Top 10 Healthcare Companies in the United States.xlsx',
    sheet_name='UnitedHealth Group Inc. (UNH)',
    header=4
)

df.columns = ['Date', 'Close', 'High', 'Low', 'Volume']

print(df.shape)
print(df.head())
print(df.dtypes)


df['Date'] = df['Date'].str.replace('오후', 'PM').str.replace('오전', 'AM')
df['Date'] = pd.to_datetime(df['Date'], format='%Y. %m. %d %p %I:%M:%S')

df = df.sort_values('Date').reset_index(drop=True)

print(df.head())
print(df.dtypes)
print("Date range:", df['Date'].min(), "to", df['Date'].max())

plt.figure(figsize=(14,5))
plt.plot(df['Date'], df['Close'])
plt.title('UnitedHealth (UNH) Closing Price Over Time (2000-2023)')
plt.xlabel('Date')
plt.ylabel('Close Price ($)')
plt.show()

# Distribution of daily closing prices
plt.figure(figsize=(8,5))
sns.histplot(df['Close'], kde=True)
plt.title('Distribution of Closing Prices')
plt.show()

# Volume over time
plt.figure(figsize=(14,4))
plt.plot(df['Date'], df['Volume'], color='orange', alpha=0.6)
plt.title('Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

# Correlation between Close, High, Low, Volume
plt.figure(figsize=(6,5))
sns.heatmap(df[['Close','High','Low','Volume']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

close_prices = df[['Close']].values
scaler = MinMaxScaler(feature_range=(0,1))
scaled_close = scaler.fit_transform(close_prices)

window_size = 60

X, y = [], []
for i in range(window_size, len(scaled_close)):
    X.append(scaled_close[i-window_size:i, 0])
    y.append(scaled_close[i, 0])

X, y = np.array(X), np.array(y)

X = X.reshape((X.shape[0], X.shape[1], 1))

print("X shape:", X.shape)
print("y shape:", y.shape)

split_index = int(len(X) * 0.8)

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

#Model 1: SimpleRNN

rnn_model = Sequential([
    SimpleRNN(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    SimpleRNN(50),
    Dropout(0.2),
    Dense(1)
])

rnn_model.compile(optimizer='adam', loss='mean_squared_error')

rnn_history = rnn_model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)
#Model 2: LSTM
lstm_model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
])

lstm_model.compile(optimizer='adam', loss='mean_squared_error')

lstm_history = lstm_model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)
#Model 3: GRU
gru_model = Sequential([
    GRU(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    GRU(50),
    Dropout(0.2),
    Dense(1)
])

gru_model.compile(optimizer='adam', loss='mean_squared_error')

gru_history = gru_model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# Get predictions from all 3 models
rnn_pred = rnn_model.predict(X_test)
lstm_pred = lstm_model.predict(X_test)
gru_pred = gru_model.predict(X_test)

# Inverse transform back to actual dollar prices (undo the 0-1 scaling)
y_test_actual = scaler.inverse_transform(y_test.reshape(-1,1))
rnn_pred_actual = scaler.inverse_transform(rnn_pred)
lstm_pred_actual = scaler.inverse_transform(lstm_pred)
gru_pred_actual = scaler.inverse_transform(gru_pred)

# Compare metrics across all 3 models
for name, pred in [('SimpleRNN', rnn_pred_actual), ('LSTM', lstm_pred_actual), ('GRU', gru_pred_actual)]:
    rmse = np.sqrt(mean_squared_error(y_test_actual, pred))
    mae = mean_absolute_error(y_test_actual, pred)
    r2 = r2_score(y_test_actual, pred)
    print(f"\n{name}")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R2 Score: {r2:.4f}")

plt.figure(figsize=(14,6))
plt.plot(y_test_actual, label='Actual Price', color='black', linewidth=2)
plt.plot(rnn_pred_actual, label='SimpleRNN Prediction', alpha=0.7)
plt.plot(lstm_pred_actual, label='LSTM Prediction', alpha=0.7)
plt.plot(gru_pred_actual, label='GRU Prediction', alpha=0.7)
plt.title('UNH Stock Price: Actual vs Predicted (Test Set)')
plt.xlabel('Time Steps (Test Period)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# Bar chart comparing RMSE across models
model_names = ['SimpleRNN', 'LSTM', 'GRU']
rmse_scores = [
    np.sqrt(mean_squared_error(y_test_actual, rnn_pred_actual)),
    np.sqrt(mean_squared_error(y_test_actual, lstm_pred_actual)),
    np.sqrt(mean_squared_error(y_test_actual, gru_pred_actual))
]

plt.figure(figsize=(7,5))
sns.barplot(x=model_names, y=rmse_scores)
plt.title('RMSE Comparison Across Models')
plt.ylabel('RMSE ($)')
plt.show()

print(""In this task, I built a model to predict UnitedHealth Group's (UNH) daily stock closing price using data from 2000 to 2023. First, I cleaned the date column and scaled the price values between 0 and 1, since deep learning models work better with scaled data. Then I created sequences using the past 60 days of prices to predict the next day's price. I trained three types of models — SimpleRNN, LSTM, and GRU — using the same setup for each so I could fairly compare them. I made sure to split the data by time (not randomly), so the model was tested only on future prices it hadn't seen before, which is more realistic for forecasting. The GRU model performed the best by far, with very low error (RMSE of $8.60) and an R² score of 0.9934, meaning it was able to track the real price movements very closely. LSTM did okay but tended to predict slightly higher prices than actual, while SimpleRNN performed the worst, likely because it has a harder time remembering patterns over longer time periods compared to LSTM and GRU. One limitation of this model is that it only looks at past prices and doesn't consider other real-world factors like news, interest rates, or economic events that can also affect stock prices."")