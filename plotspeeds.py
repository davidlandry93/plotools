#!/usr/bin/env python 

import argparse
import matplotlib.pyplot as plt
import numpy as np
import rosbag

import trutil

parser = argparse.ArgumentParser(
        description='Plot the speeds in a husky rosbag'
        )
parser.add_argument('bagfile', type=file, help='The name of the bag to parse')
ns = parser.parse_args()

bag = rosbag.Bag(ns.bagfile)

commandTime, commandLinear, commandAngular = trutil.twistDataOfTopic(
        '/husky/cmd_vel', bag
        )

encoderTime, encoder1, encoder2 = trutil.encodersDataOfTopic(
        '/husky/data/encoders', bag
        )

finiteDiff = np.diff(encoder1, n=1)
encoderSpeed = []
for i in range(0, len(encoderTime) - 1):
    encoderSpeed.append(finiteDiff[i] / (encoderTime[i+1] - encoderTime[i]))

plt.plot(commandTime, commandLinear)
#plt.plot(encoderTime, encoder2)
plt.plot(encoderTime[:-1], encoderSpeed)
plt.show()

ns.bagfile.close()
