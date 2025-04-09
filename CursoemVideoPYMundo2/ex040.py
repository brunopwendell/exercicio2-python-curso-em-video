print("Notas")
matematica = float(input("Digite sua nota em Matemática: "))
portugues = float(input("Digite sua nota em Português: "))
media = (matematica+portugues) / 2
if media < 5.0:
    print("Devido a sua Média de {}, está Reprovado".format(media))
elif media >= 5.0 and media < 6.9:
    print("Devido a sua Média de {}, está de Recuperação".format(media))
else:
    print("Devido a sua Média de {}, está Aprovado".format(media))
