print("Caixa da Loja")
valor = float(input("Qual o valor do produto: R$ "))
pagamento = input("Qual vai ser a forma de Pagamento: \n'V' À vista Dinheiro e Cheque\n'VC' Á vista no Cartão\n'CC' Cartão de Crédito\n").upper()
vezes = 0
if pagamento == "CC":
    vezes = int(input("De quantas vezes você quer fazer: 1/12"))

    if vezes <= 2:
        parcela = valor / vezes
        print("O valor final fica de R$ {:.2f}, e as parcelas ficaram de {:.2f} no valor de R$ {}".format(valor, vezes, parcela))
    elif 2 < vezes <= 12:
        valor += valor * 0.20
        parcela = valor / vezes
        print("O valor final de R$ {:.2f}, e as parcelas ficaram de {}x no valor de R$ {:.2f}".format(valor, vezes, parcela))
    else:
        print("Erro na digitação do número de parcelas")

elif pagamento == "V":
    valor -= (valor * 0.10)
    print("O valor final fica de R$ {:.2f}".format(valor))

elif pagamento == "VC":
    valor -= (valor * 0.05)
    print("O valor final fica de R$ {:.2f}".format(valor))

else:
    print("Erro na digitação da forma de Pagamento")
