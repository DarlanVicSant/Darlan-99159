import os
os.system("cls")



def sistema_pedidos_restaurante():

    
  
    MENU = {
        6: ["Picanha", 25.00],
        7: ["Lasanha", 20.99],
        8: ["Strogonoff", 18.00],
        9: ["Bife Acebolado", 15.00],
        5: ["Pão com ovo", 5.00]
    }
    
    
    pedidos = []
    
    print("=========================================")
    print("          Bem-vindo ao Restaurante       ")
    print("=========================================")
   
    print("CÓDIGO | PRATO            | PREÇO")
    print("-------|------------------|-------")
    for codigo, info in MENU.items():
        prato, preco = info
        print(f"{codigo:<6} | {prato:<16} | R$ {preco:.2f}")
    print("=========================================")
    
    
    while True:
        try:
         
            codigo_digitado = input("\nDigite o CÓDIGO do prato desejado (ou 0 para fechar a conta): ")
            
         
            codigo_digitado = int(codigo_digitado)
            
           
            if codigo_digitado == 0:
                print("\nFechando a conta...")
                break # Sai do loop while
            
            
            if codigo_digitado in MENU:
                prato, preco = MENU[codigo_digitado]
                
                
                pedidos.append({"prato": prato, "preco": preco})
                
                print(f"-> '{prato}' (R$ {preco:.2f}) adicionado ao seu pedido.")
                
            else:
                print("ERRO: Código inválido. Por favor, digite um código da tabela ou 0 para finalizar.")

        except ValueError:
            print("ERRO: Entrada inválida. Por favor, digite um número inteiro (o código do prato ou 0).")

    
   ,
    if not pedidos:
        print("\nNenhum pedido foi realizado. Obrigado e volte sempre!")
        return

    total_conta = 0.0
    
    print("\n--- RES