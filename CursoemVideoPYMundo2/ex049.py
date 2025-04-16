print("Tabuada no Laço")
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print("{} x {:2} = {}".format(numero, i, (numero*i)))
