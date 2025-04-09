from datetime import date
print("Exercito Brasileiro")
ano = int(input("Digite o ano em que você nasceu: "))
data_atual = date.today()
ano_atual = data_atual.year
idade = ano_atual - ano
if idade > 18:
    tempo = idade - 18
    print("Você já passou do tempo de alistamento, pois tem {} de idade. Corre LOGO!".format(idade))
    print("Já se passou {} de tempo".format(tempo))
elif idade == 18:
    print("Você tem que se apresentar agora no alistamento militar, pois já está na idade de {}".format(idade))
else:
    tempo = 18 - idade
    print("Você pode aguardar para o alistamento, pois sua idade de {} ".format(idade))
    print("Ainda falta {} de tempo".format(tempo))
