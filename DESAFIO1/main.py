from simulador import *

def main():
    a1 = DOC("Prova", 250000)
    a2 = PDF("Contrato", 1300000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)

if __name__ == "__main__":
    main()
