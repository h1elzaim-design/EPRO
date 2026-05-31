import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

def compute(xmin, xmax, ymin, ymax, nx=800, ny=800, upperlim=200):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymin, ymax, ny)
    C = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    Z = np.zeros_like(C)
    F = np.full(C.shape, float(upperlim))
    mask = np.ones(C.shape, dtype=bool)
    for n in range(upperlim):
        Z[mask] = Z[mask] ** 2 + C[mask]
        escaped = mask & (np.abs(Z) > 2)
        F[escaped] = n
        mask[escaped] = False
    return x, y, F

RESET = (-2.0, 0.5, -1.25, 1.25)
state = list(RESET)

fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_facecolor('#111')
ax.set_facecolor('#111')

def redraw():
    xmin, xmax, ymin, ymax = state
    ax.cla()
    ax.set_facecolor('#111')
    x, y, F = compute(xmin, xmax, ymin, ymax)
    X, Y = np.meshgrid(x, y)
    ax.pcolormesh(X, Y, F, cmap='inferno', shading='auto')
    ax.set_title(
        f'x:[{xmin:.6f}, {xmax:.6f}]  y:[{ymin:.6f}, {ymax:.6f}]\n'
        'Rechteck ziehen = Zoom  |  Rechtsklick = Zurück',
        color='white', fontsize=9
    )
    ax.set_xlabel('Re', color='white')
    ax.set_ylabel('Im', color='white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    fig.canvas.draw()
    attach_selector()

def on_select(eclick, erelease):
    x1 = min(eclick.xdata, erelease.xdata)
    x2 = max(eclick.xdata, erelease.xdata)
    y1 = min(eclick.ydata, erelease.ydata)
    y2 = max(eclick.ydata, erelease.ydata)
    if x2 - x1 < 1e-10 or y2 - y1 < 1e-10:
        return
    state[:] = [x1, x2, y1, y2]
    redraw()

def on_click(event):
    if event.button == 3:
        state[:] = list(RESET)
        redraw()

def attach_selector():
    global selector
    selector = RectangleSelector(
        ax, on_select,
        useblit=True, button=[1],
        minspanx=5, minspany=5,
        spancoords='pixels',
        props=dict(edgecolor='white', fill=False, linewidth=1.5)
    )

redraw()
fig.canvas.mpl_connect('button_press_event', on_click)
plt.tight_layout()
plt.show()
