#!/usr/bin/env python

import argparse
import numpy
import matplotlib.pyplot as plt
import rosbag
import RosTools

parser = argparse.ArgumentParser(description='Plot the error values from a teach and repeat bag.')
parser.add_argument('bagfile', type=file, help='The name of the bag to parse')
ns = parser.parse_args()

bag = rosbag.Bag(ns.bagfile)

time, errX, errY, errTheta = RosTools.errorsOfRosbag('/teach_repeat/reported_error', bag)

plt.plot(time, errX)
plt.plot(time, errY)
plt.plot(time, errTheta)
plt.legend(["X","Y","Theta"], loc=0)
plt.show()

ns.bagfile.close()
