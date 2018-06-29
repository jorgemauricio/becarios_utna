
/*######################################
# Author: Lucrecia Rodríguez
# Email: lucrepbarone@gmail.com
# Date: 2018-06-28
# Version: 1.0
#######################################*/
// Valor: 10 puntos
//El siguiente programa pide al usuario 2 números
//para posteriormente sumarlos e imprimir
//el resultado
//FUNCIONA
#include <stdio.h>
int main()
{
  int number1;
  int number2;
  printf("Ingrese el primer número:  ");
  scanf("%i",&number1);
  printf("Ingrese el segundo número:  ");
  scanf("%i",&number2);
  int suma;
  suma= number1+number2;
  printf("%i + %i = %i \n",number1,number2,suma);
  return 0;
}
