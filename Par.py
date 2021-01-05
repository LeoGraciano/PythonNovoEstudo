while True:
    try:
        n = (input('Digite um numero: ')).strip()
        if int(n) % 2 == 0:
            print(f"Numero {n} é par")
            break
        else:
            print(f"Numero {n} é impar")
            break
    except(ValueError, TypeError):
        print(f"Você digitou o Valor '{n}' não é um Numero inteiro!!")
