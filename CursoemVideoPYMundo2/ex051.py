print("Progressão Aritmética")
primeiro_termo = int(input("Digite o 1º termo: "))
razao = int(input("Digite a Razão: "))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo, razao):
    print(i, end=" ")
