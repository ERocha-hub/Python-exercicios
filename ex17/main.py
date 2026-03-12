cat1 = float(input("Comprimento do cateto oposto: "))
cat2 = float(input("Comprimento do cateto adjacente: "))
hip = (cat1**2 + cat2**2)**(1/2)

print(f"O valor da hipotenusa para os catetos {cat1:.2f} e {cat2:.2f} é {hip:.2f}")
