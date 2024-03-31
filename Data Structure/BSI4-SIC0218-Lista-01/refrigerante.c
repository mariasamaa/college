#include <stdio.h>
 
int main() {
 
    /*  e = número de garrafas vazias que o Tim já tem
        f = número de garrafas vazias encontradas
        c = quantidade de garrafas vazias para trocar por uma cheia
        resto = resto = variável resto de divisão, usada na verificação 
        r_bebidos = total de refrigerantes bebidos pelo Tim */
    
    int e, f, c, resto = 0, r_bebidos = 0;
    scanf("%d %d %d", &e, &f, &c);
    e += f;
    
    while (1) {
        
        
        
        if (e >= c) {
            //verificar se sobraram garrafas vazias insuficientes
            resto = e % c; 
            
            // somar a quantidade de refrigerantes cheios trocados
            r_bebidos += (e/c); 
            
            // somar a quantidade de refrigerantes bebidos com os insuficientes
            e = (e / c) + resto; 
            
        } else { 
            break;
        }
    }
    
    printf("%d\n", r_bebidos);
    
    
    return 0;
}