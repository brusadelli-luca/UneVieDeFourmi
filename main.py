from functions import *
from classes import *
from graph import *

anthill = 2

# For Repo : '../Fourmilieres/fourmiliere_un.txt'

anthills_names =  { 1 : 'Fourmilieres/fourmiliere_un.txt', \
                    2 : 'Fourmilieres/fourmiliere_deux.txt', \
                    3 : 'Fourmilieres/fourmiliere_trois.txt', \
                    4 : 'Fourmilieres/fourmiliere_quatre.txt', \
                    5 : 'Fourmilieres/fourmiliere_cinq.txt' \
                    }

file_name = anthills_names[anthill] # print('file name', file_name)

param = import_data(file_name) # print('param', param)

ant_nb = param[0]
node_nb = param[1]
node_list = param[2]
edge_nb = param[3]
edge_list = param[4]

# matrix = matrix_data(param, edge_list)
# print('matrix\n',matrix)

hill1 = Anthill(ant_nb, node_nb, node_list)

G = graph_creation(0, anthill, ant_nb, node_list, edge_list, show=True)

paths_list = paths_list(G, 'Sv', 'Sd')

path = paths_list[0]

step = 0
print('\nSTEP ' + str(step))
# print(G.nodes.data())

while G.nodes['Sd']['ants'] != ant_nb:

    for ant in hill1.ants:
        node = ant.origin
        if len(paths_list) != 1:
            if ant.index < 25:
                path = paths_list[1]
            else:
                path = paths_list[0]

        if node != 'Sd':
            
            dest = path[ant.steps][1]

            if G.nodes[dest]['ants'] < G.nodes[dest]['capacity']:
                G.nodes[node]['ants'] = G.nodes[node]['ants'] - 1
                G.nodes[dest]['ants'] = G.nodes[dest]['ants'] + 1

                ant.origin = dest
                print('ant', ant.index,': from', node, 'to', dest)
        
                ant.steps = ant.steps + 1

    step = step + 1   
    G.graph['step'] = step
    
    print('\nSTEP ' + str(step))
    # print(G.nodes.data())

print('END\n')

import networkx as nx
import numpy
# import scipy as sp
matrix = nx.to_numpy_array(G)
# nx.adjacency_matrix(G)
print('\n',matrix,'\n')