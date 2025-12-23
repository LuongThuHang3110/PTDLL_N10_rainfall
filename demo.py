import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import joblib

# ======================
# LOAD METRICS
# ======================
try:
    metrics = joblib.load("metrics.pkl")
    RMSE = round(metrics.get("rmse", 0), 3)
    R2 = round(metrics.get("r2_test", 0), 3)
except:
    RMSE = "N/A"
    R2 = "N/A"

# ======================
# WINDOW
# ======================
root = tk.Tk()
root.title("🌧 Dự báo lượng mưa")
root.geometry("800x560")
root.configure(bg="#f1f5f9")

# ======================
# STYLE
# ======================
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=8)
style.configure("TEntry", font=("Segoe UI", 11), padding=5)
style.configure("TCombobox", font=("Segoe UI", 11), padding=5)
style.configure("TLabelframe.Label", font=("Segoe UI", 12, "bold"))

# ======================
# MAIN FRAME
# ======================
main = tk.Frame(root, bg="white", padx=20, pady=15)
main.pack(fill="both", expand=True, padx=15, pady=15)

# ======================
# TITLE
# ======================
tk.Label(
    main,
    text="🌧 HỆ THỐNG DỰ BÁO LƯỢNG MƯA",
    font=("Segoe UI", 22, "bold"),
    fg="#1e4f91",
    bg="white"
).pack(pady=(0, 12))

# ======================
# TIME FRAME
# ======================
time_frame = tk.LabelFrame(
    main, text="📅 Thời gian",
    bg="white", fg="#1e4f91",
    padx=10, pady=6
)
time_frame.pack(fill="x", pady=6)

tk.Label(time_frame, text="Ngày:", bg="white", font=("Segoe UI", 11)).grid(row=0, column=0)
tk.Label(time_frame, text="Tháng:", bg="white", font=("Segoe UI", 11)).grid(row=0, column=2)
tk.Label(time_frame, text="Năm:", bg="white", font=("Segoe UI", 11)).grid(row=0, column=4)

day_cb = ttk.Combobox(time_frame, width=5, values=[f"{i:02d}" for i in range(1, 32)])
month_cb = ttk.Combobox(time_frame, width=5, values=[f"{i:02d}" for i in range(1, 13)])
year_cb = ttk.Combobox(time_frame, width=8, values=[str(i) for i in range(2020, 2031)])

today = datetime.now()
day_cb.set(today.strftime("%d"))
month_cb.set(today.strftime("%m"))
year_cb.set(today.strftime("%Y"))

day_cb.grid(row=0, column=1, padx=6)
month_cb.grid(row=0, column=3, padx=6)
year_cb.grid(row=0, column=5, padx=6)

# ======================
# WEATHER INFO FRAME
# ======================
info = tk.LabelFrame(
    main, text="🌍 Thông tin thời tiết",
    bg="white", fg="#1e4f91",
    padx=10, pady=8
)
info.pack(fill="x", pady=6)
info.columnconfigure(1, weight=1)

def create_row(label, widget, r):
    tk.Label(
        info,
        text=label,
        bg="white",
        font=("Segoe UI", 11),
        width=18,
        anchor="w"
    ).grid(row=r, column=0, pady=4)
    widget.grid(row=r, column=1, sticky="ew", pady=4)

location_cb = ttk.Combobox(
    info,
    values=["Hà Nội", "Đà Nẵng", "Huế", "TP.HCM", "Cần Thơ"],
    state="readonly"
)
location_cb.set("Hà Nội")

temp_e = ttk.Entry(info)
hum_e = ttk.Entry(info)
wind_e = ttk.Entry(info)
pres_e = ttk.Entry(info)

create_row("Khu vực:", location_cb, 0)
create_row("Nhiệt độ (°C):", temp_e, 1)
create_row("Độ ẩm (%):", hum_e, 2)
create_row("Gió (km/h):", wind_e, 3)
create_row("Áp suất (hPa):", pres_e, 4)

# ======================
# PREDICT FUNCTION
# ======================
def predict():
    try:
        t = float(temp_e.get())
        h = float(hum_e.get())
        w = float(wind_e.get())
        p = float(pres_e.get())

        rainfall = max(0, round(h * 0.4 + w * 0.3 - t * 0.2 + (1013 - p) * 0.01, 2))

        if rainfall >= 50:
            rain_type = "🌧 Mưa lớn"
        elif rainfall >= 20:
            rain_type = "🌦 Mưa vừa"
        else:
            rain_type = "🌤 Mưa nhỏ"

        result.set(
            f"{rain_type}\n"
            f"Lượng mưa: {rainfall} mm\n\n"
            f"📊 RMSE: {RMSE}     R²: {R2}"
        )

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ và đúng định dạng số!")

# ======================
# BUTTON
# ======================
ttk.Button(
    main,
    text="🌧 DỰ BÁO",
    command=predict
).pack(pady=10)

# ======================
# RESULT FRAME
# ======================
res_frame = tk.LabelFrame(
    main, text="📊 Kết quả & đánh giá",
    bg="white", fg="#1e4f91",
    padx=10, pady=10
)
res_frame.pack(fill="x", pady=6)

result = tk.StringVar()
tk.Label(
    res_frame,
    textvariable=result,
    font=("Segoe UI", 14, "bold"),
    fg="#0b4f8a",
    bg="white",
    justify="left"
).pack(anchor="w")

# ======================
root.mainloop()
