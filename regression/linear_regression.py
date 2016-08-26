from scipy import stats
import numpy as np 
from matplotlib import pyplot as plt

x = np.array([112,345,196,325,372,550,302,420,578])
y = np.array([1120,2523,1502,2230,2615,3400,2010,2400,2500])

a, b, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x,y, 'ro', color='blue')

plt.xlabel('Size of the house')
plt.ylabel('Price')

plt.axis([0,600,0,3500])
plt.plot(x,x*a+b,'y')
plt.plot()

#PREDICTION !!!
newX = 200
newY = newX*a+b
print(newY)

plt.show()


#PREDICTION !!!

#newX = 150
#newY = newX*a+b

#print(newY)
