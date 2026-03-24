vel = int(input("Qual a velocidade atual do carro? "))

if vel > 80:
    print("\033[31m" + "MULTADO! Você excedeu o limete de velocidade de 80km/h" + "\033[0m")
    print("\033[31m" + "Você deve pagar uma multa de " + "\033[0m"+ "\033[33m" + f"R${(vel-80)*7:.2f}!"+ "\033[0m")

print("\033[33m" + "Tenha um bom dia, dirija com segurança!" + "\033[0m")
