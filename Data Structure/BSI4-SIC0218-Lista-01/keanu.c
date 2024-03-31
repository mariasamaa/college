#include <stdio.h>
 
int main() {
 
    /*  n = número de casas na linha
        p = casas pretas do tabuleiro
        b = casas brancas do tabuleiro */
    
    int n, p=0, b=0, casas = 0;
    scanf("%d", &n);
    
    casas = (n*n); // número total de casas no tabuleiro
    p = casas/2; 
    b = casas/2 + (casas%2);
    
    /*  o tabuleiro "começa" com a casa branca
        em caso de casas impares, sempre vai 
        ter uma casa a mais que as pretas */
    
    printf("%d casas brancas e %d casas pretas\n", b, p);
 
    return 0;
}