#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy
import scipy
import pylab
# linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值


fileTrimIn = 0 
fileTrimOut = 200
fileDuration = fileTrimOut - fileTrimIn


def fourBezerCurve(p0, p1, p2, p3, percent):
    fTemp = 1 - percent
    fResult = fTemp * fTemp * fTemp * p0
    fResult += 3 * fTemp * fTemp * percent * p1
    fResult += 3 * fTemp * percent * percent * p2
    fResult += percent * percent * percent * p3
    fResult = fResult * fileDuration
    fResult += fileTrimIn

    i = 1
    for item in fResult:
        print("%10.3f" % item, end=""),
        if (i % 5 == 0):
            print()
        i += 1

    return fResult



p0 = 0    # file trim in
p1 = 0    # control point
p2 = 0  # control point
p3 = 0.2  # file trim out

timelineStart = 0
timelineEnd = 100
timelineDuration = timelineEnd - timelineStart
percent = 1.0 / timelineDuration 
print("timeline percent ", percent)

x = pylab.linspace(timelineStart, timelineEnd, timelineDuration)
pylab.plot(x, fourBezerCurve(p0, p0 + p1, p2 + p3, p3, (x - timelineStart) * percent))

p0 = p3
p1 = 0.01
p2 = -0.5
p3 = 1.0
timelineStart = 100
timelineEnd = 200

timelineDuration = timelineEnd - timelineStart
percent = 1.0 / timelineDuration 
print("timeline percent ", percent)

x = pylab.linspace(timelineStart, timelineEnd, timelineDuration)
pylab.plot(x, fourBezerCurve(p0, p0 + p1, p2 + p3, p3, (x - timelineStart) * percent))


pylab.show()
