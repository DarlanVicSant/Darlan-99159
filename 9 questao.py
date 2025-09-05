#Atividade Pontuada

import os
os.system("cls")
print("9 questao")
print()

renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
prestacao = float(input("Digite o valor da prestaçao: "))

if emprestimo <= renda * 10 and prestacao <= renda * 0.3: print("Emprestimo concedido!")
else: 
    print("Emprestimo negado")