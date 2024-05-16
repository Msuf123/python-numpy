import numpy as np
import matplotlib.pyplot as plt
array=np.array([[4,1],[5,1]],dtype=np.dtype(float))

print(array)
constants=np.array([10,12])
print(np.linalg.solve(array,constants))
