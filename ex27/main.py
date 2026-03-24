nome = str(input("Digite seu nome completo: ")).strip().split()

print(f"Muito prazer em te conhecer, {nome[0].capitalize()}!")
print(f"Seu primeiro nome é {nome[0].capitalize()}.")
print(f"Seu último nome é {nome[-1].capitalize()}.")
