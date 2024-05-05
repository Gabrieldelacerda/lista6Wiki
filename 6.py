def data_por_extenso(data):
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    dia, mes, ano = map(int, data.split('/'))

    mes_extenso = meses[mes - 1]

    print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

data_por_extenso(data_nascimento)