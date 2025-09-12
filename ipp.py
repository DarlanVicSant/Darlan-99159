import os
os.system("cls")


print("Laço de reipitçao - while")



QUANTIDADE_NOTAS = 2
soma = 0

for i in range("QUANTIDADE_NOTAS"):
    while True:
        nota = int(input(f"Digite a {i+1}nota: "))
        if nota >= 0 and nota <= 10: 
            break
else: 
    media =  soma = soma + QUANTIDADE_NOTAS

print(f"media = {media}")