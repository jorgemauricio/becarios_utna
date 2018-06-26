/*
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 5
# Valor: 10 puntos
# Corregir el siguiente código en c
*/

#include <stdio.h>

int main(){

  int number1, number2;

  printf("El siguiente programa te solicitara que ingreses dos numeros");
  printf("Posteriormente te indicara los numeros que te solicito");
  printf("Primer desplegando el primer numero");
  printf("Y en seguida el segundo numero \n");

  printf("Ingresar el primer entero: " );
  scanf("%i",&number1);
  printf("Ingresar el segundo entero: " );
  scanf("%i",&number2);
  printf("Primer número: %i\n", number1);
  printf("Segundo número: %i\n", number2);

  return 0;
}
