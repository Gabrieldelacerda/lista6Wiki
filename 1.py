def comparar_strings(string1, string2):
    print(f"String 1: {string1}\nTamanho de \"{string1}\": {len(string1)} caracteres.")
    print(f"String 2: {string2}\nTamanho de \"{string2}\": {len(string2)} caracteres.")

    if len(string1) == len(string2):
        print("As duas strings têm o mesmo tamanho.")
    else:
        print("As duas strings são de tamanhos diferentes.")

    if string1 == string2:
        print("As duas strings possuem o mesmo conteúdo.")
    else:
        print("As duas strings possuem conteúdo diferente.")

string1 = input("Digite uma string: ")
string2 = input("Digite outra string: ")

comparar_strings(string1, string2)
