#necessário ter um arquivo para abrir a lista de palavras, aqui colocado como 'palavras.txt'.

import random

def carregar_palavras():
    with open("palavras.txt", "r") as file:
        palavras = file.readlines()
    return [palavra.strip().upper() for palavra in palavras]

def escolher_palavra(palavras):
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogar_forca():
    palavras = carregar_palavras()
    palavra_escolhida = escolher_palavra(palavras)
    letras_corretas = set()
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra.")

    while True:
        print("\nPalavra:", mostrar_palavra(palavra_escolhida, letras_corretas))

        if "_" not in mostrar_palavra(palavra_escolhida, letras_corretas):
            print("Parabéns! Você ganhou!")
            break

        letra = input("Digite uma letra: ").strip().upper()

        if letra in palavra_escolhida:
            letras_corretas.add(letra)
        else:
            erros += 1
            print(f"Você errou pela {erros}ª vez.")

        if erros == 6:
            print("Você perdeu! A palavra era:", palavra_escolhida)
            break

if __name__ == "__main__":
    jogar_forca()
