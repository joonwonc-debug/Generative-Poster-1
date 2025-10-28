# app.py
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Generative Poster", layout="centered")

def random_palette(k=5):
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    angles = np.linspace(0, 2 * math.pi, points)
    radii = r * (1 + wobble * (np.random.rand(points) - 0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

st.title("🎨 Generative Poster")
st.caption("Week 2 • Arts & Advanced Big Data")

# optional UI controls
n_layers = st.slider("Number of layers", 3, 15, 8)
wobble_range = st.slider("Wobble intensity", 0.05, 0.4, 0.15)
random.seed()

# generate art
fig, ax = plt.subplots(figsize=(7, 10))
ax.axis("off")
ax.set_facecolor((0.98, 0.98, 0.97))

palette = random_palette(6)
for i in range(n_layers):
    cx, cy = random.random(), random.random()
    rr = random.uniform(0.15, 0.45)
    x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05, wobble_range))
    color = random.choice(palette)
    alpha = random.uniform(0.25, 0.6)
    ax.fill(x, y, color=color, alpha=alpha, edgecolor=(0, 0, 0, 0))

plt.xlim(0, 1)
plt.ylim(0, 1)

st.pyplot(fig)
