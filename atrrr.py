import os
os.system("cls")


contador_pares = 0
soma_pares = 0
contador_impares = 0
soma_total = 0
total_numeros_lidos = 0

print("Digite números inteiros positivos. A leitura será encerrada ao digitar o número 0.")

while True:
    try:

        numero = int(input("Digite um número: "))
 
        if numero == 0:
            break
        
     
        if numero > 0:

            total_numeros_lidos += 1
    
            soma_total += numero
    
            if numero % 2 == 0:
                contador_pares += 1
                soma_pares += numero
            else:

                contador_impares += 1
        else:
            print("Por favor, digite apenas números positivos.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n--- Resultados ---")


print(f"Quantidade de números pares: {contador_pares}")
print(f"Quantidade de números ímpares: {contador_impares}")


if contador_pares > 0:
    media_pares = soma_pares / contador_pares
    print(f"Média dos valores pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi inserido, portanto, não é possível calcular a média de pares.")

if total_numeros_lidos > 0:
    media_geral = soma_total / total_numeros_lidos
    print(f"Média geral dos números lidos: {media_geral:.2f}")
else:
    print("Nenhum número foi inserido, portanto, não é possível calcular a média geral.")