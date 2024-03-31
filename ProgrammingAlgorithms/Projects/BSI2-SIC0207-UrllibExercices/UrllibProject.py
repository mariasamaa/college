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
from time import sleep
import MessageFunctions  # send messages
import urllib.request  # open URL


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

        site = ""
        # Break while loop when finds a better price
        if price_trad < price_promo:
            if price_trad <= wanted_price:
                better_price = float(price_trad)
                site = "http://beans.itcarlow.ie/prices.html"
                break
        else:
            if price_promo <= wanted_price:
                better_price = float(price_promo)
                site = "http://beans.itcarlow.ie/prices-loyalty.html"
                break

        sleep(10)  # No exercício pede 2 segundos, mas 10 é mais apropriado
    return better_price, site


def main():

    url_trad = "http://beans.itcarlow.ie/prices.html"  # utl preço tradicional
    url_promo = "http://beans.itcarlow.ie/prices-loyalty.html"  # url preço promoção
    text_trad, text_promo = open_url(url_trad, url_promo)

    # preço a ser procurado (estipulado no exercício)
    wanted_price = 4.70

    print("\033[1;31mOlá, funcionário do Starbuzz!\n\033[0;0m")
    print("Com este programa, você pode descobrir o melhor momento")
    print("para comprar grãos de café com nosso principal fornecedor!")
    print("Primeiro precisamos fazer um rápido cadastro!\n")

    # entrada = endereço destinatário do e-mail
    receiver = str(
        input("\033[31mDigite aqui o e-mail do destinatário: \033[0m"))

    print(f"""
    Uma mensagem será enviada para seu e-mail quando
    o valor do café estiver abaixo de ${wanted_price}.
    Por favor, não feche o programa nesse processo.\n""")

    # procurando melhor preço
    better_price, site = find_good_price(
        text_trad, text_promo, wanted_price)

    # enviando a notificação por e-mail
    MessageFunctions.send_email(receiver, better_price, site)
    print(f"Uma notificação foi enviada via e-mail")

    # Estrutura para usar novamente o programa (ou não)
    another_coffe = str(input("""\nGostaria de usar o programa novamente?
    [ 1 ] Sim
    [ 2 ] Não
    Digite aqui: """))

    if another_coffe not in "12":
        while another_coffe not in "12":
            print("Resposta inválida. Digite novamente")
            another_coffe = str(
                input("Digite somente um dos números solicitados: \n"))
    if another_coffe in "1":
        main()
    else:
        print("\n\033[31mObrigado por usar o nosso programa\033[0m")


if __name__ == "__main__":
    main()
