#include <stdio.h>
 
int main() {
 
    // n = numero de casos
    // c = contador de jogadas
    // x = pontuação dos dardos
    // d = distância da jogada
    int n, c = 0, x = 0, d = 0;
    scanf("%d", &n);
    
    for (int i=0; i<n;i++) {
    
        // ler as jogadas de Joao
        int soma_joao = 0;
        for (c=0;c<3;c++) {
            scanf("%d %d", &x, &d);
            soma_joao += x * d; // soma das pontuações de Joao
        }
        
        // ler as jogadas de Maria
        int soma_maria = 0; // soma das pontuações de Maria
        for (c=0;c<3;c++) {
            scanf("%d %d", &x, &d);
            soma_maria += x * d;
        }
        
        // fazer comparação entre pontuaçoes
        if (soma_joao > soma_maria) {
            // informar que Joao ganhou a rodada
            printf("JOAO\n");
        } else { 
            // informar que Maria ganhou a rodada
            printf("MARIA\n");
        }  //não especifica empate na descrição do problema,
           //portanto não foi incluso
    }
    
    return 0;
}