Menu = """

[1] Consumo

=> """

consumo_mes = 0
recomendar_plano = (" 50 mbps, 100 mbps, 300 mbps, /")

while True:

    opcao = input(Menu)

    if opcao == "1":
        
        consumo = float(input("Informe seu consumo em GB: "))
        print(recomendar_plano(consumo))

        if consumo <= 10:
            consumo_mes += consumo


            
        