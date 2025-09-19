import os 
os.system("cls")

menu = {
    1: {"item": "Picanha", "price": 25.00},
    2: {"item": "Lasanha", "price": 20.00},
    3: {"item": "Strogonoff", "price": 18.00},
    4: {"item": "Bife Acebolado", "price": 15.00},
    5: {"item": "Pão com ovo", "price": 5.00},
}


total_bill = 0


print("=== CARDAPIO DO RESTAURANTE ===")
print("Código | Prato           | Valor")
print("---------------------------------")
for code, details in menu.items():
    print(f"{code:<6} | {details['item']:<15} | R$ {details['price']:.2f}")
print("---------------------------------")

while True:
    try:

        choice_code = int(input("\nDigite o código do prato desejado (ou 0 para sair): "))

 
        if choice_code == 0:
            break
        
      
        if choice_code in menu:
            chosen_dish = menu[choice_code]
            total_bill += chosen_dish["price"]
            print(f"Você adicionou '{chosen_dish['item']}' ao seu pedido. Valor atual: R$ {total_bill:.2f}")
        else:
            print("Código inválido. Por favor, digite um código válido do menu.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

print(f"\nSeu pedido foi finalizado.")
print(f"O valor total a ser pago é: R$ {total_bill:.2f}")
print("Obrigado pela preferência!")