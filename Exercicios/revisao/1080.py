v = int(input())
valor = v

if(v < 0 and v > 1000000):
    print('Valor inválido')

n100 = v // 100
v = v - n100*100

n50 = v // 50
v = v - n50*50

n20 = v // 20
v = v - n20*20

n10 = v // 10
v = v - n10*10

n5 = v // 5
v = v - n5*5 

n2 = v // 2
v = v - n2*2

n1 = v // 1
v = v - n1*1

print(valor)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')