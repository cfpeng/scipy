#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy
import scipy
import pylab
# linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值


fileOffset = 0;

#   
def fourBezerCurve(p0, p1, p2, p3, percent):
    fTemp = 1 - percent
    fResult = fTemp * fTemp * fTemp * p0
    fResult += 3 * fTemp * fTemp * percent * p1
    fResult += 3 * fTemp * percent * percent * p2
    fResult += percent * percent * percent * p3

    return fResult


# s ==> start
# p ==> precision

def filePosition(p0, p1, p2, p3, s, p, x):
    percent = (x - s + 1) * p # percent
    m = 1 + s*p
    temp = 1 + s*p - x*p

    fR0 = p0 * (pow(m,3)*x - 3*pow(m,2)*p*pow(x,2)/2 + m*pow(p,2)*pow(x,3) - pow(p,3)*pow(x,4)/4)
    
    fR1 = 3 * p1 * p * (pow(m,2)*pow(x,2)/2 - 2*m*p*pow(x,3)/3 + pow(p,2)*pow(x,4)/4 - pow(m,2)*s*x + m*s*p*pow(x,2) - pow(p,2)*s*pow(x,3)/3)
    
    fR2 = 3 * p2 * pow(p,2) * (m*pow(x,3)/3 - m*s*pow(x,2) + m*pow(s,2)*x - p*pow(x,4)/4 + 2*s*p*pow(x,3)/3 - pow(s,2)*p*pow(x,2)/2)
    
    fR3 = p3 * pow(p,3) * (pow(x,4)/4 - s*pow(x,3) + 3*pow(s,2)*pow(x,2)/2 - pow(s,3)*x)
    

    return fR0 + fR1 + fR2 + fR3 - fileOffset

p0 = 1    
p1 = 0    
p2 = 0    
p3 = 0.5  

timelineStart = 0
timelineEnd = 99
timelineDuration = timelineEnd - timelineStart + 1
precision = 1.0 / timelineDuration 

x = pylab.linspace(timelineStart, timelineEnd, timelineDuration)
pylab.plot(x, fourBezerCurve(p0, p0 + p1, p2 + p3, p3, (x - timelineStart) * precision))
pylab.plot(x, filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, x + 1))


fileOffset = filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, timelineStart)
print(filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, timelineEnd))
total = 0
for x in range(0, 100):
    speed = fourBezerCurve(p0, p0 + p1, p2 + p3, p3, (x - timelineStart) * precision)
    total += speed
    print("speed = %10.3f  " % speed, end=""),
    print("Total = %10.3f  " % total, end=""),
    position = filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, x + 1)
    print("position = %10.3f  " % position)


p0 = p3
p1 = 0
p2 = 0
p3 = 2.0
timelineStart = timelineDuration
timelineEnd = 199

timelineDuration = timelineEnd - timelineStart + 1
precision = 1.0 / timelineDuration 
startFilePosition = filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, timelineStart)
fileOffset = startFilePosition - total;

x = pylab.linspace(timelineStart, timelineEnd, timelineDuration)
pylab.plot(x, fourBezerCurve(p0, p0 + p1, p2 + p3, p3, (x - timelineStart) * precision))
pylab.plot(x, filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, x + 1))


for x in range(100, 200):
    speed = fourBezerCurve(p0, p0 + p1, p2 + p3, p3, (x - timelineStart) * precision)
    total += speed
    print("speed = %10.3f  " % speed, end=""),
    print("Total = %10.3f  " % total, end=""),
    position = filePosition(p0, p0 + p1, p2 + p3, p3, timelineStart, precision, x + 1)
    print("position = %10.3f  " % position)

pylab.show()
