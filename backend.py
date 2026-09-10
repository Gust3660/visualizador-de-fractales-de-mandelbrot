"""Cálculo vectorizado del conjunto de Mandelbrot."""

from __future__ import annotations

import numpy as np


def mandelbrot(
    width: int = 800,
    height: int = 500,
    max_iterations: int = 120,
    x_min: float = -2.2,
    x_max: float = 1.0,
    y_min: float = -1.4,
    y_max: float = 1.4,
) -> np.ndarray:
    """Devuelve la iteración de escape para cada punto del plano complejo."""
    if width < 50 or height < 50:
        raise ValueError("El ancho y alto deben ser de al menos 50 píxeles.")
    if max_iterations < 1:
        raise ValueError("Se requiere al menos una iteración.")
    if not x_min < x_max or not y_min < y_max:
        raise ValueError("Los límites de los ejes no son válidos.")

    real = np.linspace(x_min, x_max, width)
    imaginary = np.linspace(y_min, y_max, height)
    c = real[np.newaxis, :] + 1j * imaginary[:, np.newaxis]
    z = np.zeros(c.shape, dtype=np.complex128)
    escape = np.zeros(c.shape, dtype=np.int32)
    active = np.ones(c.shape, dtype=bool)
    for iteration in range(1, max_iterations + 1):
        z[active] = z[active] ** 2 + c[active]
        escaped_now = active & (np.abs(z) > 2)
        escape[escaped_now] = iteration
        active[escaped_now] = False
        if not np.any(active):
            break
    escape[active] = max_iterations
    return escape
