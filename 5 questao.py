#Atividade Pontuada

import os
os.system("cls")
print("5 questao")
print()

operacao = input("Digite a operação (+, -, *, /): ")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
resultado = 0

if operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b
elif operacao == '/':
    if b != 0:
        resultado = a / b
    else:
        print("Erro: Divisão por zero não é permitida.")
     
        resultado = None 
if resultado is not None:
    print(f"O resultado da operação é: {resultado}")