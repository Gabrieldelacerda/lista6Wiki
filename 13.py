#necessário ter um arquivo para abrir a lista de palavras, aqui colocado como 'palavras.txt'.

import random

def escolher_palavra():
    with open("palavras.txt", "r") as file:
        palavras = file.readlines()
        return random.choice(palavras).strip()

def embaralhar_palavra(palavra):
    letras_embaralhadas = random.sample(palavra, len(palavra))
    return ''.join(letras_embaralhadas)

def main():
    palavra = escolher_palavra()
    palavra_embaralhada = embaralhar_palavra(palavra)
    tentativas = 6

    print("Bem-vindo ao Jogo da Palavra Embaralhada!")
    print("Você tem 6 tentativas para adivinhar a palavra.")

    while tentativas > 0:
        print("\nPalavra embaralhada:", palavra_embaralhada)
        tentativa = input("Digite sua tentativa: ").strip().lower()

        if tentativa == palavra:
            print("Parabéns! Você acertou a palavra:", palavra)
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Você errou! Restam {tentativas} tentativas.")
            else:
                print("Você perdeu! A palavra correta era:", palavra)

if __name__ == "__main__":
    main()
