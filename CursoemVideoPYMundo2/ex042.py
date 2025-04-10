print("Triângulo")
c1 = float(input("Digite o 1° comprimento: "))
c2 = float(input("Digite o 2° comprimento: "))
c3 = float(input("Digite o 3° comprimento: "))
if (c1 + c2 > c3) and (c1 + c3 >c2) and (c2 + c3 > c1):
    if c1 == c2 == c3:
        print("Você conseguiu fazer um Triângulo Equilátero.")
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print("Você conseguiu fazer um Triângulo Isósceles.")
    else:
        print("Você conseguiu fazer um Triângulo Escaleno.")
else:
    print("Infelizmente, não é possível fazer um Triângulo.")
