import os
os.system("cls")



def contar_pares_impares():

    numeros = []
 
    pares = 0
    impares = 0
    
    print("--- Entrada de Dados ---")

    for i in range(6):
        while True:
            try:
 
                numero = int(input(f"Digite o {i + 1}º número inteiro: "))
                

                numeros.append(numero)
                
   
                if numero % 2 == 0:
                    pares += 1
                else:
                    impares += 1
                
  
                break
            except ValueError:

                print("Entrada inválida. Por favor, digite um número inteiro válido.")


    print("\n--- Resultados ---")

    print(f"Números informados (Vetor/Lista): {numeros}")
    
  
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")
    


if __name__ == "__main__":
    contar_pares_impares()