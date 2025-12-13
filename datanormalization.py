import matplotlib.pyplot as plt
import pandas as pd

# --- 1. Đọc file ---
df = pd.read_csv("rainfall.csv", encoding="utf-8")

# --- 2. Chuẩn hóa tên cột ---
df.columns = df.columns.str.lower().str.strip()

# --- 3. Đổi tên cột nếu muốn ngắn gọn ---
df = df.rename(columns={
    'rainfall_mm': 'rain',
    'temperature_c': 'temp',
    'humidity_pct': 'humidity',
    'wind_speed_kmh': 'wind',
    'pressure_hpa': 'pressure'
})

# --- 4. Chuẩn hóa kiểu dữ liệu ---
num_cols = ['rain', 'temp', 'humidity', 'wind', 'pressure']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

df['date'] = pd.to_datetime(df['date'], errors='coerce')

# --- 5. Chuẩn hóa text ---
df['location'] = df['location'].astype(str).str.strip().str.title()
df['rain_category'] = df['rain_category'].astype(str).str.strip().str.title()

# --- 6. Loại dòng chứa NA thực sự ---
df = df.dropna()

# --- 7. Loại giá trị ngoại lai ---
df = df[(df['pressure'] > 950) & (df['pressure'] < 1050)]
df = df[df['wind'] < 60]           # gió > 60 km/h hiếm → loại
df = df[df['rain'] >= 0]           # mưa âm → sai

# --- 8. Loại dòng trùng lặp ---
df = df.drop_duplicates()

df.to_csv("rainfall1.csv", index=False)
print("Hoàn tất! File sạch đã được tạo: rainfall1.csv")

def missing_data(df):
    """
    Hàm thống kê số lượng và tỷ lệ dữ liệu bị thiếu của từng cột.
    """
    total_missing = df.isnull().sum()
    percent_missing = (total_missing / len(df)) * 100

    missing_df = pd.DataFrame({
        'So luong thieu': total_missing,
        'Ty le thieu (%)': percent_missing.round(2)
    })
    print("\n=== THỐNG KÊ DỮ LIỆU THIẾU ===")
    print(missing_df)
    return missing_df

missing_report = missing_data(df)

data = pd.read_csv("rainfall.csv")
# Tính số lượng dữ liệu thiếu theo từng cột
missing_counts = data.isnull().sum()

plt.figure(figsize=(10, 5))
missing_counts.plot(kind='bar', color='skyblue')

plt.title('Số lượng giá trị khuyết trong tập dữ liệu')
plt.xlabel('Tên cột')
plt.ylabel('Số lượng giá trị khuyết')
plt.tight_layout()
plt.show()


def check_duplicates(df):
    # Số lượng dòng trùng lặp
    duplicated_count = df.duplicated().sum()
    print(f"\nSỐ LƯỢNG DỮ LIỆU TRÙNG LẶP: {duplicated_count}")

    # Lấy dữ liệu bị trùng (giữ tất cả bản trùng)
    duplicated_rows = df[df.duplicated(keep=False)]

    if duplicated_count > 0:
        print("\n=== CÁC DÒNG BỊ TRÙNG LẶP ===")
        print(duplicated_rows)
    else:
        print("\n✔ Không có dòng nào trùng lặp.")

    return duplicated_rows

check_duplicates(df)

# đếm các giá trị duy nhất trong một cột
def categories_counts(label_name):
    print('----------------------------------------------------')
    print(f'Số các giá trị duy nhất của cột "{label_name}":')
    print(df[label_name].value_counts())

categories_counts("location")
categories_counts("rain_category")
categories_counts("date")

df['date'] = (df['date'].dt.year - df['date'].dt.year.min()) * 12 + \
             (df['date'].dt.month - df['date'].dt.month.min())

# Chuyển tất cả các cột kiểu object sang mã số (category codes)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category').cat.codes

df.to_csv('rainfall3.csv', index=False)

print(df.head(10).to_string())

