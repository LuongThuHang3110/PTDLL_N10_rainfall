import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Đọc dữ liệu dataframe
df = pd.read_csv('rainfall1.csv')
def draw_pie_location(df):

    location_counts = df['location'].value_counts()

    plt.figure(figsize=(10, 6))
    plt.pie(
        location_counts,
        labels=location_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Tỷ lệ phân bố theo Location", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

draw_pie_location(df)