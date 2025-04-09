print("IMC")
altura = float(input("Digite a sua Altura: "))
peso = float(input("Digite o seu Peso: "))
imc = peso/ (altura * altura)
if imc < 18.5:
    print("O seu IMC é de {}, isto é, está Abaixo do Peso".format(imc))
elif 18.5 <= imc < 25:
    print("O seu IMC é de {}, isto é, está no Peso Ideal".format(imc))
elif 25 <= imc < 30:
    print("O seu IMC é de {}, isto é, está Sobrepeso".format(imc))
elif 30 <= imc < 40:
    print("O seu IMC é de {}, isto é, está com Obesidade".format(imc))
else:
    print("O seu IMC é de {}, isto é, está com Obesidade Mórbida".format(imc))
