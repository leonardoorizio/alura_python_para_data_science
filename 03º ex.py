'''
Sabendo disso, importe os métodos randrange e seed, crie 8 notas de 0 a 10, armazenando seu conteúdo numa variável chamada notas_matematica. Como os números gerados são
chamados de pseudo aleatórios, utilize o método seed escolhendo um valor de referência.
'''

from random import randrange, seed

def alura():

    notas_matematica = []

    for i in range(8):

        seed(i)
        notas_matematica.append(randrange(0,11))

    print(notas_matematica)
    print(len(notas_matematica))

alura()