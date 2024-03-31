from random import randint
import funcoesCPF as f
import tkinter


def varios_cpfs():
    lista_cadastros = open("listaCPF.txt", "a")
    soma = 0
    while soma < int(quantidade.get()):
        cpf = "".join([str(randint(0, 10)) for _ in range(0, 9)])
        cpf += f.test_dv_completo(cpf)
        if len(cpf) == 11 and f.test_cpf_completo(cpf) == True:
            texto = f"{f.coloca_mascara_cpf(cpf)} | {f.tira_mascara_cpf(cpf)}\n"
            lista_cadastros.write(texto)
            soma += 1
        else:
            pass


def mostrar_lista():
    banco = open('listaCPF.txt', 'r')
    new_window = tkinter.Tk()
    new_window.title("Banco de CPFs")
    new_window.geometry("400x500")

    banco = open('listaCPF.txt').read()
    t = tkinter.Text(new_window, height=100, width=50)
    t.insert(tkinter.INSERT, banco)
    t.pack()


def limpar_lista():
    banco = open('listaCPF.txt', 'w')
    banco.close()


# monstagem da janela principal
main_window = tkinter.Tk()
main_window.title("Gera lista de CPF")
main_window.geometry("300x180")

texto = """Este programa vai gerar uma lista
de CPFs válidos. Para criar novas
listas, copie seus CPFs e clique
em "limpar banco" para gerar nova
lista vazia."""
t = tkinter.Text(main_window, height=3, width=50)
t.insert(tkinter.INSERT, texto)
t.pack()

# caixa de inserção de texto com variável que será usada para gerar lista de cpf
texto2 = "Digite aqui a quantidade de CPFs que você deseja gerar: "
tkinter.Label(main_window, text=texto2).pack()
quantidade = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=quantidade).pack()

tkinter.Button(main_window, text="gerar CPFs",
               fg="RED", command=varios_cpfs).pack()


tkinter.Button(main_window, text="mostrar banco atual",
               command=mostrar_lista).pack()

tkinter.Button(main_window, text="limpar banco", command=limpar_lista).pack()

# Abrir a caixa de diálogo
main_window.mainloop()
