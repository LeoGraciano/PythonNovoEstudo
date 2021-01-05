String = 'Brasil é o pais do futebol, o Brasil é penta'
lista1 = String.replace(',', '').split(' ')
lista2 = String.split(',')


print(lista1)
print(lista2)


for valor in lista1:
    print(f'A palavra {valor} {lista1.count(valor)}x na fase.')

for i, v in enumerate(lista1):
    print(i, v)
