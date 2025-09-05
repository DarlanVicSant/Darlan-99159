#Atividade Pontuada

import os
os.system("cls")
print("7 questao")
print()

celular = int(input("Digite qual celular quer  "))
quantidade = int(input("Digite a quantos celulares deseja:  "))
preço = float(input("Digite o valor do produto: "))

total = quantidade * preço

if quantidade <=5:
    desconto = total * 0.02
elif 6 <= quantidade <= 10:
    desconto = total * 0.03
else: 
    desconto = total * 0.05

total_pagar = total - desconto

print(f"celular: {celular}")
print(f"Total sem desconto: R$ {total: .2f}")
print(f"Desconto: R$ {desconto: .2f}")
print(f"Total a pagar: R$ {total_pagar: .2f}")