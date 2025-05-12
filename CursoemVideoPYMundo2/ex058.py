from random import randint
sorteado = randint(0, 10)
usuario = int(input("Digite o seu número: "))
tentativas = 1
while sorteado != usuario:
    print("Você errou! tente novamente")
    tentativas += 1
    usuario = int(input("Digite o seu número: "))
print("Você acertou! com {} tentativas".format(tentativas))
