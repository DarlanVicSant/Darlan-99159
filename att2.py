import os
os.system("cls")


# Algoritmo para coleta e análise de dados de habitantes - Versão 2.0

# Constantes (para facilitar a manutenção, se o valor de corte mudar)
SALARIO_MINIMO_MULHER = 500.00

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n" + "="*30)
    print("      MENU DE OPÇÕES")
    print("="*30)
    print("1 | Adicionar pessoa")
    print("2 | Exibir resultados")
    print("3 | Sair")
    print("="*30)

def limpar_terminal():
    """Limpa o terminal (tentativa para diferentes sistemas operacionais)."""
    import os
    # 'cls' para Windows (nt), 'clear' para Linux/Mac (posix)
    os.system('cls' if os.name == 'nt' else 'clear') 

def obter_entrada_numerica(prompt, tipo=int):
    """Função robusta para obter entrada numérica (int ou float)."""
    while True:
        try:
            valor = tipo(input(prompt))
            if valor < 0:
                print("Valor inválido. Por favor, digite um número positivo.")
                continue
            return valor
        except ValueError:
            print(f"Entrada inválida. Digite apenas números inteiros (para idade) ou decimais (para salário).")

def adicionar_pessoa(dados):
    """Solicita e adiciona dados de uma nova pessoa com tratamento de erro."""
    print("\n--- Adicionar Pessoa ---")
    
    # 1. Obter Idade
    idade = obter_entrada_numerica("Digite a idade: ", tipo=int)

    # 2. Obter Sexo
    while True:
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        if sexo in ('M', 'F'):
            break
        print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")

    # 3. Obter Salário
    salario = obter_entrada_numerica("Digite o salário (R$): ", tipo=float)

    # Armazena os dados
    pessoa = {
        'idade': idade,
        'sexo': sexo,
        'salario': salario
    }
    dados.append(pessoa)
    print("\n✅ Pessoa adicionada com sucesso!")
    
    input("\nPressione Enter para voltar ao menu...") # Pausa para ver o resultado

def exibir_resultados(dados):
    """Calcula e exibe os resultados solicitados (a, b, c)."""
    print("\n--- Resultados da Pesquisa ---")
    
    if not dados:
        print("Nenhum dado foi registrado ainda. Adicione pessoas primeiro (Opção 1).")
        return

    # Inicialização das variáveis
    total_salario = 0.0
    maior_idade = -1
    menor_idade = float('inf')
    count_mulheres_salario_alto = 0
    
    # Itera sobre os dados para realizar todos os cálculos em um único loop
    for pessoa in dados:
        # a) Soma salarial
        total_salario += pessoa['salario']
        
        # b) Maior e menor idade
        if pessoa['idade'] > maior_idade:
            maior_idade = pessoa['idade']
        if pessoa['idade'] < menor_idade:
            menor_idade = pessoa['idade']
            
        # c) Quantidade de mulheres com salário >= R$ 500,00
        if pessoa['sexo'] == 'F' and pessoa['salario'] >= SALARIO_MINIMO_MULHER:
            count_mulheres_salario_alto += 1

    # Cálculo final da média
    media_salario = total_salario / len(dados)
    
    # Exibição formatada
    print(f"\nTotal de pessoas analisadas: {len(dados)}")
    print(f"a) Média salarial do grupo: R$ {media_salario:,.2f}")
    print(f"b) Maior idade do grupo: {maior_idade} anos")
    print(f"b) Menor idade do grupo: {menor_idade} anos")
    print(f"c) Mulheres com salário >= R$ {SALARIO_MINIMO_MULHER:,.2f}: {count_mulheres_salario_alto}")
    print("------------------------------")
    
    input("\nPressione Enter para voltar ao menu...") # Pausa para ver o resultado

def main():
    """Função principal que gerencia o fluxo do programa."""
    
    # Lista para armazenar os dados de cada pessoa
    dados_habitantes = []
    
    # Loop principal do programa
    while True:
        limpar_terminal() 
        exibir_menu()
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == '1':
            adicionar_pessoa(dados_habitantes)
        elif opcao == '2':
            exibir_resultados(dados_habitantes)
        elif opcao == '3':
            limpar_terminal()
            print("\nPrograma encerrado. Obrigado por utilizar o sistema!")
            break 
        else:
            print("\n❌ Opção inválida. Por favor, escolha 1, 2 ou 3.")
            input("Pressione Enter para tentar novamente...")

# Executa a função principal
if __name__ == "__main__":
    main()