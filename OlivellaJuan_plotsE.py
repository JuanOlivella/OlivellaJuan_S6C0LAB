import numpy as np
import matplotlib.pylab as plt


datos=np.genfromtxt("datosEuler.dat")

x = datos[:,0]

y = datos[:,1]

error = datos[:,2]

plt.figure()
plt.plot(x,y)
plt.title("Solucion con el metodo de Euler")
plt.xlabel("$x$")
plt.ylabel("$y(x)$")
plt.savefig("SolucionEuler.pdf")


plt.figure()
plt.plot(x,error)
plt.title("Error con el metodo de Euler")
plt.xlabel("$x$")
plt.ylabel("$Error$")
plt.savefig("ErrorEuler.pdf")
