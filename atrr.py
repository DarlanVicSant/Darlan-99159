import os
os.system("cls")

soma = 0
contador = 0

print("Digite valores inteiros positivos para calcular a média.")
print("Para parar, digite um valor negativo.")


while True:
    try:
  
        numero = int(input("Digite um número: "))


        if numero < 0:
            break

        soma += numero
        contador += 1
        
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if contador > 0:
    media = soma / contador
    print(f"\nVocê digitou {contador} números positivos.")
    print(f"A média aritmética dos números é: {media:.2f}")
else:
    print("\nNenhum número positivo foi inserido.")