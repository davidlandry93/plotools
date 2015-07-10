#!/usr/bin/env python3

import argparse
import RosTools
import rosbag

parser = argparse.ArgumentParser(
        description='Plot the speeds in a husky rosbag'
        )
parser.add_argument('bagfile', type=file, help='The name of the bag to parse')
ns = parser.parse_args()
