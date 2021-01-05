v = ['Luis Otávio', 'Joãozinho', 'Maria']

start_in_j = False
for valor in v:
    if valor.lower().startswith('j'):
        start_in_j = True

if start_in_j:
    print('Existe uma palavra que começa com "J".')
else:
    print('Não existe uma palavra que começa com "J"')
