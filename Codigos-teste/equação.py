from math import sqrt
a = int(input('Digite o a da equação: '))
b = int(input('Digite o b da equação: '))
c = int(input('Digite o c da equação: '))
print(f'{a}x² + {b}x + {c} = 0')
delta = (b ** 2) - 4 * (a * c)
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
