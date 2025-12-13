import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("rainfall3.csv")

# Chọn các cột số
corr_cols = ['rain', 'temp', 'humidity', 'wind', 'pressure']

corr_matrix = df[corr_cols].corr()
plt.figure(figsize=(9, 7))

sns.set_theme(style="white")
heatmap = sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    vmin=-1, vmax=1,
    linewidths=0.6,
    linecolor='white',
    annot_kws={"size": 12, "weight": "bold", "color": "black"},
    cbar_kws={
        "shrink": 0.8,
        "aspect": 20,
        "label": "Hệ số tương quan (r)"
    }
)

plt.title("Ma trận tương quan giữa các biến thời tiết", fontsize=18,weight='bold',pad=20)
plt.xticks(fontsize=12, rotation=15)
plt.yticks(fontsize=12, rotation=0)
# Làm bo trục cho đẹp
for _, spine in plt.gca().spines.items():
    spine.set_visible(True)
    spine.set_color("#cccccc")
plt.tight_layout()
plt.show()