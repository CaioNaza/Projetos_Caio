
#Refatoração do menu que agora virou uma classe.
#Adição do def display_menu
class Menu:
    def __init__(self):

        self.Menu = """\n
        ================ MENU ================
        [1]Depositar
        [2]Sacar
        [3]Extrato
        [4]Nova conta
        [5]Listar contas
        [6]Novo usuário
        [7]Sair
        => """   
    def display_Menu(self):
        print(self.Menu)
        return input("Escolha uma opção: ")

#Aqui foi necessário refatorar o cod, oq permitiu compactar
#e ter uma melhor legibilidade e funcionamento permitindo uma manutenção mais fácil
#cod menor e de melhor entendimento

#Classe conta: tem como metodos depositar, sacar e exibir extrato.
class Conta:
    def __init__(self, numero, agencia, cliente, extrato, saldo=0):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self.cliente = cliente 
        self.extrato = extrato

    def depositar(saldo, extrato, /):
            return saldo, extrato
    
    def sacar(*,self, saldo, valor, extrato, limite_money, nro_saq, lim_saq):
        if valor > self._saldo:
            print("Operação falhou. Saldo insuficiente.")
        elif valor > limite_money:
            print("Operação falhou. O valor do saque excede o limite.")
        elif nro_saq >= lim_saq:
            print("Operação falhou. Número máximo de saques excedido.")
        else:
            self._saldo -= valor
        
            self.extrato += f"Saque:R$ {valor:.2f}\n"
            print("Saque realizado com sucesso ")
        self._saldo = saldo
        self._numero = valor
        self._agencia = extrato
        self.limite_money = limite_money
        self.nro_saq = nro_saq
        self.lim_saq = lim_saq
        

        conta = conta(0)
        conta.depositar(100)
        print(conta._saldo)
    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:R$ {self._saldo:.2f}")
        print("==========================================")
    

    def criar_usuario(usuarios):
        cpf = input("Informe o CPF (somente número): ")
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("CPF já cadastrado")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (d-m-a): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)

    print("Usuário criado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        for conta in contas:
            linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
            print("=" * 100)

    def main():
        LIMITE_SAQUES = 3
        AGENCIA = "0001"

        saldo = 0
        limite_dia = 500
        extrato = ""
        numero_saques = 0
        usuarios = []
        contas = []

        while True:
            opcao = Menu()

            if opcao == "1":
                valor = float(input("Informe o valor do depósito: "))

                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "2":
                valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_dia,
                nro_saq=numero_saques,
                lim_saq=LIMITE_SAQUES,

             )

            elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

            elif opcao == "6":
            criar_usuario(usuarios)

            elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

            elif opcao == "5":
                listar_contas(contas)

            elif opcao == "7":
                break

            else:
               print("Operação inválida.")


main()