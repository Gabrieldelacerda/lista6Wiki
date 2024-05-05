def palindromo(frase):
    frase = frase.replace(' ', '').lower()
    return frase == frase [::-1]

def main():
    frase = input("Digite uma frase: ")
    if palindromo(frase):
        print("Palíndromo")
    else:
        print("Não é palíndromo")

if __name__ == "__main__":
    main()
