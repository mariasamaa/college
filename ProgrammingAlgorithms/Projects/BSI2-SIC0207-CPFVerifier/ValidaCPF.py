import funcoesCPF as f
import tkinter


def verificar_CPF():
    # função de verificação
    resultado.set("CPF Válido") if f.test_cpf_completo(
        cpf.get()) else resultado.set("CPF Inválido")


def limpar_labels():
    # função para limpar barras de inserção de texto
    cpf.set("")
    resultado.set("")


# montagem da caixa de diálogo com tkinter
main_window = tkinter.Tk()
main_window.title("Verificação de CPF")
main_window.geometry("300x300")

# texto explicando ao usuário como funciona
texto = "Verificação de CPF: Digite um número\nde CPF e o mesmo será classificado em\nválido ou inválido."
t = tkinter.Text(main_window, height=3, width=50)
t.insert(tkinter.INSERT, texto)
t.pack()

# secção para inserir CPF
tkinter.Label(main_window, text="Digite seu CPF aqui: ").pack()
cpf = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=cpf).pack()

# botão de verificação
tkinter.Button(main_window, text="Verificar",
               fg='RED', command=verificar_CPF).pack()
tkinter.Button()

# secção de saída com verificação
tkinter.Label(main_window, text="Resultado: ").pack()
resultado = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=resultado).pack()

# botão de limpeza das barras de inserção de texto
tkinter.Button(main_window, text="Limpar", command=limpar_labels).pack()

# abrir a caixa de diálogo
main_window.mainloop()
