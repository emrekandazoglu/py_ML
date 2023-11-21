import numpy as np
import time

start_time=time.time()
A=np.arange(1000000)
A**2

Time_1=time.time()-start_time

start_time_2=time.time()

L=range(1000000)
[i**2 for i in L]
Time_2=time.time()-start_time_2


print(Time_1)
print(Time_2)

