import pandas as pd
import matplotlib.pyplot as plt
import os

# === Rutas de archivos ===
base_dir = r"E:\PUCP\Biomecatronica\Filtrado_senales"
raw_path = os.path.join(base_dir, "data", "raw_signals.csv")
filtered_path = os.path.join(base_dir, "results", "senales_filtradas.csv")
results_dir = os.path.join(base_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# === Cargar datos ===
raw = pd.read_csv(raw_path)
filtered = pd.read_csv(filtered_path)

# =============================
# VISUALIZACIÓN EEG
# =============================
plt.figure(figsize=(12, 6))
plt.plot(raw["time"], raw["eeg"], color="gray", alpha=0.6, label="EEG crudo (raw)")
plt.plot(filtered["Tiempo"], filtered["EEG_lowpass30Hz"], label="EEG LowPass 30Hz")
plt.plot(filtered["Tiempo"], filtered["EEG_band_alpha_8_12Hz"], label="EEG Banda Alfa (8-12Hz)")

plt.title("Señales EEG: Crudo vs Filtrados")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Guardar figura
eeg_plot_path = os.path.join(results_dir, "EEG_filtrado.png")
plt.savefig(eeg_plot_path, dpi=300)
print(f"✅ Gráfico EEG guardado en {eeg_plot_path}")

plt.show()

# =============================
# VISUALIZACIÓN ECG
# =============================
plt.figure(figsize=(12, 6))
plt.plot(raw["time"], raw["ecg"], color="gray", alpha=0.6, label="ECG crudo (raw)")
plt.plot(filtered["Tiempo"], filtered["ECG_band_0.5_40Hz"], label="ECG Banda 0.5–40Hz")

plt.title("Señales ECG: Crudo vs Filtrado")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Guardar figura
ecg_plot_path = os.path.join(results_dir, "ECG_filtrado.png")
plt.savefig(ecg_plot_path, dpi=300)
print(f"✅ Gráfico ECG guardado en {ecg_plot_path}")

plt.show()
