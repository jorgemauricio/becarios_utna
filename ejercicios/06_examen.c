
// Author: Jorge Mauricio
//Email: jorge.ernesto.mauricio@gmail.com
//Date: 2018-02-01
//Version: 1.0
//No. Examen 5
//Valor: 10 puntos
//El siguiente programa pide al usuario 2 números
//para posteriormente sumarlos e imprimir
//el resultado

#include <stdio.h>
//#include <stdio.h>

int main(){
  int num1;
  int num2;
  int suma;

  printf("Ingresa el primer numero: ");
  scanf("%i",&num1);
//  printf("El numero que ingresaste es %i\n", num1);
  printf("Ingresa el segundo numero: ");
  scanf("%i",&num2);
  suma= num1+num2;
  printf("El resultado de la suma  es %i\n", suma);


  return 0;
}
