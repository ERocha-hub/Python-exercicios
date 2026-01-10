
# Table of Contents

1.  [Exercício 4 - Dissecando um valor](#orgba488d7)



<a id="orgba488d7"></a>

# Exercício 4 - Dissecando um valor

Expressa as seguintes caracteristicas de um input do usuário:

-   tipo primitivo;
-   Testes lógicos de:
    -   ser exlusicamente espaços,
    -   ser numérico,
    -   ser alfabético,
    -   ser alfanumérico,
    -   ser exlusicamente minusculas,
    -   ser exlusicamente maiusculas e
    -   estar captalizado(primeira letra maiuscula e demais minusculas).

    user_value = input("Digite algo: ")
    print(f"O tipo primitivo deste valor é: {type(user_value)}")
    print(f"Só tem espaços? {user_value.isspace()}")
    print(f"É numérico? {user_value.isnumeric()}")
    print(f"É alfabético? {user_value.isalpha()}")
    print(f"É alfanumérico? {user_value.isalnum()}")
    print(f"Está em minusculas? {user_value.islower()}")
    print(f"Está em maiusculas? {user_value.isupper()}")
    print(f"Está capitalizado? {user_value.istitle()}")

