'''
Sabendo disso, crie uma função chamada verifica_se_pode_dirigir que recebe um parâmetro chamado idade e inclua uma condicional if para analisar se a idade é maior ou igual
que 18 anos. Caso seja, exiba uma mensagem na tela dizendo que Tem permissão para dirigir. Senão(else), exiba a mensagem Não tem permissão para dirigir. Depois de executar,
crie a mesma função sem parâmetros, que armazena a idade digitada pelo usuário ou usuária. Como todo valor digitado através do teclado é uma string, não esqueça de converter
a idade com o código int(idade).
'''

#Com Parâmetro

idade = int(input('Qual sua idade:'))

def verifica_se_pode_dirigir(idade):
    if idade >= 18:
        print('Tem permissão para dirigir!')
    else:
        print('Não tem permissão para dirigir!')

verifica_se_pode_dirigir(idade)


#Sem Parâmetro

'''
def verifica_se_pode_dirigir():

    idade = int(input('Qual sua idade:'))
    if idade >= 18:
        print('Tem permissão para dirigir!')
    else:
        print('Não tem permissão para dirigir!')

verifica_se_pode_dirigir()
'''
