from random import randint
print("Jokenpô")
lista = ["PEDRA", "PAPEL", "TESOURA"]
escolha = randint(0, 2)
usuario = int(input('''Digite se você quer 
[0] para Pedra
[1] para Papel
[2] para Tesoura\n'''))
print("="*12)
print("Computador jogou {}".format(lista[escolha]))
print("O jogador jogou {}".format(lista[usuario]))
print("="*12)
if escolha == usuario:
    print("Infelizmente, Empatou")
elif (escolha == 0 and usuario == 2) or (escolha == 1 and usuario == 0) or (escolha == 2 and usuario == 1):
    print("A máquina Venceu!")
elif (usuario == 0 and escolha == 2) or (usuario == 1 and escolha == 0) or (usuario == 2 and escolha == 1):
    print("VOCÊ VENCEU!")
else:
    print("Erro")
