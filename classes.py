class Ant():
    def __init__(self,index):
        self.index = index
        self.origin = 'Sv'
        self.steps = 0

    def __str__(self):
        return 'ant description => index : ' + str(self.index) \
            + ' / origin : ' + str(self.origin) \
            + ' / dest : ' + str(self.dest)


class Anthill():
    def __init__(self, ant_nb, node_nb, node_list, step = 0):
        self.nodes = node_list
        self.ants = self.create_ants(ant_nb)
        self.step = step
        # self.Status()

    def create_ants(self, ant_nb):
        ant_list_obj = []
        
        for i in range(ant_nb):

            ant_list_obj.append(Ant(i))

        return ant_list_obj

    def print_ants(self):
        print('\nAnts status :')
        for ant in self.ants:
            print(ant)

    def Status(self):
        self.print_ants()
        print('\n')