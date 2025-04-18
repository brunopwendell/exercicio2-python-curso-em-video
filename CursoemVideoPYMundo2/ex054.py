from datetime import datetime
lista = []
ano = datetime.now().year
maior_idade = 0
menor_idade = 0
for i in range(1, 8):
    pessoa = int(input("Digite seu Ano {}º de Nascimento: ".format(i)))
    lista.append(pessoa)
    data = ano - pessoa
    if data >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print("Foram {} pessoas menor de idade e maior foram {}".format(menor_idade, maior_idade))
