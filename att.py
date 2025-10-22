import os
os.system("cls")

def ler_nota(numero_da_nota):
    """
    Função para ler e validar uma nota.
    A nota deve ser um número entre 0 e 10 (inclusive).
    Solicita a nota repetidamente até que seja válida.

    Args:
        numero_da_nota (int): O número ordinal da nota (ex: 1 para primeira nota).

    Returns:
        float: A nota válida inserida pelo usuário.
    """
    while True:
        try:
         
            nota = float(input(f"Digite a {numero_da_nota}ª nota (entre 0 e 10): "))

       
            if 0 <= nota <= 10:
                return nota 
            else:
                print("ERRO: A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
          
            print("ERRO: Entrada inválida. Digite um valor numérico para a nota.")

def calcular_media(nota1, nota2):
    """
    Função para calcular a média aritmética de duas notas.

    Args:
        nota1 (float): A primeira nota.
        nota2 (float): A segunda nota.

    Returns:
        float: A média aritmética das duas notas.
    """
    media = (nota1 + nota2) / 2
    return media

def verificar_aprovacao(media, criterio_aprovacao=7.0):
    """
    Função para verificar se o aluno está aprovado ou reprovado.

    Args:
        media (float): A média do aluno.
        criterio_aprovacao (float): O valor mínimo da média para aprovação (padrão é 7.0).

    Returns:
        str: Uma mensagem informando o status de aprovação.
    """
    if media >= criterio_aprovacao:
        return "APROVADO(A)"
    else:
        return "REPROVADO(A)"



if __name__ == "__main__":
    print("--- Sistema de Cálculo de Média e Aprovação ---")

  
    nota_a = ler_nota(1)
    nota_b = ler_nota(2)

  
    media_final = calcular_media(nota_a, nota_b)

    status = verificar_aprovacao(media_final)


    print("\n--- Resultado ---")
    print(f"Primeira Nota: {nota_a:.2f}")
    print(f"Segunda Nota: {nota_b:.2f}")
    print(f"Média Aritmética: {media_final:.2f}")
    print(f"Status: O(A) aluno(a) está **{status}**")
    print("-" * 23)