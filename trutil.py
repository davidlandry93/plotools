
import argparse
import numpy
import matplotlib.pyplot as plt
import rosbag


def absTimeToSimTime(time_list):
    t0 = time_list[0]
    f = lambda x: (x-t0).to_sec()
    return map(f, time_list)

def errorsOfRosbag(topic, rosbag):
    dataset = []
    for topic, msg, t in rosbag.read_messages(topics=topic):
        dataset.append((t,msg.data[0],msg.data[1],msg.data[2]))

    time, errX, errY, errTheta = zip(*dataset)

    return (absTimeToSimTime(time), errX, errY, errTheta)

def twistDataOfTopic(topic, rosbag):
    dataset = []
    for topic, msg, t in rosbag.read_messages(topics=topic):
        dataset.append((t, msg.linear.x, msg.angular.z))

    time, linearSpeed, angularSpeed = zip(*dataset)

    return (absTimeToSimTime(time), linearSpeed, angularSpeed)

def encodersDataOfTopic(topic, rosbag):
    dataset = []
    for topic, msg, t in rosbag.read_messages(topics=topic):
        dataset.append((t, msg.encoders[0].travel, msg.encoders[1].travel))

    time, travel1, travel2 = zip(*dataset)

    return (absTimeToSimTime(time), travel1, travel2)
