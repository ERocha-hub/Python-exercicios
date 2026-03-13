num = int(input("Digite um número: "))
print(f"Analizando o número {num}")
# // divisão inteira pelo numero
# logo 1234 // 100 = 12 e 1234 % 100 = 34
# dessa forma 1234 // 10 = 123 e 1234 % 10 = 4 e 123 % 10 = 3
# como nosso objetivo é apenas um algarismo, sempre buscamos o resto(%) 
# com 10 para achar a unidade do número
# e usamos a // para remover apenas o resto que não queremos(a unidade)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000% 10
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
