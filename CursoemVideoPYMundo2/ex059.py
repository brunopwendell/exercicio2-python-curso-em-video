resultado = maior = escolha = 0
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

while escolha != 5:
    print("[1] para Soma")
    print("[2] para multiplicar")
    print("[3] para saber o Maior")
    print("[4] para Novos Números")
    print("[5] para Sair")
    escolha = int(input("Digite sua opção: "))
    if escolha == 1:
        resultado = n1 + n2
        print("O resultado de sua soma foi {:.2f}".format(resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print("O resultado de sua multiplicação foi {:.2f}".format(resultado))
    elif escolha == 3:
        if n1 < n2:
            maior = n2
            print("O resultado do maior é {}".format(maior))
        else:
            maior = n1
            print("O resultado do maior é {}".format(maior))
    elif escolha == 4:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
    elif escolha == 5:
        print("Finalizando o programa...")
    else:
        print("Opção Inválida, tente novamente.")
print("Finalizado")
