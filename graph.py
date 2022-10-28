import networkx as nx
import matplotlib.pyplot as plt

def graph_creation(index, anthill, ant_nb, node_list, edge_list, show = False):

    G = nx.Graph(step=index)

    G.add_nodes_from(node_list, ants=0)
    G.nodes['Sv']['ants'] = ant_nb

    G.add_edges_from(edge_list)
    # nx.draw(G, with_labels=True, font_weight='bold')
    
    ants_attributes = nx.get_node_attributes(G, 'ants')
    capacity_attributes = nx.get_node_attributes(G, 'capacity')
    nodes = G.nodes()
    
    labels = []

    for node in nodes:
        labels.append((node, node + '(' + str(ants_attributes[node]) + '/' + str(capacity_attributes[node]) + ')'))

    labels = dict(labels)

    plt.title("FOURMILIERE N° " + str(anthill))
    nx.draw(G, labels=labels,  with_labels=True, font_weight='bold')

    if show:
        plt.show()

    return G


def paths_list(G, start, end):
    paths_list = list(nx.all_simple_edge_paths(G, 'Sv', 'Sd'))
    
    # for path in paths_list:
        # print(path)

    return paths_list