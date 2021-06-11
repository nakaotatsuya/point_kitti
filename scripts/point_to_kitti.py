#!/usr/bin/env python
import rospy
import pypcd
from sensor_msgs.msg import PointCloud2
import numpy as np
import os

class PointToKitti(object):
    def __init__(self):
        self.sub = rospy.Subscriber("/sensing/lidar/top/rectified/pointcloud", PointCloud2, self.cb)
        #self.sub = rospy.Subscriber("/sensing/lidar/pointcloud", PointCloud2, self.cb)
        self.counter = 0 

        self.save_dir = "./normal"

    def cb(self,msg):
        pc = pypcd.PointCloud.from_msg(msg)
        x = pc.pc_data['x']
        y = pc.pc_data['y']
        z = pc.pc_data['z']
        intensity = pc.pc_data['intensity']
        #intensity /= 255.0
        #print(intensity[0:10])
        arr = np.zeros(x.shape[0] + y.shape[0] + z.shape[0] + intensity.shape[0], dtype=np.float32)
        print(arr.shape)
        arr[::4] = x - 0.901
        arr[1::4] = y
        arr[2::4] = z - 2.066
        arr[3::4] = intensity / 255.0

        #print(arr[0:10])
        #print(arr[3])

        #higher cut
        #arr = arr.reshape((-1,4))
        # print(arr.shape)
        #arrr = np.delete(arr, np.where(arr[:,2] > 3.0)[0], 0)
        # print(arrr.shape)
        #b = arrr.flatten()
        #print(b.shape)
        #print(z.shape)
        
        print("-------------------")

        zero = "{0:03d}".format(self.counter)
        bin_file = os.path.join(self.save_dir , zero+".bin")
        arr.astype('float32').tofile(bin_file)
        #b.astype('float32').tofile(bin_file)
        self.counter += 1

if __name__ == "__main__":
    rospy.init_node("point_to_kitti")
    ptk = PointToKitti()
    rospy.spin()
    
    
        
        
        
