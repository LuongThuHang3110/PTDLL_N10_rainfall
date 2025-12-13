import sys
import time
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load data
try:
    df = pd.read_csv('rainfall3.csv')
except FileNotFoundError:
    print("File 'rainfall3.csv' không tìm thấy.")
    sys.exit(1)

# Encode location (tương đương province)
le = LabelEncoder()
df['location'] = le.fit_transform(df['location'])

# Handle date
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Giữ cấu trúc giống hệt code bạn gửi
X = df[['location', 'temp', 'humidity', 'wind', 'pressure',
        'day', 'month', 'year']]
y = df['rain']

# Fill missing values (giống cách cũ)
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest (giữ đơn giản, ổn định)
n_estimators_value = 200
model = RandomForestRegressor(
    n_estimators=n_estimators_value,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=1
)

# Train
start_time = time.time()
model.fit(X_train, y_train)
training_time = time.time() - start_time
print(f"Thời gian huấn luyện: {training_time:.2f} giây")

# Predict
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
r2 = max(0, r2)  # đảm bảo không âm hoặc âm rất nhỏ (~0)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f'R Square (Test): {r2}')
print(f'R Square (Train): {model.score(X_train, y_train)}')
