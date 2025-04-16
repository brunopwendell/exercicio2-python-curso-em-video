print("A grande Soma")
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
print("Esse foi o resultado {} da soma de todos os múltiplos de 3 de 1 a 500.".format(soma))
