print("Progressão Aritmética")
primeiro_termo = int(input("Digite o 1º termo: "))
razao = int(input("Digite a Razão: "))

for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo)
