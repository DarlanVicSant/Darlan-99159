#Atividade Pontuada

import os
os.system("cls")
print("2 questao")
print()
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").upper()
estado_civil = input("Digite seu estado civil: ").upper()
tempo_casada = 0

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Há quantos anos você é casada? "))

print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

if tempo_casada > 0:
    print(f"Tempo de casada: {tempo_casada} anos")


