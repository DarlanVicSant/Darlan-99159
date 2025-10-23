import os
from dataclasses import dataclass
os.system("cls")

from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Pessoa:
    """
    Representa uma pessoa com Nome, E-mail e Endereço.
    """

    nome: str
    email: str
    endereco: str



    def mostrar_dados(self) -> None:
        """
        Exibe todos os dados da pessoa: Nome, E-mail e Endereço.
        """
        print("-" * 30)
        print(f"Nome:     {self.nome}")
        print(f"E-mail:   {self.email}")
        print(f"Endereço: {self.endereco}")
        print("-" * 30)

    def mostrar_somente_nome(self) -> None:
        """
        Exibe apenas o nome da pessoa.
        """
        print(f"Nome da Pessoa: {self.nome}")



print("--- Criando as Pessoas ---")

pessoa1 = Pessoa(
    nome="João da Silva",
    email="joao.silva@exemplo.com",
    endereco="Rua das Flores, 101 - Centro"
)

pessoa2 = Pessoa(
    nome="Maria Oliveira",
    email="maria.o@exemplo.com",
    endereco="Avenida Principal, 55 - Bairro Novo"
)

print("\nPessoa 1 criada com sucesso.")
print("Pessoa 2 criada com sucesso.")



print("\n\n--- Chamando a função 'mostrar_dados()' para Pessoas ---")

print("\nDados Completos da Pessoa 1:")
pessoa1.mostrar_dados()

print("\nDados Completos da Pessoa 2:")
pessoa2.mostrar_dados()


print("\n\n--- Chamando a função 'mostrar_somente_nome()' para Pessoas ---")

print("\nNome da Pessoa 1:")
pessoa1.mostrar_somente_nome()

print("\nNome da Pessoa 2:")
pessoa2.mostrar_somente_nome()