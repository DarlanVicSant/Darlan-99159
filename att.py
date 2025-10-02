import os
os.system("cls")

vetor_de_notas = []

print("Solicitando 3 notas. ")
for i in range(3):
    nota = float(input("Digitei uma nota: "))

    vetor_de_notas.append(nota)

print("\nMostrando todas as notas. ")
for i in range(3):
    print(f"Nota: {vetor_de_notas[i]} ")    