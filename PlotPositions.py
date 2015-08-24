#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import rosbag

import trutil

parser = argparse.ArgumentParser(
    description='Plot the speeds in a husky rosbag')
parser.add_argument('bagfile', type=open, help='The name of the bag to parse')
parser.add_argument('bagfile2', type=open, help='The name of the bag to parse')
ns = parser.parse_args()

bag1 = rosbag.Bag(ns.bagfile)
bag2 = rosbag.Bag(ns.bagfile2)

time, position = trutil.posesOfTopic('/robot_pose_ekf/odom_combined', bag1)
time2, position2 = trutil.posesOfTopic('/robot_pose_ekf/odom_combined', bag2)

plt.plot(position[0][0], position[1][0], 'ro', label='begin')
plt.plot(position2[0][0], position2[1][0], 'bo', label='begin')
plt.plot(position[0], position[1], 'r-', label='first')
plt.plot(position2[0], position2[1], 'b-', label='second')
plt.legend()
plt.show()

ns.bagfile.close()
