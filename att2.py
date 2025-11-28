
import os
import time
from dataclasses import dataclass

os.system("cls || clear")  # limpa o terminal em Windows e Linux

lista_clientes = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}")


# Função para verificar se a lista está vazia
def lista_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False


def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu E-mail: ")
    telefone = input("Digite seu Telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")


# Função para encontrar cliente
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None


# Mostrar todos os clientes
def mostrar_todos_clientes(lista_clientes):
    if lista_vazia(lista_clientes):
        return
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        cliente.mostrar_dados()
        print("-" * 30)


# Atualizar cliente
def atualizar_clientes(lista_clientes):
    if lista_vazia(lista_clientes):
        return

    mostrar_todos_clientes(lista_clientes)
    print("\n--- Atualizar dados do cliente ---")
    nome_buscar = input("Digite o nome do cliente: ")

    cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente:
        print("\nCliente encontrado.")
        print("Deixe o campo vazio para manter o valor atual.\n")

        novo_nome = input(f"Nome atual ({cliente.nome}): ")
        novo_email = input(f"E-mail atual ({cliente.email}): ")
        novo_telefone = input(f"Telefone atual ({cliente.telefone}): ")

        if novo_nome:
            cliente.nome = novo_nome
        if novo_email:
            cliente.email = novo_email
        if novo_telefone:
            cliente.telefone = novo_telefone

        print(f"\nDados do cliente '{cliente.nome}' atualizados com sucesso!")
    else:
        print(f"\nCliente com nome '{nome_buscar}' não encontrado.")


# Excluir cliente
def excluir_cliente(lista_clientes):
    if lista_vazia(lista_clientes):
        return

    mostrar_todos_clientes(lista_clientes)
    nome_buscar = input("\nDigite o nome do cliente a ser excluído: ")

    cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente:
        lista_clientes.remove(cliente)
        print(f"\nCliente '{cliente.nome}' removido com sucesso!")
    else:
        print("\nCliente não encontrado.")


# Menu principal
while True:
    print("""
--- Gerenciador de Clientes ---
1 - Adicionar 
2 - Mostrar todos
3 - Atualizar 
4 - Excluir 
0 - Sair
""")

    try:
        opcao = int(input("Digite uma das opções acima: "))
    except:
        print("Entrada inválida! Digite um número.")
        time.sleep(2)
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_clientes(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    # Tempo antes de limpar
    if opcao == 1:
        time.sleep(1)
    elif opcao != 0:
        time.sleep(4)

    if opcao != 0:
        os.system("cls || clear")
