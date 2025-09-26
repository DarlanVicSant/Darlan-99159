import os
os.system("cls")

def limpar_terminal():
    """Limpa o terminal (tentativa para diferentes sistemas operacionais)."""
    import os
    # 'cls' para Windows (nt), 'clear' para Linux/Mac (posix)
    os.system('cls' if os.name == 'nt' else 'clear') 

def exibir_menu():
    """Exibe o menu de opções."""
    print("\n" + "="*40)
    print("      PESQUISA DE FAMÍLIAS (PREFEITURA)")
    print("="*40)
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    print("="*40)

def obter_entrada_numerica(prompt, tipo=int):
    """Função robusta para obter entrada numérica (int ou float)."""
    while True:
        try:
            valor = tipo(input(prompt))
            if valor < 0:
                print("Valor inválido. Por favor, digite um número não negativo.")
                continue
            return valor
        except ValueError:
            print(f"❌ Entrada inválida. Digite apenas números.")

def adicionar_familia(dados):
    """Solicita e adiciona dados de uma nova família."""
    print("\n--- Adicionar Família ---")
    
    # 1. Obter Salário
    # Usamos float para o salário
    salario = obter_entrada_numerica("Digite o salário da família (R$): ", tipo=float)

    # 2. Obter Número de Filhos
    # Usamos int para o número de filhos
    num_filhos = obter_entrada_numerica("Digite o número de filhos: ", tipo=int)

    # Armazena os dados como uma tupla (salário, num_filhos)
    familia = (salario, num_filhos)
    dados.append(familia)
    print("\n✅ Família adicionada com sucesso!")
    
    input("\nPressione Enter para voltar ao menu...") # Pausa para ver o resultado

def exibir_resultados(dados):
    """Calcula e exibe os resultados solicitados (a, b, c, d, e)."""
    print("\n--- Resultados da Pesquisa ---")
    
    # a) Total de famílias
    total_familias = len(dados)
    if total_familias == 0:
        print("Nenhum dado foi registrado ainda.")
        return

    # Inicialização das variáveis para soma e extremos
    soma_salarios = 0.0
    soma_filhos = 0
    maior_salario = -1.0
    menor_salario = float('inf')
    
    # Itera sobre os dados para realizar todos os cálculos em um único loop
    for salario, num_filhos in dados:
        # Soma
        soma_salarios += salario
        soma_filhos += num_filhos
        
        # d) Maior salário
        if salario > maior_salario:
            maior_salario = salario
            
        # e) Menor salário
        if salario < menor_salario:
            menor_salario = salario

    # Cálculos das médias
    # b) Média do salário da população
    media_salario = soma_salarios / total_familias
    
    # c) Média do número de filhos
    media_filhos = soma_filhos / total_familias
    
    # Exibição formatada
    print(f"\na) Total de famílias que responderam: {total_familias}")
    print(f"b) Média do salário da população: R$ {media_salario:,.2f}")
    print(f"c) Média do número de filhos: {media_filhos:,.2f} filhos por família")
    print(f"d) Maior salário: R$ {maior_salario:,.2f}")
    print(f"e) Menor salário: R$ {menor_salario:,.2f}")
    print("------------------------------")
    
    input("\nPressione Enter para encerrar...")

def main():
    """Função principal que gerencia o fluxo do programa."""
    
    # Lista para armazenar os dados de cada família (tuplas de (salario, num_filhos))
    dados_familias = []
    
    # Loop principal do programa
    while True:
        limpar_terminal() 
        exibir_menu()
        
        opcao = input("Escolha uma opção (1 ou 2): ").strip()
        
        if opcao == '1':
            adicionar_familia(dados_familias)
        elif opcao == '2':
            limpar_terminal()
            exibir_resultados(dados_familias)
            break 
        else:
            print("\n❌ Opção inválida. Por favor, escolha 1 ou 2.")
            input("Pressione Enter para tentar novamente...")

# Executa a função principal
if __name__ == "__main__":
    main()