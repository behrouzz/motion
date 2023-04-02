import numpy as np
import matplotlib.pyplot as plt
from .animation import play2d
from .readfuncs import read_func

g = 9.81


def inverse(x, y, n=None):
    if n is None:
        n = len(x)//10
    coefs = np.polyfit(x, y, 9)
    f = np.poly1d(coefs)
    new_x = np.linspace(x[0], x[-1], n)
    new_y = f(new_x)
    return new_x, new_y


def get_a(f, x):
    slopes = f.deriv()(x)

    ang = -np.arctan(slopes)
    
    ay = g * (np.sin(ang)**2)
    ax = g * np.cos(ang) * np.sin(ang)
    return ax,ay


def basics(func, n=None):
    x = np.linspace(1, 2, n)
    y = func(x)
    coefs = np.polyfit(x, y, 9)
    f = np.poly1d(coefs)

    slopes = f.deriv()(x)

    ang = -np.arctan(slopes)
    
    ay = g * (np.sin(ang)**2)
    ax = g * np.cos(ang) * np.sin(ang)
    return x,y,f,ax,ay


def core(x,y,f,ax,ay, n=None):
    dx = x[1]-x[0]
    vx = 0
    velx = [vx]

    for i in range(len(x)):
        vx = (2*ax[i]*dx + (vx**2)) ** 0.5
        velx.append(vx)
    velx = np.array(velx)

    dvx = velx[1:]-velx[:-1]
    dt = dvx/ax
    t = np.cumsum(dt)
    tt, x_t = inverse(t, x, n)
    y_t = f(x_t)
    
    return tt, x_t, y_t


class Simulation:
    def __init__(self, func=None, file=None):
        #self.g = 9.81
        self.func = func
        self.file = file
        if self.func is not None:
            self.file = None
        if (self.func is None) and (self.file is None):
            raise Exception('func OR file are needed!')

    def run(self):
        if self.func is None:
            self.x, self.y, self.f = read_func(self.file)
            self.ax, self.ay = get_a(self.f, self.x)
        else:
            self.x, self.y, self.f, self.ax, self.ay =\
                    basics(self.func, n=200)
        self.t, self.x_t, self.y_t =\
                core(self.x, self.y, self.f, self.ax, self.ay, n=200)

    def play(self):
        anim = play2d(self.x_t, self.y_t)
        plt.show()

