import math
import numpy as np
import matplotlib.pyplot as plt
list1 = []
list2 = []
def velocity(t):
    if t>=0 and t<=10:
        v=11*(t)^2-5*t
        list1.append(v)
        list2.append(t)

    elif t>=10 and t<=20:
        v = 1100-5*t
        list1.append(v)
        list2.append(t)

    elif t>=20 and t<=30:
        v = 50*t+2*(t-20)^2
        list1.append(v)
        list2.append(t)

    elif t>30:
        v = 1520*(math.exp((-0.2)*(t-26)))
        list1.append(v)
        list2.append(t)

    else:
        v = 0
        list1.append(v)
        list2.append(t)

for i in np.arange(-5,55,5):
    velocity(i)

print(list2)
print(list1)
plt.plot(list1,list2)
plt.show()