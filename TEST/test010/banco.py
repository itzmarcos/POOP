from hashlib import sha256


class ContaBancaria():
    def __init__(self, id: int, nome:str, saldo:float = 0, chave:str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = None
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f'Conta {self._id} criada com sucesso!\nSaldo atual de R${self.__saldo:.2f}')

    def pede_senha(self):
        pass

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome(self):
        return self.__titular

    @nome.setter
    def nome(self, novonome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
        else:
            print('Senha nao confere')

    @saldo.setter
    def saldo(self, saldo):
        if saldo == self.sacar:
            return self.__saldo - self.sacar
        elif saldo == self.depositar:
            return self.__saldo + self.depositar


    def validar_senha(self,chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f'A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo'


    def pede_senha():
        pass

        
    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque NEGADO!')
            else:
                self.__saldo -= valor
                print(f'Saque de R${valor:,.2f} autorizado na conta {self._id}')
        else:
            print('Senha nao confere')

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado!')