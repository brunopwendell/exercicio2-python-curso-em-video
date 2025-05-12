n = int(input("Digite um número para saber qual é seu fatorial: "))
c = n - 1
resultado = n
while c > 1:
    resultado *= c
    c -= 1
print(resultado)
