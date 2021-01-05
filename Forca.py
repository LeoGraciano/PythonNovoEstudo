secreto = 'perfume'
digitadas = []
chance = 3

while True:
    try:
        if chance <= 0:
            print(f'Você Perdeu!!!!')
            break

        letra = input('Digite uma letra: ')
        if len(letra) > 1:
            print('Ah isso não vale, digite apenas um letra.')
            continue

        digitadas.append(letra)

        if letra in secreto:
            print(f'UHUULL, a letra "{letra}" existe na palavra secreta')
        else:
            print(f'AFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta')
            chance -= 1
            print(f'VOCÊ TEM {chance} chances')
            digitadas.pop()

        secreto_temporário = ""
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporário += letra_secreta
            else:
                secreto_temporário += "*"

        if secreto_temporário == secreto:
            print(
                f'Que legal VOCÊ GANHOU!!!! a palavra secreta era {secreto_temporário}')
            break
        else:
            print(f'A palavra secreta está assim {secreto_temporário}')
    except(ValueError, TypeError, KeyboardInterrupt):
        print('ERRO!!')
        chance -= 1
