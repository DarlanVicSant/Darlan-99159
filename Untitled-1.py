	
import os
import time

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# Função com parâmetros e com retorno.
def media(n1, n2):
    return n1 + n2

# Função com parâmetros e sem retorno.
def mostrar_resultado(media):
    print(f"Resultado: {media}")

# Código principal.
# Função sem parâmetros e sem retorno.
limpa_tela() # Chamando a função.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# Função com parâmetros e com retorno.
media = calcular_media(primeiro_numero, segundo_numero)

# Função com parâmetros e sem retorno.
mostrar_resultado(media) # Chamando a função.