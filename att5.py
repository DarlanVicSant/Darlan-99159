import os
os.system("cls")

def exibir_tabuada(numero):

    
    print(f"\n--- Tabuada do {numero} ---")
    
 
    for i in range(1, 11):

        resultado = numero * i
        
      
        print(f"{numero} x {i} = {resultado}")




while True:
    try:     
        num_usuario = int(input("Digite um número inteiro para ver a tabuada: "))
        break 
    except ValueError:
      
        print("Entrada inválida. Por favor, digite apenas um número inteiro.")

exibir_tabuada(num_usuario)