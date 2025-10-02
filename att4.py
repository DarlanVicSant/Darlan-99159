import os
os.system("cls")

vetor = []


print("--- Entrada de Dados ---")

for i in range(5):
    while True:
        try:
      
            numero = float(input(f"Digite o {i+1}º número: "))
 
            vetor.append(numero)
 
            break
        except ValueError:
      
            print("Entrada inválida. Por favor, digite um número.")


quantidade_negativos = 0
soma_positivos = 0

print("\n--- Processamento ---")

for numero in vetor:

    if numero < 0:
        quantidade_negativos += 1  
   
    elif numero > 0:
        soma_positivos += numero  
   


print("\n--- Resultados ---")
print(f"Vetor preenchido: {vetor}")
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
