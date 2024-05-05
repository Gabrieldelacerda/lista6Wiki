def leet_speak(texto):
    texto = texto.upper()
    traducao = {
        'A': '4',
        'E': '3',
        'G': '6',
        'I': '1',
        'O': '0',
        'S': '5',
        'T': '7'
    }
    texto_leet = ''
    for letra in texto:
        if letra in traducao:
            texto_leet += traducao[letra]
        else:
            texto_leet += letra
    return texto_leet

def main():
    texto = input("Digite um texto para traduzir para Leet Speak: ")
    texto_traduzido = leet_speak(texto)
    print("Texto em Leet Speak:", texto_traduzido)

if __name__ == "__main__":
    main()
