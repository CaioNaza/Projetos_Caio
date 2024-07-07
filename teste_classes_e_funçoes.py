class Menu:
     
    def show_menu():
        
        Menu = """\n
    ================ MENU ================
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Nova conta
    [5]Listar contas
    [6]Novo usuário
    [7]Sair
    => """
        return input(Menu)


class conta:
    def __init__(self, numero, agencia, cliente, extrato, saldo=0) :
        
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self.cliente = cliente 
        self.extrato = extrato


    def depositar(saldo, extrato, /):
            return saldo, extrato


    def sacar(*,self, saldo, valor, extrato, limite, nro_saq, lim_saq, agencia):

        if valor > self._saldo:
              print("Saldo insufisciente")

        elif nro_saq >= lim_saq:
            print("Limite de saques excedido")
        
        

            self._saldo = saldo
            self._numero = valor
            self._agencia = agencia
            self.cliente = limite
            self.nro_saq = nro_saq
            self.lim_saq = lim_saq
            self.extrato = extrato

    @property
    def excedeu_saldo ( numero, saldo, valor):
            excedeu_saldo = valor > saldo
            print("Saldo excedido")

   