
import matplotlib.pyplot as plt
import numpy as np
p = int(input("Enter n: "))
k = int(input("Enter the width of the well ,i.e, k: "))
num = p/k
num1 = 2/k
x = np.linspace(0,k,2000)
y = np.sin(num*np.pi*x)**2
z = y*num1
plt.plot(x,z,label = "Line",color = "m")
plt.xlabel("x", fontsize = 20)
plt.ylabel("|ψ|2" , fontsize = 20)
plt.title (" Probability Distribution Curve " , fontsize = 25)
plt.legend()
plt.show()