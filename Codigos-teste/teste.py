nome = input('Digite seu nome: ')
idade = int(input('Quantos anos você tem? '))
print(f'Que nome bonito o seu {nome}')
if idade >= 18:
    print('Você já é maior de idade.')
    trabalho = input('Você trabalha? [S/N] ').upper()
    if trabalho == 'S':
        print('Meus parabéns')
    else:
        print('Eu acho bom você começar a trabalhar...')
else:
    print('Você ainda é menor de idade.')
