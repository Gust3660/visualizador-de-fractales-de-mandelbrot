# Visualizador de fractales de Mandelbrot

Aplicación Streamlit para explorar el conjunto de Mandelbrot con una vista configurable y descarga de la imagen generada.

## Funciones

- Ajusta el centro del plano complejo, el nivel de ampliación y las iteraciones.
- Cambia la resolución de la imagen.
- Calcula el tiempo de escape para cada píxel con NumPy.
- Descarga la visualización como PNG.

## Estructura

```text
.
├── backend.py       # Cálculo del fractal
├── frontend.py      # Controles, visualización y descarga
├── requirements.txt
└── README.md
```

## Instalación y ejecución

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run frontend.py
```

En macOS o Linux, activa el entorno con `source .venv/bin/activate`.

## Uso

Modifica las coordenadas del centro y la ampliación en la barra lateral. Aumentar la resolución o el máximo de iteraciones produce más detalle y puede tardar más.
