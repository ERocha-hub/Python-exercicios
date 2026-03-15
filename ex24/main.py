# Como eu fiz
cid = str(input("Digite a cidade que você nasceu: "))
cid_mod = cid.strip().lower().split()
if cid_mod[0] == "santo":
    print("True")
else:
    print("False")

# Como ele fez
# cid = str(input("Em que cidade você nasceu? ")).strip()
# print(cid[:5].upper() == "SANTO")
