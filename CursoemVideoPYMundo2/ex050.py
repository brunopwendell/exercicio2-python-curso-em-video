soma = 0
for i in range(1, 7):
    numero = int(input("Digite seu {}º número: ".format(i)))
    if numero % 2 == 0:
        soma += numero
print("Esse foi o resultado {} da soma ds números par digitados".format(soma))