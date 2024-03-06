import calculadora
def teste():
    num1 = 10
    num2 = 5

    soma = calculadora.somar(num1, num2)
    subtracao = calculadora.subtrair(num1, num2)
    multiplicacao = calculadora.multiplicar(num1, num2)
    divisao = calculadora.dividir(num1, num2)

    print("{} + {} = {}".format(num1, num2, soma))
    print("{} - {} = {}".format(num1, num2, subtracao))
    print("{} x {} = {}".format(num1, num2, multiplicacao))
    print("{} / {} = {}".format(num1, num2, divisao))

teste()