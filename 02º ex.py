'''
Sabendo disso, crie uma lista chamada idades para armazenar várias idades. Em seguida, passe essa lista como parâmetro para uma função chamada verifica_se_pode_dirigir
e para cada idade dentro da lista, verifique se a idade é maior ou igual a 18 anos. Se for, exiba a idade e a mensagem Tem permissão. Caso contrário, exiba a mensagem
Não tem permissão.
'''

idades = [12,18,24,13]

def verifica_se_pode_dirigir(idades):

    idade = 18

    for i in idades:

        if i >= 18:
            print('Tem permissão')
        else:
            print('Não tem permissão')

verifica_se_pode_dirigir(idades)
