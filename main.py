from functions import *
from classes import *

file_name = '../Fourmilieres/fourmiliere_un.txt'

param = import_data(file_name)
print(param)
matrix_tup = matrix_data(param)

matrix = matrix_tup[0]
edge_list_tup = matrix_tup[1]

# print(matrix)

ant_nb = param[0]
node_nb = param[1]
node_list = param[2]
edge_nb = param[3]
edge_list = param[4]

matrix_size = node_nb + 2

node_list_obj = []
node_list_obj.append(Node(node_list[0], ant_nb))

for i in range(1,matrix_size - 1):

    node_list_obj.append(Node(node_list[i],1))

node_list_obj.append(Node(node_list[matrix_size - 1], ant_nb))

print(node_list_obj)


#########
node_list = [*range(matrix_size)]
#########
print(node_list,edge_list_tup)


G = graph_creation(node_list, edge_list_tup)

import matplotlib.pyplot as plt

# G = nx.petersen_graph()
# print(list(G.nodes))
# print(list(G.edges))
# print(list(G.nodes))
# subax1 = plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')

# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()