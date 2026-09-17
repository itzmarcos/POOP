from Funcionario import *

def main():

    f1 = Horista("amanda", 12, 200)
    f1.calcular_salario()
    f1.analisar_sal()

    f2 = Mensalista('Jaqueline', 9000)
    f2.calcular_salario()
    f2.analisar_sal()


if __name__ == "__main__":
    main()