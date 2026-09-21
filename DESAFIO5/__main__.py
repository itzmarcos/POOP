from carrinho import *

def main():
    p1 = Produto('Caneta', 10)
    p2 = Produto('Caderno', 40)
    p3 = Produto('Pincel', 15)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p2
    c1 = c1 + p1
    c1 = c1 + p3

    c2 = c2 + c1

    print(c1)
    print(c2)
    
if __name__ == "__main__":
    main()