from datetime import date
print("Confederação Nacional de Natação")
ano_nascimento = int(input("Digite o Ano em que você nasceu: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print("Você pode participar da Categoria Mirim")
elif 9 > idade <= 14:
    print("Você pode participar da Categoria Infantil")
elif 14 > idade <= 19:
    print("VocÊ pode participar da Categoria Junior")
elif idade == 20:
    print("Você pode participar da Categoria Sênior")
else:
    print("Você pode participar da Categoria Master")
