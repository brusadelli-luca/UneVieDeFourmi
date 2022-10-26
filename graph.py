import networkx as nx
import matplotlib.pyplot as plt

def graph_creation(index, node_list, edge_list, show = False):

    G = nx.Graph(step=index)

    G.add_nodes_from(node_list, ants=0)
    G.nodes[0]['ants'] = 5
    G.add_edges_from(edge_list)

    nx.draw(G, with_labels=True, font_weight='bold')

    if show:
        plt.show()

    return G