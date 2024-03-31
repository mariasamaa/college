# Avaliação 1 - BSI
from math import ceil


def duracao_viagem(dias, horas):
    # Elabore um programa que leia a duração de uma viagem em dias e horas. 
    # Calcule e informe a duração total da viagem em número de horas.
    #     Exemplo:
    #     Número de dias: 2
    #     Número de horas: 5
    #     Total de horas: 53
    # Argumentos: dias (int) = uma quantidade de dias
    #            horas (int) = uma quantidade de horas
    # Retorna: (int): uma quantidade de horas.

    total = (dias*24)+horas
    return total


def jardas_para_metros(jardas):
    
    # 1 jarda equivale a 0.9144 metros. Desenvolva uma função 
    # que receba um valor em jardas e retorne o valor em metros.

    # Argumentos: jardas (float) = uma quantidade de jardas
    # Retorna: (float) = uma quantidade em metros, com 2 casas decimais.

    jardas_em_metros = 0.9144
    metros = jardas * jardas_em_metros
    return round(metros,2)
    


def aluguel_hotel_urbano(valor_diaria, dias):

    # Recebe uma quantidade de dias que ficou hospedado e o valor da
    # diária, e retorna o valor a ser pago, considerando um acréscimo de
    # R$ 65,00 para limpeza e 6% de taxa de administração sobre o valor
    # do aluguel, sem a taxa de limpeza

    # Argumentos: valor_diaria (float) =  o valor da diária
    #              dias (int) = a quantidade de dias de hospedagem
    # Retorna: float = o valor do aluguel, com duas casas decimais

    limpeza = 65.00
    taxa = 6
    aluguel_bruto = valor_diaria * dias 
    taxa_adm = ((aluguel_bruto * taxa)/100)
    aluguel = aluguel_bruto + limpeza + taxa_adm
    return round(aluguel,2)


def acesso_4G(qt_alunos_total, qt_alunos_4G):

    # Você foi encarregado de realizar uma pesquisa sobre 
    # acesso a redes 4G. A sua pesquisa deverá apresentar 
    # o percentual de alunos da sua escola que possuem 
    # acesso ao 4G. Para isso, elabore um algoritmo que 
    #leia o número total de alunos da sua escola e o número
    #de alunos que possuem acesso a redes 4G, por fim, com
    #base nestes dados, escreva o percentual de alunos com 
    #acesso ao 4G. Por exemplo, em uma escola com 2000 alunos, 
    #apenas 700 alunos possuem acesso à Internet, o que equivale 
    #a 40% destes 2000 alunos.

    # Argumentos: qt_alunos_total (int) = uma quantidade de horas
    #             qt_alunos_computador (int) = uma quantidade de minutos
    # Retorna:(float) = percentual de alunos com acesso a computadores
    #                       com duas casas decimais.

    alunos_4g_porcentagem = (100 * qt_alunos_4G) / qt_alunos_total
    return round(alunos_4g_porcentagem,2)

    


def media_ponderada(prova, trabalho, exercicio):

    # Calcule a média ponderada, sabendo que os pesos são os seguintes:
    # - prova: peso 5
    # - trabalho: peso 3
    # - exercício : peso 1
    #Dica: eliminar os números mágicos.

    # Argumentos:
    #     prova (float): nota de uma prova, entre 0 e 10.
    #     trabalho (float): nota do trabalho, entre 0 e 10.
    #     exercicio (float): nota do exercício, entre 0 e 10.

    # Retorna:
    #     float: média ponderada das notas, com 1 casa decimal

    peso_prova = 5
    peso_trabalho = 3
    peso_excercício = 1
    media1 = (prova * peso_prova)+(trabalho * peso_trabalho) + (exercicio * peso_excercício)
    media2 = media1/9
    return round(media2,1)


def lan_house(valor_15_minutos, qt_minutos_uso):
    # Elaborar um programa para uma lan house. O programa deve 
    # ler o valor para cada 15 minutos de uso de um computador 
    #e o tempo do cliente em minutos. Informe o valor a ser pago 
    #pelo cliente, sabendo que as frações extras de 15 minutos 
    #devem ser cobradas de forma integral.
        # Exemplo:
         # Valor para 15 minutos RS: 3.00
         # Minutos de uso: 25
         # Total a Pagar R$: 6.00

    # Argumentos: valor_15_minutos (float) = o valor ser cobrado a cada 15 minutos
    #             qt_minutos_uso (int) = a quantidade de minutos que foi utilizado
    # Retorna: (float) =  o valor a ser pago, com 2 casas decimais

    from math import ceil
    valor = ceil(qt_minutos_uso/15)
    valor1 = valor * valor_15_minutos
    return round(valor1,2)


def trimestre(mes):
    # Dado um mês como um inteiro de 1 a 12, retorna a qual 
    # trimestre do ano ele pertence como um número inteiro. 
        #Por exemplo: mês 2 (fevereiro), faz parte do primeiro trimestre; 
        # o mês 6 (junho), faz parte do segundo trimestre; 
        # e o mês 11 (novembro), faz parte do quarto trimestre.

    # Argumento: mes (inteiro) = o mês
    # Returna: inteiro = o trimestre a que o mês pertence.

    trimestre = mes/3
    return ceil(trimestre)
    
# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("Duração da viagem: ")
    test(duracao_viagem(0, 0), 0)
    test(duracao_viagem(1, 0), 24)
    test(duracao_viagem(0, 1), 1)
    test(duracao_viagem(1, 30), 54)
    test(duracao_viagem(2, 40), 88)

    print("Metros para jardas: ")
    test(jardas_para_metros(1), 0.91)
    test(jardas_para_metros(2), 1.83)
    test(jardas_para_metros(3), 2.74)
    test(jardas_para_metros(4), 3.66)
    test(jardas_para_metros(5), 4.57)

    print("Aluguel do airBnB:")
    test(aluguel_hotel_urbano(100, 1), 171.00)
    test(aluguel_hotel_urbano(100, 2), 277.00)
    test(aluguel_hotel_urbano(200, 10), 2185.00)
    test(aluguel_hotel_urbano(50, 5), 330.00)

    print("Acesso 4G:")
    test(acesso_4G(500, 0), 0.00)
    test(acesso_4G(500, 500), 100.00)
    test(acesso_4G(500, 250), 50.00)
    test(acesso_4G(500, 200), 40.00)
    test(acesso_4G(495, 133), 26.87)
    test(acesso_4G(2000, 700), 35)

    print("Média ponderada:")
    test(media_ponderada(10, 10, 10), 10)
    test(media_ponderada(7, 7, 7), 7)
    test(media_ponderada(5, 8, 10), 6.6)
    test(media_ponderada(0, 0, 0), 0)

    print("Lan House: ")
    test(lan_house(0, 0), 0)
    test(lan_house(1, 0), 0)
    test(lan_house(0, 1), 0)
    test(lan_house(1, 1), 1)
    test(lan_house(5, 70), 25)
    test(lan_house(3, 25), 6)
    test(lan_house(2, 7), 2)

    print("Trimestre: ")
    test(trimestre(1), 1)
    test(trimestre(2), 1)
    test(trimestre(3), 1)
    test(trimestre(4), 2)
    test(trimestre(5), 2)
    test(trimestre(6), 2)
    test(trimestre(7), 3)
    test(trimestre(8), 3)
    test(trimestre(9), 3)
    test(trimestre(10), 4)
    test(trimestre(11), 4)
    test(trimestre(12), 4)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")