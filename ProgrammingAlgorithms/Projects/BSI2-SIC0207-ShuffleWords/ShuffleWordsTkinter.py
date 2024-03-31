import gamefuncs
import tkinter

def main_game_tkinter():
        palavra = gamefuncs.main_play(categoria.get(),dificuldade.get())
        palavra_sorte.set(palavra)
        
def verificando_igualdade():
        for _ in range (0,5):
                if tentativa == palavra_sorte:
                        corrigir.set("Parabéns! Você acertou!")
                else:
                        corrigir.set(gamefuncs.coach_inspirador())

# Abrindo a janela principaç
main_window = tkinter.Tk()
main_window.title ("Shuffle Words")
main_window.geometry("500x800")

# inserindo texto de introdução
texto1 = """            O EMBARALHADOR DE PALAVRAS
        VOCÊ CONSEGUE DESCOBRIR A PALAVRA?\n
1. Escolha uma categoria de palavras
2. Escolha o nível de dificuldade
3. Vou sortear e embaralhar uma palavra aleatória
4. Você tem 5 chances para descobrir sua palavra\n
                  Vamos jogar?"""
intro_texto = tkinter.Text(main_window, height=9, width=50)
intro_texto.insert(tkinter.INSERT, texto1)
intro_texto.pack()


# texto de categorias
categ_texto = tkinter.Text(main_window, height=1, width=50)
categ_texto.insert(tkinter.INSERT, "Selecione uma das categorias abaixo:")
categ_texto.pack()

# caixas seleção de categoria
categoria = tkinter.StringVar()
tkinter.Radiobutton(main_window, text = "Países do Mundo", variable=categoria, value="1").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Animais em Geral", variable=categoria, value="2").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Sabores de Pizza", variable=categoria, value="3").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Objetos em Geral", variable=categoria, value="4").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Cidades do Mundo", variable=categoria, value="5").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Cores", variable=categoria, value="6").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Frutas", variable=categoria, value="7").pack(anchor='w')

# texto das dificuldades
categ_texto = tkinter.Text(main_window, height=1, width=50)
categ_texto.insert(tkinter.INSERT, "Selecione uma dificuldade de palavras:")
categ_texto.pack()

# caixas de seleção de dificuldades
dificuldade = tkinter.StringVar()
tkinter.Radiobutton(main_window, text = "Fácil", variable=dificuldade, value="1").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Intermediário", variable=dificuldade, value="2").pack(anchor='w')
tkinter.Radiobutton(main_window, text = "Difícil", variable=dificuldade, value="3").pack(anchor='w')

# botão de início do jogo
tkinter.Button(main_window, text="Start", fg="RED", command=main_game_tkinter).pack()

# secção de saída da palavra embaralhada
tkinter.Label(main_window, text="Sua palavra é: ").pack()
palavra_sorte = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=palavra_sorte).pack()

#Tentativas
tkinter.Label(main_window, text="Digite a palavra correta aqui: ").pack()
tentativa = tkinter.StringVar()
tkinter.Entry(main_window, textvariable=tentativa).pack()

# Verificar
tkinter.Button(main_window, text="Veririficar",command=verificando_igualdade).pack()
corrigir = tkinter.StringVar()
tkinter.Message(main_window, textvariable=corrigir).pack()
              
main_window.mainloop()
    