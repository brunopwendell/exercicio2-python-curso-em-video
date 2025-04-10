num = int(input("Digite um número:"))
escolha = int(input('''Escolha qual será sua conversão
[0] para Binário
[1] para Octal
[2] para Hexadecimal\n'''))
if escolha == 0:
    print("O seu número {} em Binário fica {}".format(num, bin(num)))
elif escolha == 1:
    print("O seu número {} em Octal fica {}".format(num, oct(num)))
elif escolha == 2:
    print("O seu número {} em Hexadecimal {}".format(num, hex(num)))
else:
    print("Erro!")
