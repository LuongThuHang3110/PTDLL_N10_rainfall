import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("rainfall3.csv")
def draw_rain_by_month(df):

    # Chuyển rain sang dạng số
    df['rain'] = pd.to_numeric(df['rain'], errors='coerce')

    # Chuyển cột date sang số (0–13)
    df['date'] = pd.to_numeric(df['date'], errors='coerce')

    # Đổi tên cột để dễ hiểu
    df = df.rename(columns={'date': 'Month'})

    # Nhóm theo tháng 0–13 → tính lượng mưa trung bình
    rainfall_by_month = df.groupby('Month')['rain'].mean().reset_index()

    # Vẽ biểu đồ
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x='Month',
        y='rain',
        data=rainfall_by_month,
        palette="GnBu",
        hue='Month',
        legend=False
    )

    plt.title("Lượng mưa trung bình theo tháng (0–13)", fontsize=14)
    plt.xlabel("Tháng (0–13)", fontsize=12)
    plt.ylabel("Lượng mưa trung bình (mm)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


draw_rain_by_month(df)