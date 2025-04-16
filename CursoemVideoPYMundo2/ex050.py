soma = 0
par = 0
for i in range(1, 7):
    numero = int(input("Digite seu {}º número: ".format(i)))
    if numero % 2 == 0:
        soma += numero
        par += 1
print("Foram {} numeros pares e o resultado foi {}".format(par, soma))