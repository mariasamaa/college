# Lista de Exercícios sobre list comprehension do Code Wars
import json

def square_sum(lista):
    # Complete the square sum function so that it squares each
    # number passed into it and then sums the results together
    # Example: sum[1,2,2] = 9 'cause 1^2+2^2+2^2=9.
    soma = 0
    for x in lista:
        soma += x**2
    return soma


def string_cleaning(text):
    # Your boss decided to save money by purchasing some cut-rate
    # optical character recognition software for scanning in the
    # text of old novels to your database. At first it seems to
    # capture words okay, but you quickly notice that it throws
    # in a lot of numbers at random places in the text.

    # Your harried co-workers are looking to you for a solution
    # to take this garbled text and remove all of the numbers. Your
    # program will take in a string and clean out all numeric characters,
    # and return a string with spacing and special characters
    # ~#$%^&!@*():;"'.,? all intact.
    return "".join([c for c in text if c not in "0123456789"])


def convert_numbers(number):
    # Given a random non-negative number, you have to return the
    # digits of this number within an array in reverse order.
    # Example: 35231 => [1,3,2,5,3]
    return [int(n) for n in (str(number))[::-1]]


def out_space(string):
    # Simple, remove the spaces from the string, then return the
    # resultant string.
    return "".join([c for c in string if c not in " "])

def move10(string):
    # Move every letter in the provided string forward 10 letters through the alphabet
    # If it goes past 'z', start again at 'a'.
    # Input will be a string with length > 0.
    return string

def vowel_count(string):
    # Return the number (count) of vowels in the given string.
    # We will consider a, e, i, o, u as vowels for this Kata (but not y).
    # The input string will only consist of lower case letters and/or spaces.
    

    return len([c for c in string if c])

def list_filtering(lista):
    # In this kata you will create a function that takes a list of non-negative
    # integers and strings and returns a new list with the strings filtered out.
    # Example:
    # filter_list([1,2,'a','b']) == [1,2]
    # filter_list([1,'a','b',0,15]) == [1,0,15]
    # filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
    return lista


def count_divisor(number):
    # Count the number of divisors of a positive integer n.
    # Random tests go up to n = 500000.
    # Examples (input --> output)
    # 4 --> 3 (1, 2, 4)
    # 5 --> 2 (1, 5)
    # 12 --> 6 (1, 2, 3, 4, 6, 12)
    # 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
    return number


def descending_order(number):
    # Your task is to make a function that can take any non-negative integer as an argument and
    # return it with its digits in descending order. Essentially, rearrange the digits to create
    # the highest possible number.
    # Examples:
    # Input: 42145 Output: 54421
    # Input: 145263 Output: 654321
    # Input: 123456789 Output: 987654321
    return number


def desemvowel_trolls(string):
    # Trolls are attacking your comment section!
    # A common way to deal with this situation is to remove all of the vowels from the trolls'
    # comments, neutralizing the threat. Your task is to write a function that takes a string
    # and return a new string with all vowels removed. For example, the string "This website is
    # for losers LOL!" would become "Ths wbst s fr lsrs LL!".
    return string


def break_camelcase(string):
    # Complete the solution so that the function will break up camel casing, using a space between words.
    return string


def find_odd(lista):
    # Given an array of integers, find the one that appears an odd number of times.
    # There will always be only one integer that appears an odd number of times.
    return lista


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():

    # lista1 = [1, 2, 2]
    # lista2 = [2, 3, 4]
    # lista3 = [1, 3, 5, 7]
    # lista4 = [1, 2, 5, 10]

    # print("Soma Quadrados")
    # test(square_sum(lista1), 9)
    # test(square_sum(lista2), 29)
    # test(square_sum(lista3), 84)
    # test(square_sum(lista4), 130)

    # print()
    # print("Limpando String")
    # test(string_cleaning("Olá 5mundo!"), "Olá mundo!")
    # test(string_cleaning("Batatinha pegando88 fogo!!!"),
    #      "Batatinha pegando fogo!!!")
    # test(string_cleaning("Flemis? é45 o que é dependendo7 do que seja96"),
    #      "Flemis? é o que é dependendo do que seja")
    # test(string_cleaning("Heavy Metal14 é briga de cachorro7 no microfone1."),
    #      "Heavy Metal é briga de cachorro no microfone.")

    # print()
    # print("Números em listas")
    # test(convert_numbers(15976), [6, 7, 9, 5, 1])
    # test(convert_numbers(89452), [2, 5, 4, 9, 8])
    # test(convert_numbers(0), [0])
    # test(convert_numbers(2), [2])
    # test(convert_numbers(61988), [8, 8, 9, 1, 6])
    # test(convert_numbers(38652018), [8, 1, 0, 2, 5, 6, 8, 3])

    # print()
    # print("Tira espaços")
    # test(out_space("Olá mundo!"), "Olámundo!")
    # test(out_space("Batatinha pegando fogo"), "Batatinhapegandofogo")
    # test(out_space("Flemis é o que é dependendo do que seja"),
    #      "Flemiséoqueédependendodoqueseja")
    # test(out_space("Heavy Metal é briga de cachorro no microfone"),
    #      "HeavyMetalébrigadecachorronomicrofone")

    # print()
    # print("Move 10")
    # # terminar esses testes aqui
    # test(move10("Olá mundo"), "yvk wexny")

    print()
    print("Contador de vogais")
    test(vowel_count("Olá mundo!"), 3)
    test(vowel_count("Batatinha pegando fogo"), 9)
    test(vowel_count("Flemis é o que é dependendo do que seja"), 15)
    test(vowel_count("Heavy Metal é briga de cachorro no microfone"), 16)

    # lista1 = [1, "1", "a", 12, 2, "3"]
    # lista2 = ["b", 3, 4, 5, "5", 7]
    # lista3 = ["1", 0, "3", 4, 5, 6]
    # lista4 = [0, 8, "a", "c", "e", 10]

    # print()
    # print("Filtrando Listas")
    # test(list_filtering(lista1), [1, 2, 3, 12])
    # test(list_filtering(lista2), [3, 4, 5, 7])
    # test(list_filtering(lista3), [0, 1, 3, 4, 5, 6])
    # test(list_filtering(lista4), [0, 8, 10])

    # print()
    # print("Contador de divisores")
    # test(count_divisor(20), 6)
    # test(count_divisor(13), 2)
    # test(count_divisor(589), 4)
    # test(count_divisor(864), 24)
    # test(count_divisor(720), 30)
    # test(count_divisor(128456), 8)

    # print()
    # print("Ordem descendente")
    # test(descending_order(42125), 54421)
    # test(descending_order(145263), 654321)
    # test(descending_order(123456789), 987654321)
    # test(descending_order(2384650), 8654320)
    # test(descending_order(167954), 976541)
    # test(descending_order(789123148655), 988765543211)

    # print()
    # print("Tirando vogais")
    # test(desemvowel_trolls("Olá mundo!"), "l mnd!")
    # test(desemvowel_trolls("Batatinha pegando fogo"), "bttnh pgnd fg")
    # test(desemvowel_trolls("Flemis é o que é dependendo do que seja"),
    #      "flms   q  dpndnd d q sj")
    # test(desemvowel_trolls("Heavy Metal é briga de cachorro no microfone"),
    #      "hvy mtl  brg d cchrr n mcrfn")

    # print()
    # print("Quebrando a CamelCase")
    # test(break_camelcase("Olá Mundo!"), "olá mundo!")
    # test(break_camelcase(" "), " ")
    # test(break_camelcase("Batatinha Pegando Fogo"), "batatinha pegando fogo")
    # test(break_camelcase("Flemis é o que é Dependendo Do que Seja"),
    #      "flemis é o que é dependendo do que seja")
    # test(break_camelcase("Heavy Metal é Briga de Cachorro no Microfone"),
    #      "heavy metal é briga de cachorro no microfone")

    # print()
    # print("Números estranhos")
    # test(find_odd([7]), 7)
    # test(find_odd([0]), 8)
    # test(find_odd([1, 1, 2]), 2)
    # test(find_odd([0, 1, 0, 1, 0]), 0)
    # test(find_odd([1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5,
    #      5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8]), 3)
    # test(find_odd([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]), 1)
    # test(find_odd([2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8]), 6)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
