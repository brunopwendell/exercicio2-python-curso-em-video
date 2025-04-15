print("É Primo?")
vezes = int(input("Quantas tentativas você quer fazer: "))

for i in range(0, vezes):
    numero = int(input("Digite um número: "))
    if numero <= 1:
        print("Seu número não é primo")
    else:
        e_primo = True
        for n in range(2, numero):
            if numero % n == 0:
                e_primo = False
                break
        if e_primo:
            print("Seu número é Primo")
        else:
            print("Seu número não é Primo")


