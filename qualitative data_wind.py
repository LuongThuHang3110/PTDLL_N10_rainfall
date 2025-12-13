import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Đọc dữ liệu dataframe
df = pd.read_csv('rainfall1.csv')
def draw_wind_pie(df):

    wind = df['wind']


    bins = [0, 10, 20, 30, 100]
    labels = ['0–10 km/h', '10–20 km/h', '20–30 km/h', '>30 km/h']

    wind_groups = pd.cut(wind, bins=bins, labels=labels, include_lowest=True)

    # Tính phần trăm từng nhóm
    counts = wind_groups.value_counts()

    # Vẽ biểu đồ tròn
    plt.figure(figsize=(7,7))
    plt.pie(
        counts.values,
        labels=counts.index,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Phân phối tốc độ gió (wind)", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

draw_wind_pie(df)