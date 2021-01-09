carrinho = []

carrinho.append(('PRODUTO 1', 30))
carrinho.append(('PRODUTO 2', 20))
carrinho.append(('PRODUTO 3', 50))

total = sum((y for x, y in carrinho))


print(total)
