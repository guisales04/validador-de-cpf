def verify_cpf(cpf: str) -> bool:
    with_pontuations = False

    # Verificando se o CPF possui pontuação ou não
    for i in range(len(cpf) - 1):
        if not cpf[i].isdigit():
            symbols = ['.', '-']
            if cpf[i] in symbols:
                with_pontuations = True
                continue
            else:
                return False

    # Verificando o tamanho do CPF
    if with_pontuations:
        if len(cpf) != 14:
            return False
    elif len(cpf) != 11:
        return False
    return True


def validation(cpf: str) -> bool:
    # Retirando pontuação do CPF
    cpf = ''.join(n for n in cpf if n.isdigit())
    digito1, digito2 = 0, 0

    # Multiplicação dos digitos usando a formula
    for i, r in enumerate(range(10, 1, -1)):
        digito1 += (int(cpf[i]) * r)

    digito1 = 11 - (digito1 % 11)

    if digito1 > 9:
        digito1 = 0

    for i, r in enumerate(range(11, 1, -1)):
        digito2 += (int(cpf[i]) * r)

    digito2 = 11 - (digito2 % 11)

    if digito2 > 9:
        digito2 = 0

    # Criando uma string com o CPF completo junto dos digitos validados
    novo_cpf = cpf[:-2] + str(digito1) + str(digito2)

    # Comparando se o CPF indicado pelo usúario corresponde ao resultado final
    if novo_cpf == cpf:
        if novo_cpf == novo_cpf[0] * 11:
            return False
        else:
            return True
    else:
        return False


cpf = str(input('Digite o número de CPF: '))
verify = verify_cpf(cpf)
while not verify:
    print("""O CPF digitado não corresponde as seguintes regras:
1 - O CPF deve conter 11 digitos.
2 - O CPF não deve conter letras.
3 - Pode ser tanto com pontos como sem ex:
XXX.XXX.XXX-XX ou XXXXXXXXXXX
    """)
    cpf = str(input('Digite o número de CPF: '))
    verify = verify_cpf(cpf)

cpf_validation = validation(cpf)

print('CPF Válido!' if cpf_validation else 'CPF Inválido!')
