#include <stdio.h>

int main() {
    int n; //quantidade de nomes a serem lidos
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int tam = 0; //zerando o tamanho da string
        char sn[42]; 
        scanf("%s", sn);
        
        //conferindo tamanho da string para leitura
        for (int x=0; sn[tam]!='\0'; x++) {
            tam++;
        }

        int cons = 0; // consecutivas
        int dificil = 0; 

        for (int i = 0;i<tam; i++) {
            
            // verificar se o caractere atual não é uma vogal
            if (sn[i] != 'a' && sn[i] != 'e' && sn[i] != 'i' && sn[i] != 'o' && sn[i] != 'u' &&
                sn[i] != 'A' && sn[i] != 'E' && sn[i] != 'I' && sn[i] != 'O' && sn[i] != 'U') {
                cons++;
            } else {
                cons = 0; 
            }

            if (cons >= 3) {
                dificil = 1;
                break; 
            }
        }

        if (dificil == 1) {
            printf("%s nao eh facil\n", sn);
        } else {
            printf("%s eh facil\n", sn);
        }
    }

    return 0;
}