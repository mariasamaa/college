import random
import json

def seleciona_palavra(categoria):
    # Selecionar categoria de palavras
    with open("categorias.JSON") as categorias:
        palavras = json.load(categorias)
    return dict(palavras[categoria])

def nivel_dificuldade (dificuldade,categoria_sorte):
    # Selecionar nível de dificuldade dentro da categoria
    return categoria_sorte[dificuldade]

def escolhe_palavra (dificuldade):
    # Selecionar uma palavra dentro do nível de dificuldade
    return random.choice(dificuldade)

def embaralhador(palavra_sorte):
    # Randomiza ordem de letras da
    palavra_embaralha = list(palavra_sorte)
    random.shuffle(palavra_embaralha)
    return "".join(palavra_embaralha)

def controle_categoria(categoria):
    while categoria not in "1234567":
        print ("\033[31mResposta inválida.\033[0m Por favor, digite novamente")
        categoria = str(input("Digite aqui: "))
    return categoria

def controle_dificuldade(dificuldade):
    while dificuldade not in "123":
        print ("\033[31mResposta inválida.\033[0m Por favor, digite novamente")
        dificuldade = str(input("Digite aqui: "))
    return dificuldade
    
def coach_inspirador():
    # seleção de frases de motivação
    frases_motivacionais = [
        "Sem lutas não há derrotas.",
        "O caminho é longo, mas a derrota é certa.",
        "Você consegue, eu acredito em você.",
        "É impossível se não tentar.",
        "Acredite em você, porque eu acredito.",
        "So vence quem não desite: Você consegue.",
        "Lute! Busque! Batalhe! Ainda não foi dessa vez.",
        "A persistência realiza o impossível.",
        "No meio da dificuldade, encontra-se a oportunidade.",
        "Você precisa fazer aquilo que pensa que não é capaz de fazer.",
        "O sucesso é ir de fracasso em fracasso sem perder o entusiasmo."
    ]

    return random.choice(frases_motivacionais)
    

def palavra_emabaralhada(categoria,dificuldade):
    # Escolher e embaralhar uma palavra dentro da categoria/dificuldade escolhida
    categoria_sorte = seleciona_palavra(categoria)
    dificuldade_sorte = nivel_dificuldade(dificuldade,categoria_sorte)
    palavra_sorte = escolhe_palavra(dificuldade_sorte)
    palavra_embaralha = embaralhador(palavra_sorte)
    return palavra_embaralha


def main_game (palavra_embaralha,palavra_sorte):
    # interação com o usuário: aqui o jogo começa!
    print(
        "\n"
        "\033[33mA palavra embaralhada é:\n"
        f"\033[37m{palavra_embaralha}\n"
        '------------------------'
    )
    contador = 1

    for i in range(5):
        resposta = str(input("Sua resposta: "))
        if resposta.lower() == palavra_sorte:
            break
        else:
            if i != 4:
                coach = coach_inspirador()
                print(f"\033[31m{coach} Tente de novo.")
                print(f"\033[37mVocê ainda tem {4-i} tentativas")
        contador += 1

    if resposta == palavra_sorte:
        print(
            f"\033[32mParabens! Você acertou! A palavra era {palavra_sorte.upper()}"
            f"\nVocê acertou em {contador} tentativas"
            )  
    else:
        print(f"\033[33mNão foi dessa vez... A palavra era {palavra_sorte.upper()}\033[0m")


def jogar_novamente():
    jogar_novamente = str(input("\033[0mQuer jogar novamente?\n[ 1 ] Sim\n[ 2 ] Não\nDigite aqui: "))
    if jogar_novamente not in "12":
        while jogar_novamente not in "12":
            print ("\033[31mResposta inválida.\033[0m Por favor, digite novamente")
            jogar_novamente = str(input("Digite aqui: "))
    return jogar_novamente
    