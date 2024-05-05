def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto

    return cpf[-2:] == f"{digito_verificador_1}{digito_verificador_2}"

def main():
    cpf = input("Digite o CPF em formato convencional (xxx.xxx.xxx-xx): ")
    if validar_cpf(cpf):
        print("CPF validado")
    else:
        print("CPF inválido")

if __name__ == "__main__":
    main()