from . import ext
from numpy import *
from numpy.typing import *

def CppFunc(arr:NDArray, fill:float64):
    print(">> Entering Python Layer.")
    arr = asarray(arr, dtype=float64)
    fill = float64(fill)
    return ext.CppFunc(arr, fill)