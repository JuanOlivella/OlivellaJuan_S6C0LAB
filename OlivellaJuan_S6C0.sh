# Compila el programa de la ecuacion Euler

g++ -std=c++11 OlivellaJuan_SolverE.cpp 


#Ejecuta el programa de la ecuacion Euler

./a.out > datosEuler.dat


# Genera el grafico de la ecuacion y del error  Euler

python OlivellaJuan_plotsE.py

rm a.out

rm datosEuler.dat


# Compila el programa de la ecuacion Leap

g++ -std=c++11 OlivellaJuan_SolverLF.cpp 


#Ejecuta el programa de la ecuacion Leap

./a.out > datosLeap.dat


# Genera el grafico de la ecuacion y del error Leap

python OlivellaJuan_plotsLF.py

rm datosLeap.dat

rm a.out


# Compila el programa de la ecuacion RK

g++ -std=c++11 OlivellaJuan_SolverRK.cpp 


#Ejecuta el programa de la ecuacion RK

./a.out > datosRK.dat


# Genera el grafico de la ecuacion y del error RK

python OlivellaJuan_plotsRK.py

rm datosRK.dat

rm a.out





