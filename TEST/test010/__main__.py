from banco import *

from banco import ContaBancaria

def main():
    c = ContaBancaria(20, 'Marcelo', 1000)
    c.sacar = 500
    print(c.sacar)


if __name__ == '__main__':
    main()