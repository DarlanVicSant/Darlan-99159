import os
os.system("cls")


soma_das_notas = 0
contador_de_notas = 0

while True:

    resposta = input("Deseja inserir uma nota? (S/N): ").upper()


    if resposta == "N":
        break


    try:
        nota = float(input("Digite a nota: "))
        soma_das_notas += nota
        contador_de_notas += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if contador_de_notas > 0:
    media = soma_das_notas / contador_de_notas
    print(f"\nNotas inseridas: {contador_de_notas}")
    print(f"A média aritmética das notas é: {media:.2f}")
else:
    print("\nNenhuma nota foi inserida.")