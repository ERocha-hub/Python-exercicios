num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é " + "\033[34m" + "PAR" + "\033[0m" + ".")
else:
    print(f"O número {num} é " + "\033[31m" + "ÍMPAR" + "\033[0m" + ".")
