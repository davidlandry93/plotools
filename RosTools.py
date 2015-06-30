
import argparse
import numpy
import matplotlib.pyplot as plt
import rosbag

def errorsOfRosbag(topic, rosbag):
    dataset = []
    for topic, msg, t in rosbag.read_messages(topics=topic):
        dataset.append((t,msg.data[0],msg.data[1],msg.data[2]))

    time, errX, errY, errTheta = zip(*dataset)
    doubleTime = []
    for t in time:
        doubleTime.append(t.to_time())

    return (doubleTime, errX, errY, errTheta)

