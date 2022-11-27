'''
Sabendo disso, importe o módulo matplotlib.pyplot, dando a ele o apelido plt geralmente dado pela comunidade Python. Em seguida, plote o gráfico das 8 notas de matemática,
de forma que o eixo x indique as provas e no eixo y as notas, incluindo o título Notas de matemática.
'''

import matplotlib.pyplot as plt

x = list(range(1,9))
y = [6, 2, 0, 3, 3, 9, 9, 5]
plt.plot(x,y)
plt.title('Notas de Matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()



