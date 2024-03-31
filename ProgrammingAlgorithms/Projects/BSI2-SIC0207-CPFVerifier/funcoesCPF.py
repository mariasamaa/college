import random
# Funções com testes de validação de CPF

def bruto_dv1(cpf):
    # informa valor bruto da fórmula de verificação do primeiro dígito verificador
    return sum([i*int(d) for i, d in enumerate((cpf+"00")[::-1])])


def valida_dv1(cpf):
    # informa o valor do primeiro dígito verificador
    return (bruto_dv1(cpf)*10) % 11 if (bruto_dv1(cpf)*10) % 11 < 10 else 0


def bruto_dv2(cpf):
    # informa o valor bruto da fórmula de verificação do segundo dígito verificador
    return sum([i*int(d) for i, d in enumerate((cpf+"000")[::-1])])


def valida_dv2(cpf):
    # informa o valor do segundo dígito verificador
    return ((valida_dv1(cpf)*2 + bruto_dv2(cpf))*10) % 11 if (bruto_dv2(cpf)*10) % 11 < 10 else 0


def test_dv_completo(cpf):
    # devolve os dois dígitos verificadores de uma sequência de 9 dígitos
    return f"{valida_dv1(cpf)}{valida_dv2(cpf)}"


def tira_mascara_cpf(cpf):
    # exclui caracteres que formam a máscara do CPF, se houver
    return "".join([num for num in cpf if num not in ".-"])


def coloca_mascara_cpf(cpf):
    # inclui caracteres que formam a máscara do CPF, se houver
    cpf = tira_mascara_cpf(cpf)
    return (f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")


def numeros_iguais(cpf):
    # um cpf não pode ter todos os numeros iguais, ainda que seja "válido"
    return False if len(set(cpf)) == 1 else True


def test_cpf_completo(cpf):
    # verifica se o valor inteiro do cpf está completo (testes com o dígito verificador)
    cpf_teste = tira_mascara_cpf(cpf)[:9]
    dv_teste = test_dv_completo(cpf_teste)
    return cpf_teste+dv_teste == tira_mascara_cpf(cpf) if numeros_iguais(cpf) == True else False


def main():

    print("\n\033[35m- - - ÁREA DE TESTES - - -\033[0m")

    """Obtem o resultado da soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro)."""
    assert bruto_dv1("398136146") == 258
    assert bruto_dv1("123456789") == 210

    """Calcula o DV1 do CPF"""
    assert valida_dv1("398136146") == 6
    assert valida_dv1("123456789") == 0

    """Obtem o resultado da soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa."""
    assert bruto_dv2("398136146") == 299
    assert bruto_dv2("123456789") == 255

    """Calcula o DV2 do CPF"""
    assert valida_dv2("398136146") == 8
    assert valida_dv2("123456789") == 9

    """Calcula o DV final do CPF"""
    assert test_dv_completo("398136146") == "68"
    assert test_dv_completo("123456789") == "09"
    assert test_dv_completo("054269962") == "10"

    """Tira a máscara do CPF, se houver"""
    assert tira_mascara_cpf("398.136.146-68") == "39813614668"
    assert tira_mascara_cpf("123.456.789-09") == "12345678909"
    assert tira_mascara_cpf("12345678909") == "12345678909"

    """Coloca a máscara no CPF, se não houver"""
    assert coloca_mascara_cpf("39813614668") == "398.136.146-68"
    assert coloca_mascara_cpf("12345678909") == "123.456.789-09"
    assert coloca_mascara_cpf("123.456.789-09") == "123.456.789-09"

    """Verifica validade do CPF com numeros iguais"""
    assert numeros_iguais("11111111111") == False
    assert numeros_iguais("12345678909") == True
    assert numeros_iguais("22222222222") == False
    assert numeros_iguais("99999999999") == False

    """Verifica se o CPF está correto"""
    assert test_cpf_completo("398.136.146-68") == True
    assert test_cpf_completo("123.456.789-09") == True
    assert test_cpf_completo("740.637.299-07") == True
    assert test_cpf_completo("054.269.962-10") == True
    assert test_cpf_completo("123.456.789-25") == False
    assert test_cpf_completo("198.735.486-74") == False


if __name__ == "__main__":
    main()
