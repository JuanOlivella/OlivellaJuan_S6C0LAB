import numpy as np
import matplotlib.pylab as plt

datos1=np.genfromtxt("datosLeap.dat")

x1 = datos1[:,0]

y1 = datos1[:,1]

error1 = datos1[:,2]

plt.figure()
plt.plot(x1,y1)
plt.title("Solucion con el metodo de Leap")
plt.xlabel("$x$")
plt.ylabel("$y(x)$")
plt.savefig("SolucionLeap.pdf")


plt.figure()
plt.plot(x1,error1)
plt.title("Error con el metodo de Leap")
plt.xlabel("$x$")
plt.ylabel("$Error$")
plt.savefig("ErrorLeap.pdf")
