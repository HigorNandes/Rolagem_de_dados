import random

continuar = True
while continuar:

    
    dado = input(f'Qual dado você vai rolar? (d20, d12, d10, d8, d6, d4) ')

    resultado = 0

    modificador = input("adicione seus modificadores: ")
    modificador = int(modificador)


    if dado == "d20":
        numb = int(input("Quantos d20 você precisa rolar? "))
        resultados_dados = []
        for i in range(numb):
            d20 = random.randint(1,20)
            resultados_dados.append(d20)
            d20 = int(d20)

        if numb > 1:
            qtd_dados = int(input(f'você quer a \n 1) soma dos dados\n 2) maior dado\n 3) menor dado '))
            if qtd_dados == 1:
                soma = sum(resultados_dados)
                resultado = soma + modificador
                print(f'A soma dos dados é {soma} e com os modificadores é {resultado}')

            elif qtd_dados == 2:
                maior_resultado = max(resultados_dados)
                resultado = maior_resultado + modificador
                if maior_resultado == 20:
                    print(f' Acerto Critco, você tirou {maior_resultado} e com os modificadores ficou {resultado}')
                else:
                    print(f'Você tirou {maior_resultado} e com o modificador ficou {resultado}')

            elif qtd_dados == 3:
                menor_resultado = min(resultados_dados)
                resultado = menor_resultado + modificador
                if menor_resultado == 1:
                    print(f' Erro Critco, você tirou {maior_resultado} e com os modificadores ficou {resultado}')
                else:
                    print(f'Você tirou {menor_resultado} e com o modificador ficou {resultado}')
        else:
            resultado =  d20 + modificador
            if d20 == 20:
                print(f' Acerto Critco, você tirou {d20} e com os modificadores ficou {resultado}')
            elif d20 == 1:
                print(f' Erro Critco, você tirou {d20} e com os modificadores ficou {resultado}')
            else:
                print(f'Você tirou {d20} e com o modificador ficou {resultado}')


        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d12":
        numb = int(input("Quantos d12 você precisa rolar? "))
        resultados_dados = []
        for i in range(numb):
            d12 = random.randint(1,12)
            resultados_dados.append(d12)
            d12 = int(d12)

        if numb > 1:
            qtd_dados = int(input(f'você quer a \n 1) soma dos dados\n 2) maior dado\n 3) menor dado '))
            if qtd_dados == 1:
                soma = sum(resultados_dados)
                resultado = soma + modificador
                print(f'A soma dos dados é {soma} e com os modificadores é {resultado}')

            elif qtd_dados == 2:
                maior_resultado = max(resultados_dados)
                resultado = maior_resultado + modificador
                print(f'Você tirou {maior_resultado} e com o modificador ficou {resultado}')

            elif qtd_dados == 3:
                menor_resultado = min(resultados_dados)
                resultado = menor_resultado + modificador
                print(f'Você tirou {menor_resultado} e com o modificador ficou {resultado}')

        else:
            resultado = d12 + modificador
            print(f'Você tirou {d12} e com os modificadores ficau {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d10":
        numb = int(input("Quantos d10 você precisa rolar? "))
        resultados_dados = []
        for i in range(numb):
            d10 = random.randint(1,10)
            resultados_dados.append(d10)
            d10 = int(d10)

        if numb > 1:
            qtd_dados = int(input(f'você quer a \n 1) soma dos dados\n 2) maior dado\n 3) menor dado '))
            if qtd_dados == 1:
                soma = sum(resultados_dados)
                resultado = soma + modificador
                print(f'A soma dos dados é {soma} e com os modificadores é {resultado}')

            elif qtd_dados == 2:
                maior_resultado = max(resultados_dados)
                resultado = maior_resultado + modificador
                print(f'Você tirou {maior_resultado} e com o modificador ficou {resultado}')

            elif qtd_dados == 3:
                menor_resultado = min(resultados_dados)
                resultado = menor_resultado + modificador
                print(f'Você tirou {menor_resultado} e com o modificador ficou {resultado}')

        else:
            resultado = d10 + modificador
            print(f'Você tirou {d10} e com os modificadores ficau {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d8":
        numb = int(input("Quantos d8 você precisa rolar? "))
        resultados_dados = []
        for i in range(numb):
            d8 = random.randint(1,8)
            resultados_dados.append(d8)
            d8 = int(d8)

        if numb > 1:
            qtd_dados = int(input(f'você quer a \n 1) soma dos dados\n 2) maior dado\n 3) menor dado '))
            if qtd_dados == 1:
                soma = sum(resultados_dados)
                resultado = soma + modificador
                print(f'A soma dos dados é {soma} e com os modificadores é {resultado}')

            elif qtd_dados == 2:
                maior_resultado = max(resultados_dados)
                resultado = maior_resultado + modificador
                print(f'Você tirou {maior_resultado} e com o modificador ficou {resultado}')

            elif qtd_dados == 3:
                menor_resultado = min(resultados_dados)
                resultado = menor_resultado + modificador
                print(f'Você tirou {menor_resultado} e com o modificador ficou {resultado}')

        else:
            resultado = d8 + modificador
            print(f'Você tirou {d8} e com os modificadores ficau {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d6":
        numb = int(input("Quantos d6 você precisa rolar? "))
        resultados_dados = []
        for i in range(numb):
            d6 = random.randint(1,6)
            resultados_dados.append(d6)
            d6 = int(d6)

        if numb > 1:
            qtd_dados = int(input(f'você quer a \n 1) soma dos dados\n 2) maior dado\n 3) menor dado '))
            if qtd_dados == 1:
                soma = sum(resultados_dados)
                resultado = soma + modificador
                print(f'A soma dos dados é {soma} e com os modificadores é {resultado}')

            elif qtd_dados == 2:
                maior_resultado = max(resultados_dados)
                resultado = maior_resultado + modificador
                print(f'Você tirou {maior_resultado} e com o modificador ficou {resultado}')

            elif qtd_dados == 3:
                menor_resultado = min(resultados_dados)
                resultado = menor_resultado + modificador
                print(f'Você tirou {menor_resultado} e com o modificador ficou {resultado}')

        else:
            resultado = d6 + modificador
            print(f'Você tirou {d6} e com os modificadores ficau {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    elif dado == "d4":
        numb = int(input("Quantos d12 você precisa rolar? "))
        resultados_dados = []
        for i in range(numb):
            d4 = random.randint(1,4)
            resultados_dados.append(d4)
            d4 = int(d4)

        if numb > 1:
            qtd_dados = int(input(f'você quer a \n 1) soma dos dados\n 2) maior dado\n 3) menor dado '))
            if qtd_dados == 1:
                soma = sum(resultados_dados)
                resultado = soma + modificador
                print(f'A soma dos dados é {soma} e com os modificadores é {resultado}')

            elif qtd_dados == 2:
                maior_resultado = max(resultados_dados)
                resultado = maior_resultado + modificador
                print(f'Você tirou {maior_resultado} e com o modificador ficou {resultado}')

            elif qtd_dados == 3:
                menor_resultado = min(resultados_dados)
                resultado = menor_resultado + modificador
                print(f'Você tirou {menor_resultado} e com o modificador ficou {resultado}')

        else:
            resultado = d4 + modificador
            print(f'Você tirou {d4} e com os modificadores ficau {resultado}')

        continuar = input("deseja rolar outro dado? (s/n)")

    if continuar.lower() == "n":
        break