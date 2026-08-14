import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense, Dropout

df = pd.read_csv('D:\\Work\\Github\\My-AI-Course-Bin\\Finalassessment\\File 4\\fda_ai_medical_devices.csv')

print(df.shape)
print(df[['final_decision_date', 'decision_year', 'authorization_pathway', 'review_days']].head())
print(df.dtypes[['final_decision_date', 'review_days']])
print(df['decision_year'].value_counts().sort_index())

df['final_decision_date'] = pd.to_datetime(df['final_decision_date'])

df = df.sort_values('final_decision_date').reset_index(drop=True)

print(df[['final_decision_date', 'review_days']].head())
print(df[['final_decision_date', 'review_days']].tail())
print(df.dtypes[['final_decision_date', 'review_days']])


plt.figure(figsize=(14,5))
plt.scatter(df['final_decision_date'], df['review_days'], alpha=0.4, s=15)
plt.title('FDA Review Days Over Time (per device authorization)')
plt.xlabel('Decision Date')
plt.ylabel('Review Days')
plt.show()


plt.figure(figsize=(8,5))
sns.histplot(df['review_days'], kde=True, bins=40)
plt.title('Distribution of Review Days')
plt.show()

plt.figure(figsize=(12,5))
sns.countplot(x='decision_year', data=df)
plt.title('Number of AI Device Authorizations per Year')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='authorization_pathway', y='review_days', data=df)
plt.title('Review Days by Authorization Pathway')
plt.show()

review_data = df[['review_days']].values

scaler = MinMaxScaler(feature_range=(0,1))
scaled_review = scaler.fit_transform(review_data)


window_size = 15  

X, y = [], []
for i in range(window_size, len(scaled_review)):
    X.append(scaled_review[i-window_size:i, 0])
    y.append(scaled_review[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))

print("X shape:", X.shape)
print("y shape:", y.shape)

split_index = int(len(X) * 0.8)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

def build_model(layer_type):
    model = Sequential([
        layer_type(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
        Dropout(0.2),
        layer_type(50),
        Dropout(0.2),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

rnn_model = build_model(SimpleRNN)
lstm_model = build_model(LSTM)
gru_model = build_model(GRU)

print("Training SimpleRNN...")
rnn_model.fit(X_train, y_train, epochs=20, batch_size=16, validation_split=0.1, verbose=0)

print("Training LSTM...")
lstm_model.fit(X_train, y_train, epochs=20, batch_size=16, validation_split=0.1, verbose=0)

print("Training GRU...")
gru_model.fit(X_train, y_train, epochs=20, batch_size=16, validation_split=0.1, verbose=0)

print("All models trained.")

rnn_pred = rnn_model.predict(X_test)
lstm_pred = lstm_model.predict(X_test)
gru_pred = gru_model.predict(X_test)

y_test_actual = scaler.inverse_transform(y_test.reshape(-1,1))
rnn_pred_actual = scaler.inverse_transform(rnn_pred)
lstm_pred_actual = scaler.inverse_transform(lstm_pred)
gru_pred_actual = scaler.inverse_transform(gru_pred)

for name, pred in [('SimpleRNN', rnn_pred_actual), ('LSTM', lstm_pred_actual), ('GRU', gru_pred_actual)]:
    rmse = np.sqrt(mean_squared_error(y_test_actual, pred))
    mae = mean_absolute_error(y_test_actual, pred)
    r2 = r2_score(y_test_actual, pred)
    print(f"\n{name}")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R2 Score: {r2:.4f}")

monthly_counts = df.set_index('final_decision_date').resample('ME').size()
monthly_counts = monthly_counts[monthly_counts.index >= '2016-01-01']  # trim sparse early years

print(monthly_counts.describe())

plt.figure(figsize=(12,5))
monthly_counts.plot()
plt.title('Monthly AI Device Authorization Volume (2016 onward)')
plt.ylabel('Number of Authorizations')
plt.show()

print("For this task, I tried predicting FDA device review times using deep learning, based on the review times of the past 15 authorizations. I trained SimpleRNN, LSTM, and GRU models the same way as Task 3, but all three performed poorly (R² near zero or slightly negative). To confirm this wasn't a coding error, I checked monthly authorization volume separately and found a strong, clear upward trend — meaning this dataset does have real time-based patterns, just not in the day-to-day sequence of individual review times. Each device's review time depends on that device's own complexity and product type, not on how long the previous few devices took, so there was no real sequence pattern for the model to learn. This shows that applying a time-series model successfully depends on the data actually having a temporal relationship — not just having a date column.")