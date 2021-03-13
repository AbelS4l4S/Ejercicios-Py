import random


def run():
    v_min=1
    v_max=6
    tirar='y'
    while tirar=='y':
        print('Tirando los dados...')
        dado1=random.randint(v_min,v_max)
        dado2=random.randint(v_min,v_max)
        print(f'El valor de los dados fueron {dado1} y {dado2}')
        print(f'Sumando un valor de {dado1+dado2}')
        tirar=input('¿Quieres tirar de nuevo? (y / n): ')


if __name__ == '__main__':
    run()