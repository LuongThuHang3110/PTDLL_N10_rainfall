import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Đọc dữ liệu dataframe
df = pd.read_csv('rainfall1.csv')


def draw_box_plot(df):
    df_num = df.select_dtypes(include='number')

    plt.figure(figsize=(12, 6))

    plt.boxplot(df_num.values, patch_artist=True)

    plt.xlabel("Cột số", fontsize=12)
    plt.ylabel("Giá trị", fontsize=12)
    plt.title("Boxplot của các cột định lượng", fontsize=14, fontweight='bold')

    plt.grid(linestyle='solid', linewidth=0.4)
    plt.tight_layout()
    plt.show()

draw_box_plot(df)