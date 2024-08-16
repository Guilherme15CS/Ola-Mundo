nome = input('Digite seu nome: ')
idade = int(input('Quantos anos você tem? '))
genero = input('Qual é o seu sexo? [M/F]: ').upper()
trabalho = input('Você trabalha? [S/N]: ').upper()
print(f'Que nome bonito o seu {nome}')
if idade == 18:
    if trabalho == 'S':
        print('Meus parábens por começar nessa jornada cedo.')
    else:
        print('Bem é melhor começar a pensar sobre o mais rápido possivel.')
    if genero == 'M':
        print('Você deve se alistar no exército.')
    else: 
        print('Parabéns por se tornar maior de idade, se você quiser você pode se alistar')
elif 18 < idade < 70:
    rest = 70 - idade
    if trabalho == 'S':
        print(f'Continue assim em {rest} anos você se aposenta.')
    else:
        print('Ta esperando o que para procurar um emprego?')
else:
    print('Curta a sua aposentadoria!')
    