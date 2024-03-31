import funcoesCPF
from time import sleep
from random import randint


def controle_selecao_main(selecao):
    # Controle de erros de seleção/digitação
    while selecao not in "1234" or len(selecao) != 1:
        print("\033[31mResposta inválida\033[0m")
        selecao = str(input("Digite sua seleção: "))
    return selecao


def controle_selecao_UF():
    # Controle de erros de selção/digitação
    UF = str(input(("""\033[35mDigite aqui:\033[0m """)))
    while len(UF) != 1 or UF not in "0123456789":
        print("\033[31mResposta inválida\033[0m")
        UF = str(input("Digite sua seleção: "))
    return UF


def repetir_operacao():
    # função de interação para repetir operação
    repetir = str(input(
        """    [ 1 ] Sim
    [ 2 ] Não
    \033[35mDigite sua resposta:\033[0m """))

    # controle de erros de selção/digitação
    if repetir not in "12" or len(repetir) != 1:
        while repetir not in "12":
            print("\033[31mResposta inválida\033[0m")
            repetir = str(input("Digite sua seleção: "))
    return repetir


def valida():

    # método principal
    cpf = str(
        input("\n\033[35mVamos verificar seu CPF!\nDigite aqui seu CPF aqui:\033[0m\n"))
    validade = funcoesCPF.test_cpf_completo(cpf)
    print("\033[32mCPF Válido\033[0m") if validade == True else print(
        "\033[31mCPF Inválido\033[0m")

    # repetir função (interação)
    print("\n\033[35mQuer digitar outro CPF?\033[0m")
    repetir = repetir_operacao()

    # realizar função selecionada pelo usuário
    valida() if repetir == "1" else main()


def gerar_CPF():
    # função que gera CPF
    def gerando_CPF():
        cpf = "".join([str(randint(0, 10)) for _ in range(0, 9)])
        cpf = cpf + funcoesCPF.test_dv_completo(cpf)
        if funcoesCPF.test_cpf_completo(cpf) == False and len(cpf) != 11:
            gerando_CPF()
        return cpf

    # mostrar ao usuário o cpf
    cpf = str(gerando_CPF())
    print("\n\033[35mCPF gerado:\033[0m")
    print(f"{funcoesCPF.coloca_mascara_cpf(cpf)} | {funcoesCPF.tira_mascara_cpf(cpf)}")

    sleep(1)

    # repetir função (interação)
    print("\033[35m\nQuer gerar outro CPF?\033[0m")

    repetir = repetir_operacao()
    gerar_CPF() if repetir == "1" else main()


def gera_lista():

    # determinando a quantidade de CPFs a ser gerada
    print("\033[35mVamos gerar uma lista de CPFs.\nQuantos CPFs você precisa gerar?")
    quantidade = int(input("\033[0mDigite aqui: "))

    soma = 0
    cpfs = []
    # função principal de geração da lista
    while soma < int(quantidade):
        cpf = "".join([str(randint(0, 10)) for _ in range(0, 9)])
        cpf += funcoesCPF.test_dv_completo(cpf)
        if len(cpf) == 11 and funcoesCPF.test_cpf_completo(cpf) == True:
            texto = f"{funcoesCPF.coloca_mascara_cpf(cpf)} | {funcoesCPF.tira_mascara_cpf(cpf)}"
            cpfs.append(texto)
            soma += 1
        else:
            pass
    for i in cpfs:
        print(i)

    print("\n\033[35mQuer gerar outra lista?\033[0m")
    repetir = repetir_operacao()
    gera_lista() if repetir == "1" else main()


def main():
    # diálogo de seleção
    print("\n\033[35mGERANDO E VERIFICANDO CPF\033[0m")
    selecao = str(input("""Selecione uma opção:
    [ 1 ] Validar CPF
    [ 2 ] Gerar CPF válido
    [ 3 ] Gerar lista de CPFs
    [ 4 ] Sair
    \033[35mDigite aqui:\033[0m """))

    # controle de erros de digitação
    if selecao not in "1234":
        selecao = controle_selecao_main(selecao)

    # execução da função selecionada
    if selecao == "1":
        valida()
    if selecao == "2":
        gerar_CPF()
    if selecao == "3":
        gera_lista()
    if selecao == "4":
        print("\n\033[36mOBRIGADO POR USAR ESTE PROGRAMA!\033[0m\n")


if __name__ == '__main__':
    main()
