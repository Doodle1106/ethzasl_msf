import rospy
from geometry_msgs.msg import TransformStamped

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def draw(file, color):
    f1 = open(file).readlines()
    x = []
    y = []
    z = []

    for line in f1:
        r = line.split()[1:]
        x.append(float(r[0].split(',')[0]))
        y.append(float(r[1].split(',')[0]))
        z.append(float(r[2].split(',')[0]))
        # print(x,y,z)



    ax.scatter(x, y, z, color=color)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

draw("/home/gishr/software/msf/results.log", 'r')
draw("/home/gishr/software/msf/results2.log", 'y')

plt.show()
