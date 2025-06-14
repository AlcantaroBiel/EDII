v = float(input())

if v < 0 or v > 1000000:
    print('Valor inválido')
else:
    v = int(round(v * 100))  # Multiplica por 100 para evitar problemas de precisão

    # Notas
    n100 = v // 10000
    v %= 10000

    n50 = v // 5000
    v %= 5000

    n20 = v // 2000
    v %= 2000

    n10 = v // 1000
    v %= 1000

    n5 = v // 500
    v %= 500

    n2 = v // 200
    v %= 200

    # Moedas
    m1 = v // 100
    v %= 100

    m05 = v // 50
    v %= 50

    m02 = v // 25
    v %= 25

    m01 = v // 10
    v %= 10

    m005 = v // 5
    v %= 5

    m001 = v // 1

    print('NOTAS:')
    print(f'{n100} nota(s) de R$ 100.00')
    print(f'{n50} nota(s) de R$ 50.00')
    print(f'{n20} nota(s) de R$ 20.00')
    print(f'{n10} nota(s) de R$ 10.00')
    print(f'{n5} nota(s) de R$ 5.00')
    print(f'{n2} nota(s) de R$ 2.00')

    print('MOEDAS:')
    print(f'{m1} moeda(s) de R$ 1.00')
    print(f'{m05} moeda(s) de R$ 0.50')
    print(f'{m02} moeda(s) de R$ 0.25')
    print(f'{m01} moeda(s) de R$ 0.10')
    print(f'{m005} moeda(s) de R$ 0.05')
    print(f'{m001} moeda(s) de R$ 0.01')