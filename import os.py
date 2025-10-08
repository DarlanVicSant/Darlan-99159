import os
os.system("cls")

def calcular_inflacao(preco):
    if preco < 100:
        return preco * 1.10  # aumenta 10%
    else:
        return preco * 1.20  # aumenta 20%


preco_original = float(input("Digite o preço do produto: "))

preco_inflacionado = calcular_inflacao(preco_original)


print(f"Preço original: R$ {preco_original:.2f}")
print(f"Preço com inflação: R$ {preco_inflacionado:.2f}")
