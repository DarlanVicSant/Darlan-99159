#Atividade Pontuada

import os
os.system("cls")
print("1 questao")

a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))
c = int(input("Digite o valor de c: "))

soma = a + b + c

if a+b < c:
    print(f"A soma de A + B é {soma}.")
else:
    print(f"A soma de A + B é {soma} e é maior que {c}.")



