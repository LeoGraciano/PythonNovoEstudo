while True:
    try:
        cpf = input('Digite seu CPF: ').strip()
        cpf_null = cpf.replace('.', '').replace('-', '')
        if cpf == '0':
            print('Fim do Sistema')
            break
        cpf_chk = cpf_null[:-2]  # Remove 2 últimos Dígitos
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

        sequencia = cpf_chk == str(
            cpf_chk[0]) * len(cpf_null)

        if cpf_null == cpf_chk and not sequencia:
            print('Válido')
            print('Fim do Sistema')
            break
        else:
            print('Inválido')

    except(ValueError, TypeError, KeyboardInterrupt, IndexError):
        print('ERRO!!')
