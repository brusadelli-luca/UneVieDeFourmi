import pandas
import numpy

# Data file parcing
def import_data(file_name):

    data = pandas.read_table(file_name, header=None)
    print(data)
    data = data.to_numpy()

    # Get ant number
    ant_nb = int(str(data[0][0]).split('=')[-1])

    # Get node number
    for cell in data:

        if '-' in str(cell):

            node_nb = int(numpy.where(data==cell)[0]) - 1 + 2
            break


    # Get node list with names and capacity attribute
    node_list = [('Sv', {'capacity' : ant_nb})]

    for i in range(1, node_nb - 1):
        node = data[i][0].split(' ')
        if len(node) < 3:
            node_list.append((node[0], {'capacity' : 1}))

        else:
            node_list.append((node[0], {'capacity' : int(node[2])}))  
    
    node_list.append(('Sd', {'capacity' : ant_nb}))


    # Get edge number
    edge_nb = data.shape[0] - node_nb - 1 + 2


    # Get edge list
    edge_list = []

    for i in range(1 + node_nb - 2, data.shape[0]):
        edge = data[i][0].split(' - ')
        edge = (edge[0], edge[1])
        edge_list.append(edge)


    return (ant_nb, node_nb, node_list, edge_nb, edge_list)