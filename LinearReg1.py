import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("rainfall3.csv")

columns = ['date', 'location', 'temp', 'humidity', 'wind', 'pressure', 'rain_category']

# Tạo figure 2 × 4
plt.figure(figsize=(15, 13))

for i, col in enumerate(columns, 1):
    plt.subplot(2, 4, i)
    sns.scatterplot(
        data=df,
        x=col,
        y='rain',
        s=15,  # điểm nhỏ giống hình
        alpha=0.6,  # độ mờ tương tự
        color='#1f77b4'  # màu xanh giống hình mẫu
    )
    plt.title(f"Relationship between {col} and Rainfall (rain)", fontsize=6)
    plt.xlabel(col)
    plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.show()
