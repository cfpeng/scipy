#! /usr/bin/env python
# -*- coding:utf-8 -*-

import numpy
import scipy
import pylab
# linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值
x = pylab.linspace(0, 4 * numpy.pi, 100)
pylab.plot(x, numpy.sin(x))
pylab.show()
