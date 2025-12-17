import pandas as pd
import statsmodels.api as sm
from joblib import dump, load

# =========================
# 1. Đọc dữ liệu
# =========================
data = pd.read_csv("rainfall3.csv")

print("5 dòng đầu:")
print(data.head())

# Tiền xử lý
data = data.drop(columns=['date'])

# Chọn cột cần thiết
data = data[['rain', 'temp', 'humidity', 'wind',
             'pressure', 'location', 'rain_category']]

data_clean = data.dropna() # Xoá missing

X = data_clean.drop(labels='rain', axis=1) #  Tách X và y
y = data_clean['rain']
# ⚠ ÉP KIỂU SỐ (QUAN TRỌNG)
X = X.astype(float)
y = y.astype(float)
X = sm.add_constant(X)   # 4. Thêm hằng số

model = sm.OLS(y, X).fit() # 5. Huấn luyện OLS
# 6. Đánh giá
print("\n========== OLS REGRESSION RESULTS ==========\n")
print(model.summary())
dump(model, "linear_regression_model.joblib") # 7. Lưu mô hình
print("\n✔ Mô hình đã được lưu!")
model = load("linear_regression_model.joblib") # Dự đoán thử

new_data = pd.DataFrame({
    'const': [1],
    'temp': [30],
    'humidity': [80],
    'wind': [5],
    'pressure': [1010],
    'location': [1],
    'rain_category': [0]
})

rain_pred = model.predict(new_data)
print("\n🌧 Lượng mưa dự đoán:", rain_pred.iloc[0])

#Đoạn code này dùng để tạo một bộ dữ liệu mới (1 quan sát)
# với các giá trị cụ thể của các biến độc lập, nhằm dự đoán lượng mưa bằng mô hình hồi quy đã huấn luyện.
# const: hằng số chặn (intercept) của mô hình hồi quy
# temp = 30: nhiệt độ (°C)
# humidity = 80: độ ẩm (%)
# wind = 5: tốc độ gió
# pressure = 1010: áp suất khí quyển
# location = 1: mã hoá khu vực
# rain_category = 0: nhóm mức mưa