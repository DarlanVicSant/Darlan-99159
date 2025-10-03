import os
os.system("cls")

def verificar_sinal(valor):

    
    if valor > 0:
        print(f"O número {valor} é POSITIVO.")
    elif valor < 0:
        print(f"O número {valor} é NEGATIVO.")
    else:

        print(f"O número {valor} é ZERO.")



print("--- Teste 1: Positivo ---")
verificar_sinal(10)

print("\n--- Teste 2: Negativo ---")
verificar_sinal(-5)

print("\n--- Teste 3: Zero ---")
verificar_sinal(0)



print("\n--- Teste com Input do Usuário ---")
try:
    
    numero_digitado = int(input("Digite um número inteiro: "))
    
 
    verificar_sinal(numero_digitado)
    
except ValueError:
    print("Entrada inválida. Por favor, digite apenas um número inteiro.")