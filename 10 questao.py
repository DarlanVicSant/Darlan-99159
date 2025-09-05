#Atividade Pontuada

import os
os.system("cls")
print("10 questao")
print()

Litros = int(input("Digite quantos litros deseja:  "))
Tipo_combustivel = input("Digite o Tipo de combustível (A-álcool, G-gasolina): ").upper()

Al = 3,79
Gasolina = 6,59

valor_a_pagar = 0.0

if Tipo_combustivel == 'A':
     valor_a_pagar = Litros * Al
elif Tipo_combustivel == 'G':
    valor_a_pagar = Litros * Gasolina
else:
   print("Não temos esse combustivel somente A e G.")

if  valor_a_pagar > 0:
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")