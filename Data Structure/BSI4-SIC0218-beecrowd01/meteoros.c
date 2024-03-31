#include <stdio.h>
 
int main() {
 
    // (x1, y1) = canto superior esquerdo da fazenda
    // (x2, y2) = canto inferior direito da fazenda
    // (x, y)  = coordenadas do meteoro
    // n = numero de meteoritos (quantidade de repticoes)
    // c = contador (informa numero do teste)
    int x1=0, x2=0, x=0, y1=0, y2=0, y=0, n=0, c=0;
    
    while (1) {
        
        // determinar limites das da fazenda
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    
       
        // soma = número total de meteoros caídos na propriedade
        int soma = 0;
        
        // incrementar contador para informar numero do teste
        c++;
        
        // conferir se é a entrada final (tudo 0)
        if (x1!=0 && x2!=0 && y1 !=0 && y2 != 0) {
           
            //informar quantidade de meteoros a serem lidos
            scanf("%d", &n);
        
            // ler as coordenadas dos meteoros
            for (int i = 0; i<n; i++) {
                scanf("%d %d", &x, &y);
            
                // conferir se o meteoro caiu dentro da propriedade
                if (x1<=x && x<=x2 && y<=y1 && y2<=y) {
                    soma++; //aumentar o contador de meteoros
                } 
            }
    
            //informar a identificação do teste
            printf("Teste %d\n%d\n", c, soma);
        } else {
            break;
        }
    }
    
    return 0;
}