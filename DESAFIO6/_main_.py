from validador import *

def main():
    validar_dado(Usuario(), 'jaki_123')
    validar_dado(Email(), "cavalaro@gmail.com")
    validar_dado(Senha(), "Senha123!")
    
if __name__ == "__main__":
    main()