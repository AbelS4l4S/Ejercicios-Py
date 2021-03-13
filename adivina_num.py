import random


def run():
    num_a=int(input('Elige un número: '))
    num_b=int(input('Elige un número número mayor al número anterior: '))
    print(f'Dberas adivinar el número que voy a pen1sar entre {num_a} y {num_b}')
    print('Pensando ...')
    num_random=random.randint(num_a,num_b)
    num_elegido=int(input('Eliege un número'))

    while num_elegido != num_random:
        if num_elegido>num_random:
            num_elegido=int(input('Elige un número mas chico: '))
        else:
            num_elegido=int(input('Elige un número mas grande: '))
    
    print(f'FELICIDADES {num_random} es el número que pensé')


if __name__=='__main__':
    run()