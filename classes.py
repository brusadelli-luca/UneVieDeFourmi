class Node():
    def __init__(self,name,index,capacity = 1):
        self.name = name
        self.index = index
        self.capacity = capacity
        self.ant = False

    def __str__(self):
        return 'node description => name : ' + str(self.name) \
            + ' / index : ' + str(self.index) \
            + ' / capacity : ' + str(self.capacity) \
            + ' / ant : ' + str(self.ant)


class Ant():
    def __init__(self,index):
        self.index = index
        self.origin = 0
        self.dest  = 0

    def __str__(self):
        return 'ant description => index : ' + str(self.index) \
            + ' / origin : ' + str(self.origin) \
            + ' / dest : ' + str(self.dest)


class Anthill():
    def __init__(self, ant_nb, node_nb, node_list, step = 0):
        self.nodes = self.create_nodes(ant_nb, node_nb, node_list)
        self.ants = self.create_ants(ant_nb)
        self.step = step
        # self.Status()


    def create_nodes(self, ant_nb, node_nb, node_list):
        node_list_obj = []
        node_list_obj.append(Node(node_list[0], 0, capacity = ant_nb))

        for i in range(1,node_nb - 1):

            node_list_obj.append(Node(node_list[i], i))

        node_list_obj.append(Node(node_list[node_nb - 1], node_nb - 1, capacity = ant_nb))

        # print(node_list_obj)
        return node_list_obj


    def create_ants(self, ant_nb):
        ant_list_obj = []
        
        for i in range(ant_nb):

            ant_list_obj.append(Ant(i))

        # print(ant_list_obj)
        return ant_list_obj

    def print_nodes(self):
        print('\nNodes status :')
        for node in self.nodes:
            print(node)

    def print_ants(self):
        print('\nAnts status :')
        for ant in self.ants:
            print(ant)

    def Status(self):
        self.print_nodes()
        self.print_ants()
        print('\n')