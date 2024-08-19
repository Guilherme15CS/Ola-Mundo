from math import sqrt
verde = '\033[1;32m'
vermelho = '\033[1;31m'
fim = '\033[m'
a = int(input(f'Digite o "A" da equação: (\033[1mSEM O SINAL{fim}) '))
b = int(input(f'Digite o "B" da equação: (\033[1mSEM O SINAL{fim}) '))
c = int(input(f'Digite o "C" da equação: (\033[1mSEM O SINAL{fim}) '))
print(f'''Qual dessas maneiras a equação se dá: 
      [1] {a}x² {verde}+{fim} {b}x {verde}+{fim} {c} = 0
      [2] {a}x² {verde}+{fim} {b}x {vermelho}-{fim} {c} = 0
      [3] {a}x² {vermelho}-{fim} {b}x {vermelho}-{fim} {c} = 0
      [4] {a}x² {vermelho}-{fim} {b}x {verde}+{fim} {c} = 0''')
opc = int(input('Qual forma deseja utilizar: '))
if opc == 1:
       print(f'{a}x² + {b}x + {c} = 0')
       delta = (+b ** 2) - 4 * (a * +c)
elif opc == 2:
       print(f'{a}x² + {b}x - {c} = 0')
       delta = (b ** 2) - 4 * (a * -c)
elif opc == 3:
        print(f'{a}x² - {b}x - {c} = 0')
        delta = (-b ** 2) - 4 * (a * -c)
elif opc == 4:
        print(f'{a}x² - {b}x - {c} = 0')
        delta = (-b ** 2) - 4 * (a * +c)
print(f'Delta vale {delta}')
if delta < 0:
    print('Não existe raiz real para essa equação')
elif delta > 0:
        x1 = (-b + sqrt(delta)) / (a * 2)
        print(f'O valor de x1 é {x1}')
        x2 = (-b - sqrt(delta)) / (a * 2)
        print(f'O valor de x2 é {x2}')
elif delta == 0:
        x = (-b + 0) / (a * 2)
        print(f'Como delta é zero o valor de x é {x}')
