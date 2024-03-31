from pathlib import Path
from operator import itemgetter
import matplotlib.pyplot as matlib
import numpy as np


def txt_pt():
    print("\033[1;34mPercy Jackson e os Olimpianos: Português")
    percy_pt = Path(__file__).resolve().parent
    with open(f'{percy_pt}/percy-jackson-pt.txt', encoding='utf-8') as file:
        pjo_pt = file.read().lower()
    print(f"\033[0;34mTexto sem formatação")
    print(f"\033[0;0m{len(pjo_pt)} caracteres carregados\n")

    # Limpando string (retirar caracteres especiais)
    pjo_pt_sem_ponto = ""
    for caracter in pjo_pt:
        if caracter.isalpha() and caracter not in "ǁº":
            pjo_pt_sem_ponto += caracter

    # Padronizando string em formato lower sem acentos
    pjo_pt_sem_ponto.lower()
    padrao_acento = {
        "à": "a",
        "á": "a",
        "â": "a",
        "ã": "a",
        "è": "e",
        "é": "e",
        "ê": "e",
        "ì": "i",
        "í": "i",
        "î": "i",
        "ò": "o",
        "ó": "o",
        "õ": "o",
        "ô": "o",
        "ù": "u",
        "ú": "u",
        "û": "u",
        "ü": "u"
    }

    pjo_pt_padrao = ""
    for caracter in pjo_pt_sem_ponto:
        if caracter in "àáãâèéêìíîòóôõùúûü":
            caracter = padrao_acento[caracter]
        pjo_pt_padrao += caracter
    print("\033[0;34mTexto sem caracteres especiais")
    print(f"\033[0;0m{len(pjo_pt_sem_ponto)} caracteres carregados\n")

    # Verificando quantidade de letras aparentes (max=27)
    frequencia_letras_pjo_pt = {}
    for letra in pjo_pt_padrao:
        frequencia_letras_pjo_pt[letra] = frequencia_letras_pjo_pt.get(
            letra, 0) + 1
    print("\033[0;34mFrequência de letras no texto")
    print(
        f'\033[0;0m{len(frequencia_letras_pjo_pt)} letras unicas carregadas\n')

    # Encontrando as letras mais comuns
    top_letras_pjo_pt = sorted(
        frequencia_letras_pjo_pt.items(), key=itemgetter(1), reverse=True)
    print("\033[0;34mTop letras que mais aparecem no texto")
    top_letras = []
    top_quqnatidade = []
    for letra, quantidade in top_letras_pjo_pt[:10]:
        top_letras.append(letra)
        top_quqnatidade.append(quantidade)
    return top_letras, top_quqnatidade


def txt_es():
    print("\033[1;33mPercy Jackson e os Olimpianos: Espanhol")
    percy_es = Path(__file__).resolve().parent
    with open(f'{percy_es}/percy-jackson-es.txt', encoding='utf-8') as file:
        pjo_es = file.read().lower()
    print(f"\033[0;33mTexto sem formatação")
    print(f"\033[0;0m{len(pjo_es)} caracteres carregados\n")

    # Limpando string (retirar caracteres especiais)
    pjo_es_sem_ponto = ""
    for caracter in pjo_es:
        if caracter.isalpha() and caracter not in "ǁº":
            pjo_es_sem_ponto += caracter

    # Padronizando string em formato lower sem acentos
    pjo_es_sem_ponto.lower()
    padrao_acento = {
        "à": "a",
        "á": "a",
        "â": "a",
        "ã": "a",
        "è": "e",
        "é": "e",
        "ê": "e",
        "ì": "i",
        "í": "i",
        "î": "i",
        "ò": "o",
        "ó": "o",
        "õ": "o",
        "ô": "o",
        "ù": "u",
        "ú": "u",
        "û": "u",
        "ü": "u"
    }

    pjo_es_padrao = ""
    for caracter in pjo_es_sem_ponto:
        if caracter in "àáãâèéêìíîòóôõùúûü":
            caracter = padrao_acento[caracter]
        pjo_es_padrao += caracter
    print("\033[0;33mTexto sem caracteres especiais")
    print(f"\033[0;0m{len(pjo_es_sem_ponto)} caracteres carregados\n")

    # Verificando quantidade de letras aparentes (max=27)
    frequencia_letras_pjo_es = {}
    for letra in pjo_es_padrao:
        frequencia_letras_pjo_es[letra] = frequencia_letras_pjo_es.get(
            letra, 0) + 1
    print("\033[0;33mFrequência de letras no texto")
    print(
        f'\033[0;0m{len(frequencia_letras_pjo_es)} letras unicas carregadas\n')

    # Encontrando as letras mais comuns
    top_letras_pjo_es = sorted(
        frequencia_letras_pjo_es.items(), key=itemgetter(1), reverse=True)
    print("\033[0;33mTop letras que mais aparecem no texto")
    top_letras = []
    top_quqnatidade = []
    for letra, quantidade in top_letras_pjo_es[:10]:
        top_letras.append(letra)
        top_quqnatidade.append(quantidade)
    return top_letras, top_quqnatidade


def main():

    top_pt, top_quant_pt = txt_pt()
    print(f"\033[0;0m{dict(zip(top_pt,top_quant_pt))}\n")
    top_es, top_quant_es = txt_es()
    print(f"\033[0;0m{dict(zip(top_es,top_quant_es))}")

    # Configurando larguras das barras/gráfico
    bar_width = 0.25
    matlib.figure(figsize=(10, 5))

    # Definindo posição das barras
    r1 = np.arrange(len(top_quant_pt))
    r2 = [x + bar_width for x in r1]

    matlib.bar(r1, top_quant_es, color="#FFFF00",
               width=bar_width, label="Espanhol")
    matlib.bar(r2, top_quant_pt, color="#00CED1",
               width=bar_width, label="Português")

    matlib.title(
        "Comparação de letras mais frequentes em\nPercy Jackson e os Olimpianos: o Ladrão de Raios")
    matlib.xlabel("Letras")
    matlib.xticks([r + bar_width for r in range(len(top_quant_pt))], top_pt)
    matlib.ylabel("Frequência")
    matlib.legend()
    matlib.show()


if __name__ == "__main__":
    main()
