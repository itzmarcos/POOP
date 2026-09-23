from hashlib import sha256


class ContaBancaria():
    def __init__(self, id: int, nome, saldo = 0):
        self._id = id
        self._titular = nome
        self.__saldo = 0
        self.__hash = None
        #@nome

    @property
    def hash(self):
        return self.__hash

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome(self):
        return self.__titular

    @saldo.setter
    def saldo(self, saldo):
        if saldo == self.sacar:
            return self.__saldo - self.sacar
        elif saldo == self.depositar:
            return self.__saldo + self.depositar


    def validar_senha(self,chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('Senha conferi')
        else:
            print('Senha não conferi')


    def pede_senha():
        pass

        
    def sacar(self, valor, chave):
        try:
            saque = input(valor)
            return saque
        except:
            print('Tente novamente')

    def depositar(self, valor):
        try:
            deposita = input(valor)
            return deposita
        except:
            print('Tente novamente')