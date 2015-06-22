#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import rosbag

parser = argparse.ArgumentParser(description='Plot the error values from a teach and repeat bag.')
parser.add_argument('bagfile', type=file, help='The name of the bag to parse')
ns = parser.parse_args()

bag = rosbag.Bag(ns.bagfile)
dataset = []
for topic, msg, t in bag.read_messages(topics=['/teach_repeat/reported_error']):
    dataset.append((t,msg.data[0], msg.data[1], msg.data[2]))

time, errX, errY, errTheta = zip(*dataset)

doubleTime = []
for t in time:
    doubleTime.append(t.to_time())

plt.plot(doubleTime, errX)
plt.plot(doubleTime, errY)
plt.plot(doubleTime, errTheta)
plt.legend(["X","Y","Theta"], loc=0)
plt.show()

ns.bagfile.close()
