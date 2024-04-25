import random

continuar = True
while continuar:

    
    dado = input(f'Qual dado você vai rolar? (d20, d12, d10, d8, d6, d4) ')

    resultado = 0

    modificador = input("adicione seus modificadores: ")
    modificador = int(modificador)


    if dado == "d20":
        d20 = random.randint(1,20)
        d20 = int(d20)
        resultado = int(d20 + modificador)

        if d20 == 20:
            print(f'Acerto critico você tirou {d20} e com seus modificadores o resultado é: {resultado}')

        elif d20 == 1:
            print(f'Erro critico, você tirou {d20} e o com seus modificadores o resultado é: {resultado}')

        else:
            print(f'você tirou {d20} e o com seus modificadores o resultado é: {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d12":
        d12 = random.randint(1,12)
        d12 = int(d12)
        resultado = int(d12 + modificador)
        print(f'você tirou {d12} e o com seus modificadores o resultado é: {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d10":
        d10 = random.randint(1,10)
        d10 = int(d10)
        resultado = int(d10 + modificador)
        print(f'você tirou {d10} e o com seus modificadores o resultado é: {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d8":
        d8 = random.randint(1,8)
        d8 = int(d8)
        resultado = int(d8 + modificador)
        print(f'você tirou {d8} e o com seus modificadores o resultado é: {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d6":
        d6 = random.randint(1,6)
        d6 = int(d6)
        resultado = int(d6 + modificador)
        print(f'você tirou {d6} e o com seus modificadores o resultado é: {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d4":
        d4 = random.randint(1,4)
        d4 = int(d4)
        resultado = int(d4 + modificador)
        print(f'você tirou {d4} e o com seus modificadores o resultado é: {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    if continuar.lower() == "n":
        break