print("Digite uma quantidade em reais:")
print("(com separação dos centávos por .)")

real = float(input("R$ "))

print(f"Com R${real:.2f} BRL você pode comprar ${real*0.19:.2f} USD.")
