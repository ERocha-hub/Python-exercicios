from math import radians, sin, cos, tan

graus = float(input("Digite um ângulo em graus(º): "))

print(f"O seno de {graus} é {sin(radians(graus)):.2f}")
print(f"O cosseno de {graus} é {cos(radians(graus)):.2f}")
print(f"O tangente de {graus} é {tan(radians(graus)):.2f}")
