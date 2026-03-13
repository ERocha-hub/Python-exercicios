nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome...")
print(f"Seu nome em maiusculas é: {nome.upper()}")
print(f"Seu nome em minusculas é: {nome.lower()}")
# A função abaixo ele fez assim:
# print(f"A quantidade de letras no seu nome é: {len(nome) - nome.count(' ')}")
print(f"A quantidade de letras no seu nome é: {len(nome.replace(' ', ''))}")
print(f"A quantidade de letras no seu primeiro nome é: {len(nome.split()[0])}")
