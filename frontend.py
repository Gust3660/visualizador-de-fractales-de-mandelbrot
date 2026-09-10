"""Interfaz Streamlit para explorar el conjunto de Mandelbrot."""

from __future__ import annotations

from io import BytesIO

import matplotlib.pyplot as plt
import streamlit as st

from backend import mandelbrot


st.set_page_config(page_title="Fractal de Mandelbrot", page_icon="🌀", layout="wide")
st.title("Visualizador de fractales de Mandelbrot")
st.write("Ajusta el centro, la ampliación y la resolución para explorar el conjunto de Mandelbrot.")

with st.sidebar:
    st.header("Vista")
    center_x = st.number_input("Centro real", min_value=-2.0, max_value=1.0, value=-0.5, step=0.05)
    center_y = st.number_input("Centro imaginario", min_value=-1.5, max_value=1.5, value=0.0, step=0.05)
    zoom = st.slider("Ampliación", min_value=1, max_value=100, value=1)
    width = st.select_slider("Ancho", options=[400, 600, 800, 1000, 1200], value=800)
    max_iterations = st.slider("Iteraciones máximas", min_value=30, max_value=500, value=120, step=10)

base_width = 3.2 / zoom
base_height = 2.8 / zoom
x_min, x_max = center_x - base_width / 2, center_x + base_width / 2
y_min, y_max = center_y - base_height / 2, center_y + base_height / 2
height = int(width * base_height / base_width)
escape = mandelbrot(width, height, max_iterations, x_min, x_max, y_min, y_max)

fig, axis = plt.subplots(figsize=(12, 7))
image = axis.imshow(
    escape,
    extent=[x_min, x_max, y_min, y_max],
    origin="lower",
    cmap="magma",
    interpolation="nearest",
)
axis.set_xlabel("Parte real")
axis.set_ylabel("Parte imaginaria")
axis.set_title(f"Conjunto de Mandelbrot · {width} × {height} · {max_iterations} iteraciones")
fig.colorbar(image, ax=axis, label="Iteraciones de escape")
fig.tight_layout()
st.pyplot(fig, use_container_width=True)
buffer = BytesIO()
fig.savefig(buffer, format="png", dpi=160, bbox_inches="tight")
st.download_button("Descargar imagen PNG", buffer.getvalue(), "mandelbrot.png", "image/png")
plt.close(fig)
st.caption("Los puntos que no escapan antes del límite de iteraciones se muestran dentro del conjunto.")
