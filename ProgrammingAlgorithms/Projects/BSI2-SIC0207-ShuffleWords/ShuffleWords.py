import gamefuncs 

def escolher_categoria():
    # Seleção de categorias pelo usuário
    categoria = str(input(
    "\n\033[33mSelecione sua categoria:\n"
    "\033[37m[ 1 ] Países do mundo   \n"
    "[ 2 ] Animais domésticos e selvagens\n"
    "[ 3 ] Sabores de Pizza\n"
    "[ 4 ] Objetos em geral\n"
    "[ 5 ] Cidades do Mundo\n"
    "[ 6 ] Cores\n"
    "[ 7 ] Frutas\n"
    "Digite aqui: "
    ))
    
    # Controle de erros de digitação
    if categoria not in "1234567":
        categoria = gamefuncs.controle_categoria(categoria)
    return categoria

def escolher_dificuldade():       
    # Seleção de dificuldade pelo usuário
    dificuldade = str(input(
    "\n\033[33mSelecione o nível de dificuldade:\n"
    "\033[37m[ 1 ] Fácil\n"
    "[ 2 ] Médio\n"
    "[ 3 ] Difícil\n"
    "Digite aqui: "  
    ))
    
    # Controle de erros de digitação
    if dificuldade not in "123":
        dificuldade = gamefuncs.controle_dificuldade(dificuldade)
    return dificuldade

def jogar_outra_vez():
    jogar = gamefuncs.jogar_novamente()
    if jogar == "1":
            main_play()
    if jogar == "2": 
        print ("\n\033[34mObrigado por jogar esse jogo!\033[0m")

def main_play():
    
    categoria = escolher_categoria()
    dificuldade = escolher_dificuldade()    
   
    # Escolher e embaralhar uma palavra dentro da categoria/dificuldade escolhida
    categoria_sorte = gamefuncs.seleciona_palavra(categoria)
    dificuldade_sorte = gamefuncs.nivel_dificuldade(dificuldade,categoria_sorte)
    palavra_sorte = gamefuncs.escolhe_palavra(dificuldade_sorte)
    palavra_embaralha = gamefuncs.embaralhador(palavra_sorte)

    # interação com o usuário: aqui o jogo começa!
    gamefuncs.main_game(palavra_embaralha, palavra_sorte)
    
    # interação para o usuário encerrar o jogo ou jogá-lo novamente
    jogar_outra_vez()   

def main():
    
    print ("""
    \033[35m\n             O EMBARALHADOR DE PALAVRAS
    \033[37m    VOCÊ CONSEGUE DESCOBRIR A PALAVRA?\n
    1. Escolha uma categoria de palavras
    2. Escolha o nível de dificuldade
    3. Vou sortear e embaralhar uma palavra aleatória
    4. Você tem 5 chances para descobrir sua palavra\n
    \033[35mVamos jogar?"""
    )
    #jogar o jogo
    main_play()
    
if __name__ == "__main__":
    main()
    
