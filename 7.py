def contar_caracteres(frase):
    espacos_em_branco = 0
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for caractere in frase:
        if caractere == ' ':
            espacos_em_branco += 1
        elif caractere.lower() in vogais:
            vogais[caractere.lower()] += 1

    return espacos_em_branco, vogais

frase = input("Digite uma frase: ")

espacos, vogais = contar_caracteres(frase)

print("Quantidade de espaços em branco:", espacos)
print("Quantidade de vogais:")
for vogal, quantidade in vogais.items():
    print(f"{vogal}: {quantidade}")