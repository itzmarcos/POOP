from senha import *

def main():
    c = Credencial()
    c.senha = str(input('Digite uma senha: '))
    print(c.senha)

    c.validar('show')


if __name__ == '__main__':
    main()