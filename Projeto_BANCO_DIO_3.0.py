import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
#Implementando POO na versão 3.0 do sistema bancário
#Foi necessário criar classes para algumas operações, como: conta, conta corrente, histórico, saque, Depósito...
#Armazenando os dados dos clientes em objetos ao inves de dicionarios

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
#Classe cliente tem como métodos realizar_transacao e add_conta
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def add_conta(self, conta):
        self.contas.append(conta)
        #Esse método adiciona uma nova conta a uma lista de contas pertencente a um objeto da classe.

class Pessoa_f(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
#Classe Pessoa_f é uma subclasse de Cliente, com atributos específicos de pessoa
class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.cliente = cliente
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("Operação falhou. Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso ")
            return True
        else:
            print("Operação falhou. O valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso ")
        else:
            print("Operação falhou. O valor informado é inválido.")
            return False
        
        return True

class Conta_corrente(Conta):
        def __init__(self, numero, cliente, limite=500, limite_saques=3):
            super().__init__(numero, cliente)
            self._limite = limite
            self._limite_saques = limite_saques   
            
        def sacar(self, valor):
            numero_saques = len(
                [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )

            excedeu_limite = valor > self._limite
            excedeu_saques = numero_saques >= self._limite_saques

            if excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite. @@@")

            elif excedeu_saques:
                print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

            else:
                return super().sacar(valor)

            return False
        def __str__(self):
                return f"""\
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
            """



class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def add_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
    
        if sucesso_transacao:
            conta.historico.add_transacao(self)

#Re escrevendo e implementando novos metodos
def menu():
    menu = """\n
    ================ MENU ================
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Nova conta
    [5]Listar contas
    [6]Novo usuário
    [7]Sair
    => """
    return input(textwrap.dedent(menu))

def sacar(clientes):
    cpf = input("infome o CPF ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
       
    valor = float(input("Informe o valor do saque"))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
       
    cliente.realizar_transacao(conta, transacao)

        
def exibir_extrato(clientes):
        cpf = input("infome o CPF ")
        cliente = filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado")
            return

        conta = recuperar_conta_cliente(cliente)
        if not conta:
           return                          

        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes

        extrato = ""
        if not transacoes:
           extrato = "Não foram realizadas movimentações."
        else:
           for transacao in transacoes:
               extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
        
        print(extrato)
        print(f"\nSaldo:R$ {conta.saldo:.2f}")
        print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("CPF já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (d-m-a): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = Pessoa_f (nome = nome, data_nascimento = data_nascimento, cpf = cpf, endereco = endereco)
    
    clientes.append(Cliente)

    print("Usuário criado")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encotrado")
        return
        
    conta = Conta_corrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
                depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "6":
            criar_cliente(clientes)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        if contas:
            contas.append(contas)

        elif opcao == "5":
                listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida.")

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("O cliente não possui conta")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(" O cliente não encontrado")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("O cliente não encontrado")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("CPF já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = Pessoa_f(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente cadastrado com sucesso. ===")

def main():
    clientes = []
    contas = []
#def main reescrita para garantir que funcione junto com as implementações do cod

    while True:
        opcao = menu()

        if opcao == "1":
           depositar(clientes)
        elif opcao == "2":
           sacar(clientes)
        

        elif opcao == "3":
            criar_conta(clientes, contas)

        elif opcao == "6":
           criar_cliente(clientes)

        elif opcao == "4":
          exibir_extrato(clientes)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida.")


main()