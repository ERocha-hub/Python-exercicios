
# Table of Contents

1.  [Exercício 4 - Dissecando um valor](#orgb39544e)



<a id="orgb39544e"></a>

# Exercício 4 - Dissecando um valor

    user_value = input("Digite algo: ")
    print(f"O tipo primitivo deste valor é: {type(user_value)}")
    print(f"Só tem espaços? {user_value.isspace()}")
    print(f"É numérico? {user_value.isnumeric()}")
    print(f"É alfabético? {user_value.isalpha()}")
    print(f"É alfanumérico? {user_value.isalnum()}")
    print(f"Está em minusculas? {user_value.islower()}")
    print(f"Está em maiusculas? {user_value.isupper()}")
    print(f"Está capitalizado? {user_value.istitle()}")

