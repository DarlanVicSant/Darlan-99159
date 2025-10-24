import os
from dataclasses import dataclass
os.system("cls")
@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

    def mostrar_endereco(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}"


@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print("\n--- DADOS DA PESSOA ---")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco.mostrar_endereco()}")


def main():
    print("=== Cadastro de Pessoa ===")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")

    print("\n--- Endereço ---")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    cidade = input("Cidade: ")

    endereco = Endereco(logradouro, numero, cidade)
    pessoa = Pessoa(nome, email, endereco)

    pessoa.mostrar_dados()


if __name__ == "__main__":
    main()
