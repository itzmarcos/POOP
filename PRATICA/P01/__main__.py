from animal import *

def main():
    g = Gato('Flajola')
    c = Cachorro('Scooby')
    g = Galinha('Pintadinha')
    
    print(g.som())
    print(c.som())
    print(g.som())

if __name__ == "__main__":
    main()