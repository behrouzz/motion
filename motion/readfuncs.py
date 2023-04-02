import numpy as np
from skimage import color
import matplotlib.pyplot as plt




def get_poly(x, y, n=9):
    coefs = np.polyfit(x, y, 9)
    f = np.poly1d(coefs)
    return f

def limx(im):
    mx = im.max(axis=1)
    mx = np.where(mx>0.7, 1, 0)
    i_x1 = np.where(mx>0)[0][0]
    i_x2 = np.where(mx>0)[0][-1]
    return im[i_x1:i_x2+1,:]

def limy(im):
    my = im.max(axis=0)
    my = np.where(my>0.7, 1, 0)
    i_y1 = np.where(my>0)[0][0]
    i_y2 = np.where(my>0)[0][-1]
    return im[:, i_y1:i_y2+1]


def read_func(file):
    im = plt.imread(file)
    im = color.rgb2gray(im).T
    im = im.max() - im
    im = limx(im)
    im = limy(im)
    im = np.where(im>0.7,1,0)
    im = np.flip(im, 1)

    x = np.arange(im.shape[0])
    y = np.zeros(len(x),)
    for i in range(im.shape[0]):
        y[i] = np.where(im[i]==im[i].max())[0][0]

    f = get_poly(x, y, n=9)
    return x, y, f
"""
x, y, f = read_func('../Scan/01.jpg')
xx = np.arange(len(x))
yy = f(xx)

fig, ax = plt.subplots()

ax.plot(x, y, c='b')
ax.plot(xx, yy, c='r')
plt.show()
"""
