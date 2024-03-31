#include <stdio.h>

// TAD para a representação de uma esfera
typedef struct esfera Esfera;

Esfera * criar_esfera (double raio);
    /* Função que cria uma esfera a partir de um
    valor para o seu raio definido como argumento*/

void excluir_esfera (Esfera *esferinha); 
    /*Função que destroi os recursos alocados
    para a estrutura da esfera passada como argumento*/

double acessar_raio (Esfera* esferinha);
    /*Função que acessa as informações da esfera (de raio)*/

double acessar_volume(Esfera* esferinha);
    /*Função que acessa as informações da esfera (de volume)*/

double acessar_area(Esfera* esferinha);
    /*Função que acessa as informações da esfera (de area)*/

void atribuir_raio (Esfera *esferinha, double raio);
    /*Função que recebe um novo valor de raio e 
    modifica o tamanho da esfera*/
