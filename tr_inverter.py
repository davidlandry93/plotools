
import string
import os
import shutil
import argparse

def copy_anchor_points(inputDir, outputDir):
    apList = filter(lambda x: x.endswith(".vtk"), os.listdir(inputDir))

    for ap in apList:
        shutil.copy(os.path.join(inputDir, ap), os.path.join(outputDir, ap))    

def convert_anchor_point_file(filename, outputFile):
    f = open(filename, 'r')
    
    anchorPoints = []
    for line in f:
        anchorPoints.append(line)

    of = open(outputFile, 'w')
    for anchorPoint in reversed(anchorPoints):
        of.write(anchorPoint)

    f.close()
    of.close()

def convert_position_file(filename, outputFile):
    f = open(filename, 'r')
    
    positions = []
    for line in f:
        splitString = string.split(line, ',')
        splitString = map(float, splitString)
        positions.append(tuple(splitString))

    lastTime = positions[-1][0]
    invertedPositions = map(
            lambda x: (-1*(x[0] - lastTime), x[1], x[2], x[3], x[4], x[5], x[6], x[7]), 
            reversed(positions)
        )

    of = open(outputFile, 'w')
    for pos in invertedPositions:
        for value in pos[0:-1]:
            of.write(repr(value) + ',')
        of.write(repr(pos[-1]) + '\n')

    of.close()
    f.close()
    return lastTime

def convert_speed_file(filename, outputFile, lastTime):
    f = open(filename, 'r')
    
    invertedSpeeds = []
    for line in f:
        splitString = string.split(line, ',')
        splitString = map(float, splitString)
        invertedSpeeds.append(tuple(splitString))

    invertedSpeeds = map(
            lambda x: (-1*(x[0]-lastTime), -1*x[1], -1*x[2]), 
            reversed(invertedSpeeds)
        )

    of = open(outputFile, 'w')
    for command in invertedSpeeds:
        of.write(
                repr(command[0]) + ',' + 
                repr(command[1]) + ',' + 
                repr(command[2]) + '\n' 
            )

    of.close()
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="""Outputs a reversed version of the teach in another 
                            folder."""
        )
    parser.add_argument('input', type=str, help='Path to the source teach.')
    parser.add_argument(
            'output', 
            type=str, 
            help='Where to store the reversed version.'
        )
    ns = parser.parse_args()

    if (not os.path.isdir(ns.input)):
        raise Exception('Input provided is not a directory')
    if (not os.path.isdir(ns.output)):
        os.mkdir(ns.output)

    # invert positions
    posFilepath = os.path.join(ns.input, "positions.pl")
    lastTime = 0.0 # The time the teach finished. 
    if(os.path.isfile(posFilepath)):
        lastTime = convert_position_file(
                posFilepath, 
                os.path.join(ns.output, "positions.pl")
            )
    else:
        raise Exception('Position file not found')

    
    # invert speeds
    speedFilepath = os.path.join(ns.input, "speeds.sl")
    if (os.path.isfile(speedFilepath)):
        convert_speed_file(
                speedFilepath, 
                os.path.join(ns.output, "speeds.sl"),
                lastTime)
    else:
        raise Exception('Speed file not found')

    # invert anchor points.
    anchorPointFilepath = os.path.join(ns.input, "anchorPoints.apd")
    if (os.path.isfile(anchorPointFilepath)):
        convert_anchor_point_file(
                anchorPointFilepath,
                os.path.join(ns.output, "anchorPoints.apd")
            )
    else:
        raise Exception('Anchor point directory not found')

    
    # Copy the anchor points.
    copy_anchor_points(ns.input, ns.output)

