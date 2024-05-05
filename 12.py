def validar_e_corrigir_telefone(telefone):
    telefone = telefone.replace("-", "").replace(" ", "")

    if len(telefone) == 7:
        telefone_corrigido = "3" + telefone
        return telefone_corrigido
    else:
        return telefone

def main():
    telefone = input("Digite o número de telefone: ")
    telefone_corrigido = validar_e_corrigir_telefone(telefone)

    if telefone_corrigido != telefone:
        print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
        print("Telefone corrigido sem formatação:", telefone_corrigido)
        print("Telefone corrigido com formatação:", telefone_corrigido[:4] + "-" + telefone_corrigido[4:])
    else:
        print("Número de telefone válido:", telefone)

if __name__ == "__main__":
    main()
