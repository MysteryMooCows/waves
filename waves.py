import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def dists(xs, ys, point):
    return np.sqrt(((ys - point[1]) ** 2) + ((xs - point[0]) ** 2))

def presFunc(t, x):
    currX = t - x
    return amp(currX) * wavFunc(currX)

class Grid:
    def __init__(self, cols, rows):
        self.xx, self.yy = np.meshgrid(range(cols), range(rows))
        self.disturbances = []
        self.t = 1

    def disturb(self, x, y):
        self.disturbances.append(Disturbance(x, y))

    def currPreses(self):
        return np.sum(presFunc(self.t, dists(self.xx, self.yy, d.pos)) for d in self.disturbances)

class Disturbance:
    def __init__(self, x, y, wavFunc):
        self.pos = (x, y)
        self.wavFunc = wavFunc

g = Grid(200, 200)
g.disturb(100, 100)

fig = plt.figure()
im = plt.imshow(g.currPreses(), origin='lower', interpolation='none')

def updateFig(*args):
    g.t += 1 ## g.t += 1.05
    
    im.set_array(g.currPreses())
    return im,

ani = animation.FuncAnimation(fig, updateFig, interval=50, blit=True)

plt.show()
