import calculadora
import time 
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("[1] Soma")
        print("[2] Subtrair")
        print("[3] Multiplicar")
        print("[0] Sair\n")

        opcao = input("Digite a operação desejada: ")

        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(num1,"+",num2, "= ", calculadora.somar(num1, num2))

        if opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(num1,"-",num2, "= ", calculadora.subtrair(num1, num2))    

        if opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(num1,"x",num2, "= ", calculadora.multiplicar(num1, num2))       
        
        elif opcao == '0':
            print("Encerrando...")
            break
menu()