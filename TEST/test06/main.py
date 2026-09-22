from diariosecreto import *

def main():
    d = Diario()

    d.escrever('Olá Mundo')
    d.escrever('Eu gosto de Python')
    d.escrever('Estou conseguindo fazer o ex29')
    try:
        d.ler('Admin')
    except Exception as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()