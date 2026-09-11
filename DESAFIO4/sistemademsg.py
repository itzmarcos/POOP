green = "\033[42m"
normal = "\033[0m"
yellow = "\033[43m"
red =  "\033[41m"

class Mensagem():
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def mostrar(self):
        print(green + self.mensagem + normal)

class Alerta(Mensagem):

    def mostrar(self):
        print(yellow + 'AVISO' + normal)
        print(yellow + self.mensagem + normal)

class Erro(Mensagem):

    def mostrar(self):
        print(red + "ERRO" + normal)
        print(red + self.mensagem + normal)