import numpy as np
import pandas as pd
import os

# Configuración
fs = 250  # frecuencia de muestreo (Hz)
t = np.linspace(0, 10, fs*10)  # 10 segundos

# ---- Señal EEG simulada ----
eeg = 50 * np.sin(2 * np.pi * 10 * t) + np.random.normal(0, 10, len(t))

# ---- Señal ECG simulada ----
ecg = 1000 * np.sin(2 * np.pi * 1.2 * t) + np.random.normal(0, 50, len(t))

# ---- Ruido de red 50 Hz ----
noise = 100 * np.sin(2 * np.pi * 50 * t)
eeg_noisy = eeg + noise
ecg_noisy = ecg + noise

# ---- Rutas seguras ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

output_file = os.path.join(DATA_DIR, "raw_signals.csv")

# Guardar datos
df = pd.DataFrame({"time": t, "eeg": eeg_noisy, "ecg": ecg_noisy})
df.to_csv(output_file, index=False)

print(f"✅ Señales crudas guardadas en {output_file}")
