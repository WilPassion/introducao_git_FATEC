import calculadora
def teste():
    num1 = 1
    num2 = 2

    soma = calculadora.somar(num1, num2)
    subtracao = calculadora.subtrair(num1, num2)

    print("{} + {} = {}".format(num1, num2, soma))
    print("{} - {} = {}".format(num1, num2, subtracao))

teste()