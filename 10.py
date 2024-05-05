def numero_por_extenso(numero):
    unidades = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return especiais[numero - 10]
    else:
        dezena = dezenas[numero // 10]
        unidade = unidades[numero % 10]
        if unidade:
            return f'{dezena} e {unidade}'
        else:
            return dezena

def main():
    while True:
        try:
            numero = int(input("Digite um número entre 0 e 99: "))
            if 0 <= numero <= 99:
                extenso = numero_por_extenso(numero)
                print(f'O número {numero} por extenso é: {extenso}')
                break
            else:
                print("Por favor, digite um número entre 0 e 99.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
