from random import randint
import funcoesCPF as f
import tkinter


def gera_cpf():
    # gerar cpf aleatório (com dígito de região)
    cpf = "".join([str(randint(0, 10)) for _ in range(0, 8)])+UF.get()
    cpf += f.test_dv_completo(cpf)

    # verificar validade do número gerado
    if len(cpf) == 11 and f.test_cpf_completo(cpf) == True:
        resultado.set(f.coloca_mascara_cpf(cpf))
    else:
        gera_cpf


def limpar_labels():
    # função para limpar barras de inserção de texto
    nome.set("")
    UF.set("")
    resultado.set("")


def salvar_CPF():
    # função para salvar os dados dentro de um arquivo
    banco = open('bancoCPFs.txt', 'a')
    novo = f"{nome.get()}, {resultado.get()}\n"
    banco.write(novo)


def mostrar_banco_atual():
    banco = open('bancoCPFs.txt', 'r')
    new_window = tkinter.Tk()
    new_window.title("Banco de CPFs")
    new_window.geometry("400x300")

    banco = open('bancoCPFs.txt').read()
    t = tkinter.Text(new_window, height=100, width=50)
    t.insert(tkinter.INSERT, banco)
    t.pack()


# criando caixa de diálogo com tkinter
main_window = tkinter.Tk()
main_window.title("Geração de CPF")
main_window.geometry("500x550")

# texto explicando ao usuário como funciona
texto = "Geração de um novo CPF:Digite seu nome completo, então selecione o grupo onde está presente sua UF. Será criado um número de CPF em nosso banco de dados para  você. Selecione SALVAR para gravar seus dados em nosso banco."
t = tkinter.Text(main_window, height=5, width=53)
t.insert(tkinter.INSERT, texto)
t.pack()

# secção para inserir nome
tkinter.Label(main_window, text="Digite seu nome aqui: ").pack()
nome = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=nome).pack()


# caixas de seleção de uf para cálculo de CPF
UF = tkinter.StringVar()
grupo1 = "Grupo 1: DF, GO, MS, MT ou TO"
tkinter.Radiobutton(main_window, text=grupo1,
                    variable=UF, value="1").pack(anchor="w")
grupo2 = "Grupo 2:  AC, AM, AP, PA, RO ou RR"
tkinter.Radiobutton(main_window, text=grupo2,
                    variable=UF, value="2").pack(anchor="w")
grupo3 = "Grupo 3: CE, MA ou PI"
tkinter.Radiobutton(main_window, text=grupo3,
                    variable=UF, value="3").pack(anchor="w")
grupo4 = "Grupo 4: AL, PB, PE, RN"
tkinter.Radiobutton(main_window, text=grupo4,
                    variable=UF, value="4").pack(anchor="w")
grupo5 = "Grupo 5: BA ou SE"
tkinter.Radiobutton(main_window, text=grupo5,
                    variable=UF, value="5").pack(anchor="w")
grupo6 = "Grupo 6: MG"
tkinter.Radiobutton(main_window, text=grupo6,
                    variable=UF, value="6").pack(anchor="w")
grupo7 = "Grupo 7: ES ou RJ"
tkinter.Radiobutton(main_window, text=grupo7,
                    variable=UF, value="7").pack(anchor="w")
grupo8 = "Grupo 8: SP"
tkinter.Radiobutton(main_window, text=grupo8,
                    variable=UF, value="8").pack(anchor="w")
grupo9 = "Grupo 9:SC ou PR"
tkinter.Radiobutton(main_window, text=grupo9,
                    variable=UF, value="9").pack(anchor="w")
grupo0 = "Grupo 0: RS"
tkinter.Radiobutton(main_window, text=grupo0,
                    variable=UF, value="0").pack(anchor="w")


# botão que gera novo número aleatório de CPF
tkinter.Button(main_window, text="Gerar novo CPF",
               fg="RED", command=gera_cpf).pack()

# secção de saída com novo número de CPF
tkinter.Label(main_window, text="Novo CPF: ").pack()
resultado = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=resultado).pack()

# botão de limpeza das barras de inserção de texto
tkinter.Button(main_window, text="Limpar", command=limpar_labels).pack()

# botão para salvar o nome + cpf em um arquivo
tkinter.Button(main_window, text="Salvar", command=salvar_CPF).pack()

# botão para mostrar banco atual
tkinter.Button(main_window, text="Mostrar banco atual",
               command=mostrar_banco_atual).pack()

# abrir a caixa de diálogo
main_window.mainloop()
