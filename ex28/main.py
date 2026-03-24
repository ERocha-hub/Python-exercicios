from random import randint
print(("\033[33m" + "-=-" + "\033[0m") * 20)
print("\033[34m" + "Vou pensar em um número entre 0 e 5. Tente adivinhar..." + "\033[0m")
print(("\033[33m" + "-=-" + "\033[0m") * 20)

num_user = int(input("Em que número eu pensei? "))
num_rand = randint(0,5)
if num_user == num_rand:
    print("\033[32m" + "Parabéns! Você acertou!" + "\033[0m")
else:
    print("\033[31m" + f"Você errou! o número que eu pensei foi {num_rand}" + "\033[0m")
