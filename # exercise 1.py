 # exercise 1

import os
os.system("cls")

a = float(input ("Digite o numero A: "))
b = float(input ("Digite o numero B: "))

soma = a + b
print(f"A soma de {a} e {b} é {soma}")


subtracao = a - b
print(f"A subtração de {a} por {b} é {subtracao}")


multiplicacao = a * b
print(f"A multiplicação de {a} por {b} é {multiplicacao}")


divisao = a / b
print(f"A divisão de {a} por {b} é {divisao}")


divisao_inteira = a // b
print(f"A divisão inteira de {a} por {b} é {divisao_inteira}")

resto = a % b
print(f"O resto da divisão de {a} por {b} é {resto}")