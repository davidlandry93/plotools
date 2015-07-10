#!/usr/bin/env python

import argparse
import numpy
import matplotlib.pyplot as plt
import rosbag
import RosTools

parser = argparse.ArgumentParser(description='Plot the error values from a teach and repeat bag.')
parser.add_argument('bagfile1', type=file, help='The name of the bag to parse')
parser.add_argument('bagfile2', type=file, help='The name of the bag to parse')
ns = parser.parse_args()

bag1 = rosbag.Bag(ns.bagfile1)
bag2 = rosbag.Bag(ns.bagfile2)

time1, errX1, errY1, errTheta1 = RosTools.errorsOfRosbag('/teach_repeat/reported_error', bag1)
time2, errX2, errY2, errTheta2 = RosTools.errorsOfRosbag('/teach_repeat/reported_error', bag2)

f, subplots = plt.subplots(3, sharex=True)
subplots[0].plot(time1, errX1)
subplots[0].plot(time2, errX2)
subplots[0].set_title('Erreur en X')

subplots[1].plot(time1, errY1)
subplots[1].plot(time2, errY2)
subplots[1].set_title('Erreur en Y')

subplots[2].plot(time1, errTheta1)
subplots[2].plot(time2, errTheta2)
subplots[2].set_title('Erreur en Theta')

plt.show()

ns.bagfile1.close()
ns.bagfile2.close()
