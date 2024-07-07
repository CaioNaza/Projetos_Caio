# Inicializa uma lista vazia para armazenar os equipamentos
equipamentos = []

# Definindo a quantidade máxima de equipamentos a serem inseridos
quantidade_maxima = 3

# Loop para solicitar ao usuário inserir os equipamentos
for i in range(quantidade_maxima):
    print(f"\n ")
    
    # Solicita o nome do equipamento
    nome = input( )
    
    # Cria um dicionário para armazenar as informações do equipamento
    equipamento = {
        "-": nome,
    }
    
    # Adiciona o dicionário à lista de equipamentos
    equipamentos.append(equipamento)

# Exibe a lista de equipamentos cadastrados
print("\nLista de Equipamentos:")
for equipamento in equipamentos:
    print(f"- {equipamento['-']}")
