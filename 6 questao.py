#Atividade Pontuada

import os
os.system("cls")
print("6 questao")
print()

nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"


if conceito in ["A", "B", "C"]:
    status = "Aprovado"
else:
    status = "Reprovado"


print(f"\n--- Resultado para {nome_aluno} ---")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")