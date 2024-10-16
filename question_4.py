# ORIENTADO A OBJETO - Desenvolva um programa que simule um caixa eletrônico de um banco com múltiplas contas correntes. O programa deve permitir operações como depósito, saque, transferência entre contas e consulta de extrato (o extrato deve exibir o saldo da conta, juntamente com o registro de todas as transações efetuadas pelo cliente). Implemente também um sistema de cadastro de senhas para cada nova conta cadastrada. Essa senha será requerida pelo sistema ao usuário para a conclusão de uma das transações supracitadas. No caso do usuário digitar três vezes a senha incorreta, a conta do usuário deverá ser bloqueada e uma mensagem deverá surgir, orientando que o cliente se dirija à boca do caixa para efetuar o desbloqueio.

import getpass

class AccountBank:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0
        self.transactions = []
        self.password_attempts = 0
        self.is_active = True
        
    def login(self):
        if (self.status() == False):
            return False

        password = getpass.getpass('Digite sua senha: ')
        while password != self.password:
            self.password_attempts += 1
            if self.password_attempts == 3:
                self.is_active = False
                return self.status()
            print('Senha incorreta')
            password = getpass.getpass('Tente novamente: ')
        return True
        
    def status(self):
        if (self.is_active):
            return True
        print('Conta bloqueada, dirija-se a um caixa para desbloquear\n\n')
        return False

    def deposit(self, value):
        self.balance += value
        self.transactions.append(f'Depósito realizado: R${value}')
        print('Depósito realizado com sucesso\n\n')

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.transactions.append(f'Saque realizado: R${value}')
            print('Saque realizado com sucesso\n\n')
        else:
            print('Saldo insuficiente\n\n')

    def transfer(self, value, account):
        if self.balance >= value:
            self.balance -= value
            account.balance += value
            self.transactions.append(f'Você enviou R${value} para {account.name}')
            account.transactions.append(f'Você recebeu R${value} de {self.name}')
            print('Transferência realizada com sucesso\n\n')
        else:
            print('Transferência não realizada, saldo insuficiente\n\n')

    def extract(self):
        print(f'Nome: {self.name}\nSaldo: R${self.balance}\nTransações: {self.transactions}\n\n')
        
class Bank:
    def __init__(self):
        self.accounts = []
        self.account = None
        self.menu()

    def menu(self):
        while True:
            print('1 - Criar conta\n2 - Login\n3 - Sair')
            option = input('Escolha uma opção: ')
            if option == '1':
                self.create_account()
            elif option == '2':
                self.login()
            elif option == '3':
                break
            else:
                print('Opção inválida')

    def create_account(self):
        name = input('Digite o nome da sua nova conta: ')
        password = getpass.getpass('Crie uma senha (você não verá nada): ')
        account = AccountBank(name, password)
        self.accounts.append(account)
        print('\nConta criada com sucesso!\n\n')

    def login(self):
        name = input('Digite o nome da sua conta: ')
        accountIndex = self.find_account(name)
        if (accountIndex == -1):
            print('Conta não encontrada\n\n')
            return
        account = self.accounts[accountIndex]
        if account.login():
            self.account = account
            print('Credenciais corretas, você entrou!\n\n')
            self.account_menu()
            
    def find_account(self, name):
        for i, account in enumerate(self.accounts):
            if account.name == name:
                return i
        return -1
    
    def transferTo(self, value, name):
        accountIndex = self.find_account(name)
        if (accountIndex == -1):
            print('Transferência não realizada, conta não encontrada\n\n')
            return
        account = self.accounts[accountIndex]
        if account:
            self.account.transfer(value, account)
    
    def account_menu(self):
        while True:
            print(f'Conta de {self.account.name}\nSaldo: R${self.account.balance}\n')
            print('1 - Depositar\n2 - Sacar\n3 - Transferir\n4 - Extrato\n5 - Sair da conta')
            option = input('Digite uma opção: ')
            print('\n')
            if option == '1':
                value = float(input('Valor: '))
                self.account.deposit(value)
            elif option == '2':
                value = float(input('Valor: '))
                self.account.withdraw(value)
            elif option == '3':
                value = float(input('Valor: '))
                name = input('Nome do destinatário: ')
                self.transferTo(value, name)
            elif option == '4':
                self.account.extract()
            elif option == '5':
                break
            else:
                print('Invalid option')

Bank()