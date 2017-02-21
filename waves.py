import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def dists(xs, ys, point):
    return np.sqrt(((ys - point[1]) ** 2) + ((xs - point[0]) ** 2))

class Grid:
    def __init__(self, cols, rows):
        self.xx, self.yy = np.meshgrid(range(cols), range(rows))
        disturbances = []
        self.t = 1

    def currPreses(self):
        return np.sum(d.wavFunc(self.t, dists(self.xx, self.yy, d.pos)) for d in disturbances)

class Disturbance:
    def __init__(self, x, y, wavFunc):
        self.pos = (x, y)
        self.wavFunc = wavFunc

disturbances = []

g = Grid(200, 200)

disturbances.append(Disturbance(100, 100, (lambda t, x: np.sin(t - x))))

fig = plt.figure()
im = plt.imshow(g.currPreses(), origin='lower', interpolation='none')

def updateFig(*args):
    g.t += 1 ## g.t += 1.05
    
    im.set_array(g.currPreses())
    return im,

ani = animation.FuncAnimation(fig, updateFig, interval=50, blit=True)

plt.show()
