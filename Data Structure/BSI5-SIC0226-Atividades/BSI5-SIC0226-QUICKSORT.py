def quicksort (esquerda, direita, dataset):
    if esquerda < direita:
        # mostrando os passos da ordenação conforme teste de mesa
        print(dataset)
        # ponteiro que vai fazer as partições dos subarrays
        ponteiro = particao(esquerda, direita, dataset)
        # subarray à esquerda do ponteiro alocado (elementos menores que o antigo pivô)
        quicksort(esquerda, ponteiro-1, dataset)
        # subarray à direita do ponteiro alocado (elementos maiores que o pivô)
        quicksort(ponteiro+1, direita, dataset)
        
def particao (esquerda, direita, dataset):
    pivo = dataset[direita] # define o ponteiro como o mais a direita (o último elemento da lista)
    i = esquerda - 1 # define o ponteiro como uma posição anterior da que será utilizada, por causa da iteração dentro do for
    
    for j in range(esquerda, direita): # percorre todos os elementos da posição esquerda até a direita
        if dataset[j] <= pivo: # se o elemento da posição j for menor igual ao pivô
            i = i + 1 # o ponteiro vai iterar mais um (por isso i - 1 antes da estrutura de repetição)
            dataset[i], dataset[j] = dataset[j], dataset[i] # troca o elemento na posição i com o elemento da posição j
    
    # ao final da repetição, o elemento na posição direita (pivô) é trocado com o elemento na posição do ponteiro
    dataset[i+1], dataset[direita] = dataset[direita], dataset[i+1]
    return i + 1 # retorna a posição do elemento como ponteiro para a função quicksort, a fim de definir os limites dos subarrays

def main():
    dataset = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6] # lista com 10 elementos
    comprimento = len(dataset) # comprimento do dataset
    esquerda = 0 # posição do primeiro item da lista
    direita = comprimento - 1 # posição do último item da lista
    
    # mostra a lista original (finalidade comparativa)
    print("\033[35mDATASET ORIGINAL\033[0m")
    for i in dataset:
        print(f"{i} ", end="")
    print("\n")
        
    # chama a função quicksort
    # foi adicionado o parâmetro "dataset" por usarmos o main nesta implementação de arquivo único
    quicksort(esquerda, direita, dataset)
    
    # mostra a lista ordenada (finalidade comparativa)
    print("\033\n[35mDATASET ORDENADO\033[0m")
    for i in dataset:
        print(f"{i} ", end="")
        
if __name__ == "__main__":
    main()
