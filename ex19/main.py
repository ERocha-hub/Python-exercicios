import random

aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
print(f"O escolhido foi {random.choice(lista)}")

# Outras formas seriam
## random.shuffle(lista) e print(lista[0])
## lista[random.randint(0, 3)]
