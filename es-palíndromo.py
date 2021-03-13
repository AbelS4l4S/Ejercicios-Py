def palíndromo(palabra):
    palabra=palabra.replace(' ','')
    palabra=palabra.lower()
    palabra_invertuda=palabra[::-1]
    if palabra==palabra_invertuda:
        return True
    else:
        return False


def run():
    palabra=input('Escribe una palabra')
    es_palíndromo=palíndromo(palabra)
    if es_palíndromo:
        print(f'La palabra {palabra} es un palíndromo')
    else:
        print(f'La palabra {palabra} NO es un palíndromo')


if __name__ == '__main__':
    run()
