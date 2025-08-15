 # exercise 1

import os
os.system("cls")

a = float(input ("Digite o numero A: "))
print()
b = float(input ("Digite o numero B: "))
print()

print(f"Exibindo resultados: ")
soma = a + b
print(f"A soma de {a} e {b} é {soma}")
print()

subtracao = a - b
print(f"A subtração de {a} por {b} é {subtracao}")
print()

multiplicacao = a * b
print(f"A multiplicação de {a} por {b} é {multiplicacao}")
print()

divisao = a / b
print(f"A divisão de {a} por {b} é {divisao}")
print()

divisao_inteira = a // b
print(f"A divisão inteira de {a} por {b} é {divisao_inteira}")
print()
resto = a % b
print(f"O resto da divisão de {a} por {b} é {resto}")
print()