#!/usr/bin/env python


def absTimeToSimTime(time_list):
    t0 = time_list[0]
    f = lambda x: (x-t0).to_sec()
    return map(f, time_list)


def errorsOfRosbag(topic, bag):
    dataset = []
    for topic, msg, t in bag.read_messages(topics=topic):
        dataset.append((t, msg.data[0], msg.data[1], msg.data[2]))

    time, errX, errY, errTheta = zip(*dataset)

    return (absTimeToSimTime(time), errX, errY, errTheta)


def twistDataOfTopic(topic, bag):
    dataset = []
    for topic, msg, t in bag.read_messages(topics=topic):
        dataset.append((t, msg.linear.x, msg.angular.z))

    time, linearSpeed, angularSpeed = zip(*dataset)

    return (absTimeToSimTime(time), linearSpeed, angularSpeed)


def encodersDataOfTopic(topic, bag):
    dataset = []
    for topic, msg, t in bag.read_messages(topics=topic):
        dataset.append((t, msg.encoders[0].travel, msg.encoders[1].travel))

    time, travel1, travel2 = zip(*dataset)

    return (absTimeToSimTime(time), travel1, travel2)


def posesOfTopic(topic, bag):
    dataset = []
    for topic, msg, t in bag.read_messages(topics=topic):
        dataset.append((t, msg.pose.pose.position.x, msg.pose.pose.position.y))

    time, x, y = zip(*dataset)

    return (absTimeToSimTime(time), (x, y))
