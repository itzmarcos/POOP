from batalha import *

def main():
    p1 = Knight("Lord'Paulistinha", 1000)
    p2 = Sorcerer("Cachero", 2000)

    p1.atacar(p2, 200)
    p2.atacar(p1, 200)

    p1.curar()
    p2.curar()


if __name__ == "__main__":
    main()