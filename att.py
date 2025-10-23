import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando dados da pessoa: ")
pessoa1 = Pessoa(nome=input("Digite deu nome: "),
                 idade=int("Digite sua idade: "),
                peso=float("Digite seu peso: "),
                altura=float("Digite sua altura: ")),
               