print("Compre sua Casa dos Sonhos")
valor_casa = float(input("Digite qual é o valor da casa que você quer: R$"))
salario = float(input("Digite seu salario: R$"))
anos = float(input("Digite em quantos anos você quer pagar ela: "))
mensal = 0
if anos >= 1.0:
    ano = anos * 12
    mensal = valor_casa/ano
    if mensal > (salario * (1 + 30/100)):
        print("Emprestimo Negado!")
        print("Infelizmente sua mensalidade está no valor de R${:.2f} excedeu 30% do seu Salário".format(mensal))
    else:
        print("Emprestimo Aprovado!")
        print("Suas mensalidade estão no valor de R$ {:.2f} ".format(mensal))
        print("De acordo com o tempo escolhido que é de {} meses/anos".format(anos))
else:
    mensal = valor_casa/anos
    if mensal > (salario * (1 + 30 / 100)):
        print("Emprestimo Negado!")
        print("Infelizmente sua mensalidade está no valor de R${:.2f} excedeu 30% do seu Salário".format(mensal))
    else:
        print("Emprestimo Aprovado!")
        print("Suas mensalidade estão no valor de R$ {:.2f} ".format(mensal))
        print("De acordo com o tempo escolhido que é de {} meses/anos".format(anos))
