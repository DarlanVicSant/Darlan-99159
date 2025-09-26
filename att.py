import os
os.system("cls")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += 1
    soma += nota

    continuar = input("Deseja digitar mais uma nota? Digite S ou N: ").lower()
    if continuar == "n":
        print("Calculando media")
        break 

media = soma / contador

print(f"\nMedia: {media} ")