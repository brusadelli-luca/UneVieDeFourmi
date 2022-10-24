import pandas
import numpy
import networkx as nx

def import_data(file_name):

    data = pandas.read_table(file_name,header=None)
    data = data.to_numpy()

    ant_nb = int(str(data[0][0]).split('=')[-1])

    for cell in data:

        if '-' in str(cell):

            room_nb = int(numpy.where(data==cell)[0]) - 1
            break

    room_list = ['Sv']

    for i in range(1, room_nb + 1):
        room_list.append(data[i][0])  
    
    room_list.append('Sd')


    node_nb = data.shape[0] - room_nb - 1

    node_list = []

    for i in range(1 + room_nb, data.shape[0]):
        node_list.append(data[i][0])  


    return(ant_nb, room_nb, room_list, node_nb, node_list)

def matrix_data(param):

    node_nb = param[1]
    node_list = param[2]
    edge_nb = param[3]
    edge_list = param[4]

    matrix_size = node_nb + 2

    matrix = numpy.zeros((matrix_size,matrix_size))

    edge_list_coord = []
    edge_list_tup = []

    for edge in edge_list:

        edge = edge.split(' - ')
        matrix_coord = (node_list.index(edge[0]), node_list.index(edge[1]))
        
        #################################################################
                
        edge_list_coord.append(matrix_coord)
        # matrix_coord_tup = (edge[0], edge[1])
        # edge_list_tup.append(matrix_coord_tup)

        #################################################################

        matrix_coord_reverse = (node_list.index(edge[1]), node_list.index(edge[0]))

        matrix[matrix_coord] = matrix[matrix_coord] + 1
        matrix[matrix_coord_reverse] = matrix[matrix_coord_reverse] + 1


    return (matrix, edge_list_coord)
    # return (matrix, edge_list_tup)


def graph_creation(node_list,edge_list_tup):

    G = nx.Graph()

    G.add_nodes_from(node_list)
    G.add_edges_from(edge_list_tup)

    return G