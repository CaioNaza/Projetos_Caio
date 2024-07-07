

def recomendar_plano(consumo_mes):
    return consumo_mes

def consumo(consumo_medio):
    if consumo_medio <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif  consumo_medio <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    elif consumo_medio >= 21:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."
    



consumo_mensal = float(input("Digite o consumo médio mensal: "))
classificacao = consumo(consumo_mensal)
print(f" {classificacao}")

