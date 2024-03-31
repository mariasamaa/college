#include <stdlib.h>
#include <stdio.h>
#include "esfera.h"


int main () {

    double raio=3; //atirbuir um valor pré-detemrinado para raio
    Esfera *esferinha; //criar uma variável que será de tipo Esfera

    esferinha = criar_esfera(raio); //criar a esfera com o argumento raio
    printf("Raio: %.1lfcm\n", acessar_raio(esferinha)); //usar método de acesso para consultar o valor da propriedade raio
    printf("Volume: %.1lfcm\n", acessar_volume(esferinha)); //usar método de acesso para consultar o valor da propriedade volume
    
    atribuir_raio(esferinha, 5.0); //alterar valores das propriedades da esfera com um novo valor pré-determinado
    printf("Raio: %.1lfcm\n", acessar_raio(esferinha));
    printf("Volume: %.1lfcm\n", acessar_volume(esferinha));
    printf("Area: %.1lfcm\n", acessar_area(esferinha));

    scanf("%lf",&raio); //ler um valor determinado pelo usuário
    atribuir_raio(esferinha, raio);
    printf("Raio: %.1lfcm\n", acessar_raio(esferinha));
    printf("Volume: %.1lfcm\n", acessar_volume(esferinha));
    printf("Area: %.1lfcm\n", acessar_area(esferinha));
    
    excluir_esfera(esferinha); //liberar o espaço da esferinha, excluí-la

    /*Não descomentar próxias linhas! Foram usadas apenas para testes
    de implementação e, como esperado, depois de excluir a esferinha,
    os métodos de acesso retornam valores com*/

    // printf("Raio: %.1lfcm\n", acessar_raio(esferinha)); //retorna 0
    // printf("Volume: %.1lfcm\n", acessar_volume(esferinha)); //retorna valor negativo aleatório

    return 0;
}
