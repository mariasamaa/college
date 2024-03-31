#include <stdlib.h>
#include <stdio.h>
#include "esfera.h"

struct esfera {
    double raio; // propriedade raio que pode ser atribuida
    double volume; //propriedade definida dependendo do raio
    double area; //propriedade definida dependedo do raio
}; //tipo exportado


// função que criar uma esfera a partir de um raio
Esfera * criar_esfera (double raio) {
    Esfera* esferinha = (Esfera*) malloc(sizeof(Esfera));
    if (esferinha != NULL) { //se houver espaço para a esferinha
        esferinha->raio = raio; //atribuindo à propriedade "raio" o valor do argumento
        esferinha->volume = (4/3.0)*(3.14159)*(raio*raio*raio); //fórmula do volume da esfera
        esferinha->area = 4*(3.14159)*(raio*raio); // fórmula da area da esfera
        printf("Esfera criada com sucesso\n"); //informar ao usuário que a esferinha foi criada :)
        return esferinha; 
    }
    printf("Espaco Indisponivel\n"); 
    /*  informar que não foi possível criar a esferinha
    se a condição de espaço da estrutura condicional anterior
    não for atendida */
}
    
// libera a memória alocada para a esfera
void excluir_esfera (Esfera* esferinha) {
    free(esferinha); //liberar o espaço
    printf("Esfera excluída com sucesso!\n"); //informar o usuário que a exclusão foi concluída
}

/*Função que acessa as informações da esfera*/
double acessar_raio (Esfera* esferinha) {
    return esferinha->raio; //informar apenas o valor atual do raio
}

double acessar_volume(Esfera* esferinha){
    return esferinha->volume; //informar apenas o valor atual do volume
}

double acessar_area(Esfera* esferinha){
    return esferinha->area;
}

/*Função que recebe um novo valor de raio e modifica
o tamanho da esfera (basicamente, um 'setter' que
altera os valores das propriedades)*/
void atribuir_raio (Esfera* esferinha, double raio) {
    
    esferinha->raio = raio;
    esferinha->volume = (4/3.0)*(3.14159)*(raio*raio*raio); //calcular o volume de novo
    esferinha->area = 4*(3.14159)*(raio*raio); // fórmula da area da esfera
    printf("Valores atualizados com sucesso!\n");
    /*informar ao usuário que a atualização de valores
    foi concluída*/
}
