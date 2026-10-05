from exporta import *

def main():
    u = [
        Usuario("Antonia", "antonia@gmail.com"),
        Usuario("Jaki", "jaki_cavalaro@gmail.com"),
        Usuario("Eddy", "ed@hotmail.com")
    ]
    a = [Aluno("Vitoria", "Gastronomia", "2 ano"),
         Aluno("Vitor", "Astrologia", "1 ano"),
         Aluno("Bambam", "ADS", "2 ano")
         ]
    exporta_dados(JSON(), u)
    exporta_dados(XML(), a)

if __name__ == "__main__":
    main()