# Proyecto de Filtrado de Señales (EEG/ECG)

Este proyecto tiene como objetivo **procesar y visualizar señales biomédicas** (como EEG o ECG) mediante filtrado digital.  
Se trabaja con datos en crudo (`raw_signals.csv`) y se generan señales filtradas almacenadas en `senales_filtradas.csv`.

---

## 📂 Estructura del Proyecto

E:\PUCP\Biomecatronica\Filtrado_senales
│
├── data
│ └── raw_signals.csv # Datos crudos (señales sin filtrar)
│
├── results
│ └── senales_filtradas.csv # Señales filtradas y exportadas
│
├── src
│ ├── filtrar_senal.py # Script para aplicar filtros digitales
│ └── visualizar_senal.py # Script para graficar señales (raw y filtradas)
│
└── README.md

yaml
Copiar código

---

## 🚀 Uso del Proyecto

1. Coloca tus señales crudas en `data/raw_signals.csv`.
   - El archivo debe tener al menos dos columnas:  
     - `time` → tiempo o muestras.  
     - `signal` → valores de la señal.  

2. Ejecuta el script de **filtrado**:
   ```bash
   python src/filtrar_senal.py
Esto generará el archivo results/senales_filtradas.csv.

Ejecuta el script de visualización:

bash
Copiar código
python src/visualizar_senal.py
Se mostrarán gráficos comparativos entre la señal original y la filtrada.

📊 Métodos de Filtrado
Actualmente el proyecto implementa:

Filtro Pasa-Banda Butterworth (ejemplo: 0.5 – 40 Hz, configurable).
Este rango es típico para señales EEG o ECG, pero puede ajustarse según la aplicación.

✅ Requisitos
Python 3.8+

Librerías necesarias:

bash
Copiar código
pip install numpy pandas scipy matplotlib
📌 Futuras Mejoras
Implementar diferentes tipos de filtros (Notch, FIR, Wavelets).

Incorporar análisis de características (ej. energía, frecuencia dominante).

Generar una interfaz gráfica básica.
