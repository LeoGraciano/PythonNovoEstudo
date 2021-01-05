from random import randint

try:
    n = str(randint(000000000, 999999999))
    cpf_chk = n
    reverso = 10  # Conta o reverso
    total = 0
    for index in range(19):
        if index > 8:  # Primeiro Indice vai de 0 a 9,
            index -= 9  # São os 9 primeiros dígitos do CPF

        # Valor total da Multiplicação
        total += int(cpf_chk[index]) * reverso

        reverso -= 1  # Decrementa o contator reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0  # Zera Total
            cpf_chk += str(d)
    print(cpf_chk[:3]+'.'+cpf_chk[3:6]+'.'+cpf_chk[6:9]+'-'+cpf_chk[9:11])

except(ValueError, TypeError, KeyboardInterrupt, IndexError):
    print('ERRO!!')
