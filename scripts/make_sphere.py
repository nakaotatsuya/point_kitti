#!/usr/bin/env python
import rospy
import pypcd
from sensor_msgs.msg import PointCloud2
import numpy as np
import os

class Sphere(object):
    def __init__(self):
        x = np.array([3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4])
        y = np.array([0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5])
        z = np.array([0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1])
        intensity = np.array([255,19,255,120,255,255,255,64,12])
        self.counter = 0
        self.save_dir = "./sphere"

        arr = np.zeros(x.shape[0] + y.shape[0] + z.shape[0] + intensity.shape[0], dtype=np.float32)
        arr[::4] = x
        arr[1::4] = y
        arr[2::4] = z
        arr[3::4] = intensity / 255.0
        zero = "{0:03d}".format(self.counter)
        bin_file = os.path.join(self.save_dir, zero+".bin")
        arr.astype("float32").tofile(bin_file)

if __name__ == "__main__":
    sphere = Sphere()
