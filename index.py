import numpy as np
import matplotlib.pyplot as plt
from utils import plot_lines
multi_d=np.array([[1,2,3],[3,4,4]])
print(multi_d.ndim)
#Maths operations
array_one=np.array([1,2,3])
array_two=np.array([4,5,6,7,8,9])
# additon=array_one+array_two
# print(additon)
# print(array_one-array_two)
# print(array_one*array_two)
# print(np.vstack((array_two,array_one)))
# print(np.hstack((array_two,array_one)))
print(np.hsplit(array_two,3))