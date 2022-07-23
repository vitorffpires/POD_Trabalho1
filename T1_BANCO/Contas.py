from abc import ABCMeta, abstractmethod


class ErroQuantidade(Exception):
    """Classe de erros relacionados a quantidade"""
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return 'Este valor não é válido: ' + str(self.valor)


class ErroSaldo(Exception):
    """Classe de erros relacionados ao saldo"""
    def __init__(self, tipoconta, valor):
        self.valor = valor
        self.TipoConta = tipoconta

    def __str__(self):
        return 'valor de saldo de ' + str(self.valor) + 'fora dos limites na ' + str(self.TipoConta)


class Moeda:
    """ classe que implementa o tipo de moeda utilizada nos saques e depositos feitos pelas contas """

    def __init__(self, tipo='real', valor=0):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        print('Moeda: {}'.format(self.tipo))


class ContaBancaria(metaclass=ABCMeta):
    """Classe abstrata e geral das contas"""
    conta_bancaria = 0

    def __init__(self, id, nome, cpf, saldo):
        self.__id = id
        if len(str(id)) != 8:
            raise ErroQuantidade(id)  # id com menos ou mais do que 4 letras
        self.__nome = nome
        if len(self.nome) > 50 or len(self.nome) == 0:
            print('nome muito grande ou não digitado, tente novamente')
            raise ValueError
        self.__cpf = cpf
        if len(self.cpf) != 12:
            print('Cpf com valor invalido, digite um cpf com 11 digitos')
            raise ValueError
        self.__saldo = saldo
        ContaBancaria.add_ContaBancaria()

    # função que consulta o id
    @property
    def id(self):
        return self.__id 

     # consulta o nome do cliente
    @property
    def nome(self):
        return self.__nome

    # consulta o cpf do cliente
    @property
    def cpf(self):
        return self.__cpf

    #get saldo
    @property
    def saldo(self):
        return self.__saldo

    # setter do id
    @id.setter
    def id(self, valor):
        self.__id = valor

    # setter do nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor    

    # setter do cpf
    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    # setter do saldo
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    # saque
    def saque(self, num):
            if num < 0:
                raise ValueError
            self.__saldo -= num
            #if self.__saldo < 0:
            #    raise ErroSaldo("conta", self.__saldo)

    # deposito
    def deposito(self, num):
        if num < 0:
            raise ValueError
        self.__saldo += num

    # Função para tratar atributos desconhecidos
    def __getattr__(self, nome):
        print('Atributo desconhecido:', nome)
        return self.metodo_desconhecido

    # Função para metodos desconhecidos
    @staticmethod
    def metodo_desconhecido():
        return 'Método desconhecido!'

    # Função para consultar o rendimento
    @abstractmethod
    def consulta_rendi(self, tempo): pass

    # mostra quantas contas bancarias existem
    @staticmethod
    def qtd_ContaBancaria():
        print(f'A quantidade de Contas Bancarias criadas é igual a: {ContaBancaria.conta_bancaria}.')

    # Função para mostrar a quantidade de contas criadas no total
    @staticmethod
    def status_conta():
        ContaBancaria.qtd_ContaBancaria()
        ContaCorrente.qtd_contaCorrente()
        ContaInvestimento.qtd_contaInvestimento()
        ContaPoupanca.qtd_contaPoupanca()

    # incrementa o numero das contas bancarias
    @classmethod
    def add_ContaBancaria(cls):
        cls.conta_bancaria += 1

    # operação de saque verboso em uma das contas
    def saque_verboso(obj, valor):
        if isinstance(obj, ContaCorrente):
            print(f"nome: {ContaBancaria.nome}, cpf: {ContaBancaria.cpf}, cheque especial {ContaCorrente.chequeEspecial}, "
                  f"saldo: {ContaCorrente.saldo}, id: {ContaCorrente.id}")
            obj.saque(valor)
        if isinstance(obj, ContaPoupanca):
            print(f"nome: {ContaBancaria.nome}, cpf: {ContaBancaria.cpf}, taxa {ContaPoupanca.taxa}, "
                  f"saldo: {ContaPoupanca.saldo}, id: {ContaPoupanca.id}")
            obj.saque(valor)
        if isinstance(obj, ContaInvestimento):
            print(f"nome: {ContaBancaria.nome}, cpf: {ContaBancaria.cpf}, risco {ContaInvestimento.risco}, "
                  f"saldo: {ContaInvestimento.saldo}, id: {ContaInvestimento.id}")
            obj.saque(valor)


class ContaCorrente(ContaBancaria):
    conta_corrente = 0

    def __init__(self, id, nome, cpf, saldo, chequeEspecial):
        super().__init__(id, nome, cpf, saldo)
        if chequeEspecial > 0:
            print('o cheque especial deve ser negativo')
            raise ValueError
        self.__chequeEspecial = chequeEspecial
        ContaCorrente.add_conta_corrente()

    # função que consulta o cheque especial na conta corrente
    @property
    def chequeEspecial(self):
        return self.__chequeEspecial

    # setter do cheque especial
    @chequeEspecial.setter
    def chequeEspecial(self, valor):
        self.__chequeEspecial = valor  

    # função que calcula quanto do cheque especial vai ser incrementado
    def consulta_rendi(self, tempo):
        montante = self.saldo
        rendi = (montante * (pow((1 + 0.01), tempo) - 1))
        return f"rendimento: {rendi}"

    # consulta o numero de contas corrente
    @staticmethod
    def qtd_contaCorrente():
        print(f'A quantidade de contas corrente criadas é igual a {ContaCorrente.conta_corrente}.')

    # incrementa o numero de contas correntes
    @classmethod
    def add_conta_corrente(cls):
        cls.conta_corrente += 1


class ContaPoupanca(ContaBancaria):
    conta_poupanca = 0

    def __init__(self, id, nome, cpf, saldo, taxa):
        super().__init__(id, nome, cpf, saldo)
        if taxa < 0 or taxa > 1:
            raise ValueError
        self.__taxa = taxa
        ContaPoupanca.add_conta_poupanca()

    # função que consulta a taxa na conta pupanca
    @property
    def taxa(self):
        return self.__taxa

    # setter da taxa
    @taxa.setter
    def taxa(self, num):
        self.__taxa = num 

    # função que retorna o rendimento esperado da conta poupança
    def consulta_rendi(self, tempo):
        montante = self.saldo
        rendi = (montante * (pow((1 + self.__taxa), tempo) - 1))
        return f"rendimento de : {rendi}"

    # consulta o numero de contas poupanla criadas
    @staticmethod
    def qtd_contaPoupanca():
        print(f'A quantidade de contas poupança criadas é igual a: {ContaPoupanca.conta_poupanca}.')

    # incrementa o numero de contas poupança
    @classmethod
    def add_conta_poupanca(cls):
        cls.conta_poupanca += 1


class ContaInvestimento(ContaBancaria):
    conta_investimento = 0

    def __init__(self, id, nome, cpf, saldo, risco):
        super().__init__(id, nome, cpf, saldo)
        if "alto" in risco:
            self.__risco = risco
        elif "medio" in risco:
            self.__risco = risco
        elif "baixo" in risco:
            self.__risco = risco
        else:
            raise ValueError
        self.__risco = risco.lower()
        ContaInvestimento.add_conta_investimento()

    # função que consulta o id na conta investimento
    @property
    def risco(self):
        return self.__risco

    # setter do risco
    @risco.setter
    def risco(self, valor):
        self.__risco = valor 

    # função que consulta o rendimento esperado na conta de investimento
    def consulta_rendi(self, tempo):
        montante = self.saldo
        taxa_i = 0
        if "baixo" in self.risco:
            taxa_i = 0.1
        elif 'medio' in self.risco:
            taxa_i = 0.25
        elif 'alto' in self.risco:
            taxa_i = 0.5
        rendi = montante * (pow((1 + taxa_i), tempo) - 1)
        return f"rendimento de {rendi}"

    # função que consulta o numero de contas criadas de investimento
    @staticmethod
    def qtd_contaInvestimento():
        print(f'A quantidade de contas de investimento criadas é igual a: {ContaInvestimento.conta_investimento}.')

    # função que incrementa  numero de contas de investimento
    @classmethod
    def add_conta_investimento(cls):
        cls.conta_investimento += 1