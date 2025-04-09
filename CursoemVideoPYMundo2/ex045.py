from random import choice
print("Jokenpô")
lista = ["PEDRA", "PAPEL", "TESOURA"]
escolha = choice(lista)
usuario = input("Digite se você quer Pedra/Papel/Tesoura: ").strip().upper()
if escolha == usuario:
    print("Infelizmente, Empatou")
elif (escolha == "PEDRA" and usuario == "TESOURA") or (escolha == "PAPEL" and usuario == "PEDRA") or (escolha == "TESOURA" and usuario == "PAPEL"):
    print("A máquina Venceu!")
elif (usuario == "PEDRA" and escolha == "TESOURA") or (usuario == "PAPEL" and escolha == "PEDRA") or (usuario == "TESOURA" and escolha == "PAPEL"):
    print("VOCÊ VENCEU!")
else:
    print("Erro")
