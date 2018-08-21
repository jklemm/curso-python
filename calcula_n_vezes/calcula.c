/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <string.h>

int eh_primo(int numero) {
    if (numero == 1) {
        return 0;
    }
    
    for (int num = 2; num < numero; num++) {
        if (numero % num == 0) {
            return 0;
        }
    }
    return 1;
}

int main(args) {
    int maximo = 10;
    int total = 0;
    int quantidade = 0;

    printf("Digite um numero: ");
    scanf("%d", &maximo);
    
    for (int n = 1; n <= maximo; n++) {
        if (eh_primo(n) == 1) {
            total += n;
            quantidade++;
        }
    }
    
    printf("Achei %d numeros primos!\n", quantidade);
    printf("O total eh %d.\n", total);
    
    return 0;
}
