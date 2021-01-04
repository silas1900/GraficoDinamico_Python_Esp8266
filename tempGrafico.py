# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:12:18 2021

@author: silas
"""


from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests
#import time



img = plt.figure()
ax = img.add_subplot(1, 1, 1)

ex = [0] #lista eixo x
ey = [10] #lista eixo y


#incremento partindo dos últimos valores de cada lista
temperatura=10
tempo=0

#função para animar
def draw_graph(i, ex, ey):
    global temperatura
    global tempo
    #IP address: 10.0.0.15 do esp8266 para saber o endereço basta abrir o monitor serial logo assim que conectcar o esp
    resposta = requests.get('http://10.0.0.15/') # use o IP address atribuido a sua placa.
    dados = resposta.text
    dados_separados = dados.split("=")
    #incremento
    #temperatura= temperatura+10
    print(dados_separados[1])
    temperatura= float(dados_separados[1][0:4])
    tempo = tempo + 2 #incremento de 2 em 2 segundos

    #append índice do tempo e temperatura adiciona no final da lista
    ex.append(tempo)
    ey.append(temperatura)


    # desenhar x e y
    ax.clear()
    ax.axis(ymin=0, ymax=60) # Escala de Valores max e mim do eixo y
    ax.plot(ex, ey,marker='o')
    ax.grid()


    plt.title('Temperatura/Tempo')
    plt.ylabel('Temperatura/°C',color='blue')
    plt.xlabel('Tempo/s', color='blue')

# altere o valor do interval para que que o frame seja atualizado de maneira mais rápida ou lenta
ani = animation.FuncAnimation(img, draw_graph, fargs=(ex, ey), interval=2000) # interval=2000 = 2s
plt.show()