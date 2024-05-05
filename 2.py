def nome_invertido_maiusculo(nome):
    nome = nome.upper()
    nome_invertido = nome[::-1]
    return nome_invertido

nome_usuario = input("Digite seu nome: ")
nome_invertido = nome_invertido_maiusculo(nome_usuario)
print("Nome ao contrário: ", nome_invertido)