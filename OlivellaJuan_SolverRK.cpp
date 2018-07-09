#include <iostream>
#include <cstdlib>
#include <cmath>
#include <math.h>


using std::cout;
using std::endl;
using std::abs;


float funcion(float x, float y);


int main(){

  float h = 0.01;

  int maxx = 4;

  int minx = 0;

  int puntos = (maxx-minx)/(h);

  float x[puntos];

  float y[puntos];

  float error[puntos];

  x[0] = minx;
  
  y[0] = 1.0;


  error[0] = 0.0;


  for(int i = 1; i < puntos; i++){

    float k1 = h*funcion(x[i-1], y[i-1]);
    float k2 = h*funcion(x[i-1] + 0.5*h,y[i-1] +0.5*k1);
    float k3 = h* funcion(x[i-1] + 0.5*h, y[i-1] +0.5*k2);
    float k4 = h* funcion(x[i-1] + h, y[i-1] + k3);

    float promedioK = (k1 + 2*k2 + 2*k3 + k4)*(1.0/6.0);

    x[i] = x[i-1] + h;

    y[i] = y[i-1] + promedioK;

    error[i] = abs (y[i] - (exp (x[i])));

    cout << x[i] << "  " << y[i] <<  "  " << error[i] << endl;

  }


}


float funcion(float xx, float yy){

  return yy;


}