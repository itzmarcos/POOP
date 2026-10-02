from EscolaH import *

def main():
    c = Aluno('Jaqueline', 16, "aluna")
    p = Professor('Daniele', 32, 'Professora')
    d = Diretor('Carlos', 50, 'Diretor')
       
    print(c.funcao())
    print(p.funcao())
    print(d.funcao())

if __name__ == "__main__":
    main()