import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. ĐỌC FILE GỐC (CHƯA MÃ HÓA)
# ==========================
df_raw = pd.read_csv("rainfall.csv")   # đổi tên file nếu cần
df_raw['location_code'] = df_raw['location'].astype('category').cat.codes

# Tạo map code -> tên tỉnh
location_map = dict(zip(df_raw['location_code'], df_raw['location']))

df = pd.read_csv("rainfall3.csv")

# Gắn lại tên tỉnh bằng map
df['location_name'] = df['location'].map(location_map)
# ==========================
# 3. GROUP VÀ PIVOT DỮ LIỆU CHO HEATMAP
# ==========================
df_group = df.groupby(['location_name', 'date'])['rain'].mean().reset_index()
df_pivot = df_group.pivot(index='location_name', columns='date', values='rain')

plt.figure(figsize=(8, 6))
sns.heatmap(
    df_pivot,
    cmap='YlGnBu',
    annot=True,     # <= hiện số
    fmt=".2f",      # <= định dạng số
    linewidths=0.5)

plt.title("Biểu đồ heatmap phân bố lượng mưa trung bình theo tháng và tỉnh", fontsize=16)
plt.xlabel("Tháng chuẩn hóa", fontsize=10)
plt.ylabel("Tên tỉnh", fontsize=10)
plt.tight_layout()
plt.show()