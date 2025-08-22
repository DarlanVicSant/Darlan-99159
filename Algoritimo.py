# Condicionais simples

import os
os.system("cls")

print(f"CALCULO DE ALGORITIMOS:")

numero_A = float(input ("Digite o numero A: "))
print()
numero_B = float(input ("Digite o numero B: "))
print()

print(f"Exibindo resultados: ")
print()

if numero_A > numero_B:
     print("primeiro numero maior que o segundo")
else:
     print("Segundo numero maior que o primeiro")
print()

Alto = numero_A + numero_B
print(f"A Alto valor de {numero_A} e {numero_B} é {Alto}")
print()

menor = numero_A - numero_B
print(f"A menor de {numero_A} por {numero_B} é {menor}")
print()

Produto = numero_A * numero_B
print(f"O Produto de {numero_A} por {numero_B} é {Produto}")
print()
