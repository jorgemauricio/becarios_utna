
/*#######################################
# Author: Lucrecia Rodríguez
# Email: lucrepbarone@gmail.com
# Date: 2018-06-28
# Version: 1.0
#######################################*/
//Valor: 10 puntos
//Corregir el siguiente código en c
//FUNCIONA


#include <stdio.h>
int main()
{
  int number1;
  int number2;


    //Print Menu
    printf("El siguiente programa te solicitara que ingreses dos números");
    printf("Posteriormente te indicara los números que te solicito");
    printf("Primero desplegando el primer número");
    printf("Y en seguida el segundo número\n");

    //printf() dislpays the formatted output
    //number1=input("Ingresa el primer entero: ")

    //scanf() reads the formatted input and stores them
    printf("Ingrese el primer número:  ");
    scanf("%i",&number1);
    printf("Ingrese el segundo número:  ");
    scanf("%i",&number2);

    printf("Primer número %i \n",number1);
    printf("Segundo número %i \n",number2);
    //printf() dislpays the formatted output

    //scanf() reads the formatted input and stores them
    //scanf("%s"+ number3);

    //printf() displays the formatted output
    //i entero f flotante %.2f dos decimales
    //printf("La suma es  %i \n", suma);
    return 0;

}
//if __name__=='__main__':
//main()
