# Desenvolva um programa que:
# Tenha uma função que receba uma *url* como parâmetro e pesquisa o
# preço dentro dela, retornando o preço

# Faça a chamada dessa função para as 2 páginas mostradas nesse
# tutorial.

# Estabeleça um valor mínimo de 4.70 e informe que a compra pode ser
# feita quando o valor for inferior a esse limite.

# Após cada consulta, aguarde um tempo de 2 segundos para voltar a
# consultar (isso vai evitar que você seja acusado de um ataque de
# negação de serviço).

# Para informar da compra, envie um email, whatsapp, twitter ou outra
# forma de comunicação.

# Bibliotecas a pesquisar: *time*, *smtplib* e outras.
# -----------------------------------------------------------------------
from cgitb import text
from email import message
from time import sleep
import MessageFunctions  # send messages
import urllib.request  # open URL
import getpass  # hide password


def open_url(url_t, url_p):
    page_trad = urllib.request.urlopen(url_t)
    text_trad = page_trad.read().decode("utf8")
    page_promo = urllib.request.urlopen(url_p)
    text_promo = page_promo.read().decode("utf8")
    return text_trad, text_promo


def find_good_price(text_trad, text_promo, wanted_price):
    better_price = ''
    while True:
        start_trad = text_trad.find(">$") + 2
        end_trad = start_trad + 4
        price_trad = float(text_trad[start_trad:end_trad])

        start_promo = text_promo.find(">$") + 2
        end_promo = start_promo + 4
        price_promo = float(text_promo[start_promo:end_promo])

        # print(f"O preço tradicional está em ${price_trad}")
        # print(f"O preço promocional está em ${price_promo}")

        # Break while loop when finds a better price
        if price_trad < price_promo:
            if price_trad <= wanted_price:
                better_price = int(price_trad)
                break
        else:
            if price_promo <= wanted_price:
                better_price = int(price_promo)
                break

        sleep(10)  # No exercício pede 2 segundos, mas 10 é mais apropriado
    return better_price


def main():

    url_trad = "http://beans.itcarlow.ie/prices.html"  # utl preço tradicional
    url_promo = "http://beans.itcarlow.ie/prices-loyalty.html"  # url preço promoção
    text_trad, text_promo = open_url(url_trad, url_promo)

    # Procurando o melhor preço do café
    wanted_price = 10.00  # preço estipulado no exercício

    print("\033[1;31mOlá, funcionário do Starbuzz!\n\033[0;0m")
    print("Com este programa, você pode descobrir o melhor momento")
    print("para comprar grãos de café com nosso principal fornecedor!")
    print("Primeiro precisamos fazer um rápido cadastro!\n")

    # Área de cadastros para envio de notificações
    print("Por onde você gostaria de ser notificado quando o preço estiver ideal?")
    print("[ 1 ] Via E-mail\n[ 2 ] Via Telegram\n[ 3 ] Via Whatsapp\n[ 4 ] Via Twitter")
    message_selection = str(
        input("Digite somente um dos números solicitados: "))

    # Controle de erros de digitação
    if message_selection not in "1234":
        while message_selection not in "1234":
            print("Resposta inválida. Digite novamente")
            message_selection = str(
                input("Digite somente um dos números solicitados: \n"))

    # Cadastros de acordo com opção de envio
    if message_selection == "1":
        # Cadastro/envio do e-mail
        receiver = str(
            input("\033[1;0mDigite aqui o e-mail do destinatário: \033[0;0m"))
        print(
            f"\nUma mensagem será enviada para seu e-mail quando\no valor do café estiver abaixo de ${wanted_price}")
        better_price = better_price = find_good_price(
            text_trad, text_promo, wanted_price)
        MessageFunctions.send_email(receiver, better_price)
        print(f"Uma notificação foi enviada via e-mail")

    if message_selection == "2":
        # Cadastro do telegram
        receiver = "+5547999216377"
        print(
            f"\nUma mensagem será enviada para seu telegram quando\no valor do café estiver abaixo de ${wanted_price}")
        better_price = better_price = find_good_price(
            text_trad, text_promo, wanted_price)
        MessageFunctions.send_telegram(receiver, better_price)
        print(f"\nUma notificação foi enviada via e-mail")

    # Cadastro do Whatsapp
    # Cadastro do Twitter

    # Estrutura para usar novamente o programa (ou não)


if __name__ == "__main__":
    main()
