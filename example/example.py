from numpy import *
import pipcpptemp

arr = pipcpptemp.CppFunc(array([0,0,0]), 3)
print(arr)