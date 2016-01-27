# coding : utf-8

from numpy import *
array = random.rand(4, 4)
print array
randMat = mat(array)
print randMat
invrandMat = randMat.I
I = randMat*invrandMat
print I
myeye = I - eye(4)
print myeye