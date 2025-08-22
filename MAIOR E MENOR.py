# Condicionais simples

import os
os.system("cls")

print(f"Suas Medias:")

nota = float(input ("Digite a primeira nota "))
print()
nota = float(input ("Digite a segunda nota "))
print()

print(f"Exibindo resultados: ")


media = (nota + nota) / 2

if media >= 7:
     print(f"A media é {media}. aprovado")  
else:
     print(f"A media é {media}. reprovado")
print("Fim")