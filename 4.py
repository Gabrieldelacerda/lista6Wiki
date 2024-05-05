def imprimir_escada(nome):
    nome_formatado = ""
    for letra in nome:
        nome_formatado += letra
        print(nome_formatado)

nome_usuario = input("Digite seu nome: ")
imprimir_escada(nome_usuario)