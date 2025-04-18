maior = 0
escolhido = ""
soma = 0
mulheres = 0
for i in range(1, 5):
    print("----- {}ª PESSOA -----".format(i))
    nome = input("Digite seu Nome: ").strip()
    idade = int(input("Digite sua Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()
    soma += idade
    if sexo == "F" and idade < 20:
        mulheres += 1
    elif idade > maior:
        maior = idade
        escolhido = nome
media = soma/4
print("A média de idade do Grupo é de {:.2f} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maior, escolhido))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheres))
