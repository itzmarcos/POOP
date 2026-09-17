from transportes import *


def main():
    dist = 80

    # entrega = Caminhao(dist)
    # print(f'Frete de {type(entrega).__name__} em {dist}km = R${entrega.calc_frete()}')

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    for item in viagem:
        print(f'{dist}km | {type(item).__name__} | R${item.calc_frete()}')

if __name__ == "__main__":
    main()