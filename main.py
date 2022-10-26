from functions import *
from classes import *
from graph import *

anthill = 1

anthills_names = {1 : '../Fourmilieres/fourmiliere_un.txt', \
                    2 : '../Fourmilieres/fourmiliere_deux.txt', \
                    3 : '../Fourmilieres/fourmiliere_trois.txt', \
                    4 : '../Fourmilieres/fourmiliere_quatre.txt', \
                    5 : '../Fourmilieres/fourmiliere_cinq.txt' \
                       }

file_name = anthills_names[anthill] # print('file name', file_name)

param = import_data(file_name) # print('param', param)

ant_nb = param[0]
node_nb = param[1]
node_list = param[2]
edge_nb = param[3]
edge_list = param[4]
# print('edge_list', edge_list)

edge_list = name_to_index(node_list,edge_list) # print('edge_list', edge_list)

# matrix = matrix_data(param, edge_list)
# print('matrix\n',matrix)

node_list = [*range(node_nb)]
# print('node_list', node_list, 'edge_list', edge_list)

hill1 = Anthill(ant_nb, node_nb, node_list)

G = graph_creation(0, node_list, edge_list, show=False)
print(G.graph,G.nodes.data())
# print(G.nodes[0])
# print(G)

# print(list(G.nodes))
# print(list(G.edges))

for step in range(2):
    print('\nSTEP ' + str(step) + '\n')
    print(G.graph,G.nodes.data())

    for ant in reversed(hill1.ants):
        print(ant)
        node = ant.origin
        print('//node//',node)
        # print('//G.adj[' + str(node) + ']//',G.adj[node])
        # print('//list(G.adj[' + str(node) + '])//',list(G.adj[node]))
        # print('//list(G.adj[' + str(node) + '][0])//', list(G.adj[node])[0])
        print('\n')

        # node = G.nodes[ant.origin]
        
        # print('node[1]', node[1])
        # for node in list(G.nodes):
        # print(G.nodes[node])
        # print(G.nodes[node]['ants'])

        
        for adj in list(G.adj[node]):
            # print(G.nodes[adj])
            # print(G.nodes[adj]['ants'])

            if G.nodes[adj]['ants'] == 0:
                G.nodes[node]['ants'] = G.nodes[node]['ants'] - 1
                G.nodes[adj]['ants'] = G.nodes[adj]['ants'] + 1

        ant.origin = adj
        
    G.graph['step'] = G.graph['step'] + 1