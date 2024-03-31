import urllib.request
from time import sleep


def open_url(url):
    page = urllib.request.urlopen(url)
    text = page.read().decode("utf8")
    return text


def main():
    url = "http://beans.itcarlow.ie/prices.html"
    text = open_url(url)
    print(text)
    price = ''
    while True:
        inicio = text.find(">$")
        fim = text.find(inicio+4)
        price = int(text[inicio:fim])
        if price <= 4.70:
            print(f"O café está {price} reais. Comprar!")
            break
        else:
            print(f"O café está {price} reais. Não comprar ainda!")
        sleep(2)


if __name__ == "__main__":
    main()
