class Bicicletas:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim")


    def parar (self):
        print ("parando bicicleta")
        print("bicicleta parada")

    def correr (self):
        ("correndo")

    #def __str__(self):
    #    return f"Bicicletas: cor ={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor 
    in self.__dict__.items()])} 


# b1 = Bicicletas ("vermelho", "monark barra circular", 1989, 550 )
#   b1.buzinar()
 #   b1.correr()
  #  b1.correr()
#print("b1.cor, b1.modelo, b1.ano, b1.valor")

b2 = Bicicletas("vrmelho", "monark barra circular", 1989, 550 )