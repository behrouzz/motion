import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D, proj3d


def play2d(x, y, path=True, legend=True, interval=20, repeat=True):


    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_title('HICHI')
    lines = []

    alpha = 0.2

    ax.plot(x, y, alpha=alpha)
    lines.append(ax.plot(x, y, marker='o')[0])

    def init():
        for line in lines:
            line.set_xdata(np.array([]))
            line.set_ydata(np.array([]))
        return lines

    def animate(i):
        for j,line in enumerate(lines):
            line.set_xdata(x[i])
            line.set_ydata(y[i])
        return lines

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=len(x), interval=interval,
                         blit=True, repeat=repeat)
    return anim
