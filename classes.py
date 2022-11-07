from functions import *
import numpy
import networkx as nx

# Ant class definition
class Ant():
    def __init__(self, index):
        self.index = index
        self.origin = 'Sv'
        self.pos = 'Sv'
        self.steps = 0

    def __str__(self):
        return 'ant description => index : ' + str(self.index) \
            + ' / origin : ' + str(self.origin) \
            + ' / dest : ' + str(self.dest)


# Anthill class definition
class Anthill():
    def __init__(self, param):       
        self.ant_nb = param[0]
        self.node_nb = param[1]
        self.nodes = param[2]
        self.edge_nb = param[3]
        self.edge_list = param[4]

        self.ants = []

        for i in range(self.ant_nb):
            self.ants.append(Ant(i))


        # Graph creation with networkx
        G = nx.Graph()

        G.add_nodes_from(self.nodes, ants=0, dead_end=False, to_end=self.node_nb)
        G.nodes['Sv']['ants'] = self.ant_nb

        G.add_edges_from(self.edge_list)
        
        self.pos = nx.spring_layout(G)
        self.graph = G

        self.matrix = nx.to_numpy_array(G)

        self.plot_data = []


    # Data savig method to plot animation
    def save_graph_data(self):
        
        G = self.graph


        # Gets attributes
        ants_attributes = nx.get_node_attributes(G, 'ants')
        dead_end_attributes = nx.get_node_attributes(G, 'dead_end')
        to_end_attributes = nx.get_node_attributes(G, 'to_end')
        capacity_attributes = nx.get_node_attributes(G, 'capacity')
       

        # Builds labels with attributes
        labels = []
        
        for node in G.nodes():
            if to_end_attributes[node] == self.node_nb:
                cost = '\n'

            else:
                cost = '\n-->' + str(to_end_attributes[node]) # + ')'
                
            # labels.append((node, node + '\n' + str(to_end_attributes[node]) + '\n' + str(ants_attributes[node]) + '/' + str(capacity_attributes[node])))
            labels.append((node, node + '\n' + str(ants_attributes[node]) + cost)) #/' + str(capacity_attributes[node])))

        labels = dict(labels)


        # Sets node colors depending on ant number in nodes
        colors = []

        for node in G.nodes():

            if node == 'Sv':
                colors.append('tab:orange')
                
            elif dead_end_attributes[node]:
                colors.append('tab:red')

            elif ants_attributes[node] == 0:
                colors.append('tab:blue')

            elif ants_attributes[node] < capacity_attributes[node]:
                colors.append('tab:grey')

            elif node == 'Sd' and ants_attributes[node] == self.ant_nb:
                colors.append('tab:green')

            else:
                colors.append('tab:grey')


        # Sets edge colors depending on dead end status
        edge_colors = []

        for edge in G.edges():

            if dead_end_attributes[edge[1]]:
                edge_colors.append('tab:red')
            else:
                edge_colors.append('tab:grey')

        # self.plot_data.append((labels, colors, edge_colors, [(i + 1) * 100 for i in list(ants_attributes.values())]))        
        self.plot_data.append((labels, colors, edge_colors, [(i + 1) * 100 for i in list(capacity_attributes.values())]))        


    def print_ants(self):
        print('\nAnts status :')
        for ant in self.ants:
            print(ant)

    def Status(self):
        self.print_ants()
        print('\n')