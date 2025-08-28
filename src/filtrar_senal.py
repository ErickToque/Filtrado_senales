import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt
import os

# === Función de filtrado ===
def butter_filter(data, cutoff, fs, btype, order=4):
    """
    Aplica un filtro Butterworth.
    data: señal (array)
    cutoff: frecuencia(s) de corte (Hz)
    fs: frecuencia de muestreo
    btype: 'low', 'high', 'band'
    order: orden del filtro
    """
    nyq = 0.5 * fs
    if isinstance(cutoff, (list, tuple)):
        normal_cutoff = [c / nyq for c in cutoff]
    else:
        normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return filtfilt(b, a, data)

if __name__ == "__main__":
    # Parámetros
    fs = 250  # Hz (misma frecuencia que en generar_datos.py)

    # --- Rutas absolutas ---
    base_dir = r"E:\PUCP\Biomecatronica\Filtrado_senales"
    data_dir = os.path.join(base_dir, "data")
    results_dir = os.path.join(base_dir, "results")
    os.makedirs(results_dir, exist_ok=True)

    # Leer datos crudos
    raw_file = os.path.join(data_dir, "raw_signals.csv")
    df_raw = pd.read_csv(raw_file)

    t = df_raw["time"].values
    eeg_raw = df_raw["eeg"].values
    ecg_raw = df_raw["ecg"].values

    # Aplicar filtros
    eeg_low = butter_filter(eeg_raw, cutoff=30, fs=fs, btype='low')
    eeg_band = butter_filter(eeg_raw, cutoff=(8, 12), fs=fs, btype='band')  # Banda alfa
    ecg_band = butter_filter(ecg_raw, cutoff=(0.5, 40), fs=fs, btype='band')  # ECG típico

    # Guardar resultados
    save_path = os.path.join(results_dir, "senales_filtradas.csv")
    df_out = pd.DataFrame({
        "Tiempo": t,
        "EEG_crudo": eeg_raw,
        "EEG_lowpass30Hz": eeg_low,
        "EEG_band_alpha_8_12Hz": eeg_band,
        "ECG_crudo": ecg_raw,
        "ECG_band_0.5_40Hz": ecg_band
    })
    df_out.to_csv(save_path, index=False)

    print(f"✅ Señales filtradas guardadas en {save_path}")
