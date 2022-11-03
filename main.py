from classes import *
import random as rd
from functions import *
import matplotlib.pyplot as plt

# Select data set (anthill number)
anthill = 3

anthills_names =  { 1 : '../Fourmilieres/fourmiliere_un.txt', \
                    2 : '../Fourmilieres/fourmiliere_deux.txt', \
                    3 : '../Fourmilieres/fourmiliere_trois.txt', \
                    4 : '../Fourmilieres/fourmiliere_quatre.txt', \
                    5 : '../Fourmilieres/fourmiliere_cinq.txt' \
                    }

file_name = anthills_names[anthill]


# Data set file parsing
param = import_data(file_name)

ant_nb = param[0]
node_nb = param[1]
node_list = param[2]
edge_nb = param[3]
edge_list = param[4]


# Create anthill (ants list) and node graph
hill1 = Anthill(param)


# Save step contents in txt file
file = open("output.txt","a+")

step = 0
print('\nSTEP ' + str(step))

file.write('STEP ' + str(step))

G = hill1.graph

# Runs loop until all ants reach end node
while G.nodes['Sd']['ants'] != ant_nb:

    step = step + 1
    print('\nSTEP ' + str(step))
    file.write('\n\nSTEP ' + str(step))

    for ant in hill1.ants:

        node = ant.pos
        dest = ''

        if node != 'Sd':
            
            dest_list = list(iter(G[node]))

            # Removes dead ends from destinations list
            for dest_i in dest_list:
                if G.nodes[dest_i]['dead_end'] == True:
                    dest_list.remove(dest_i)

            # If dead end reached
            if len(dest_list) == 1 and dest_list[0] == ant.origin:
                G.nodes[node]['dead_end'] = True
                dest = dest_list[0]
            
            # If end node in destinations
            elif 'Sd' in dest_list:
                dest = 'Sd'

            else:

                # Sort destinations by cost to end
                dest_list_t = []

                for i in range(len(dest_list)):
                    dest_list_t.append((dest_list[i], G.nodes[dest_list[i]]['to_end']))

                dest_list = dest_list_t
                dest_list = rd.sample(dest_list, len(dest_list))
                sorted(dest_list, key=lambda dest:dest[1])
                
                # Fwd if possible
                for dest_i in dest_list:
                    dest_i = dest_i[0]
                    
                    if G.nodes[dest_i]['ants'] < G.nodes[dest_i]['capacity'] and \
                        (dest_i != ant.origin or (dest_i != ant.origin and dest_list.index(dest_i) == (len(dest_list) - 1))): 
                        
                        dest = dest_i
                        break      
            
            # Move ant
            if dest != '':

                G.nodes[node]['ants'] = G.nodes[node]['ants'] - 1
                G.nodes[dest]['ants'] = G.nodes[dest]['ants'] + 1

                ant.origin = node
                ant.pos = dest
                print('ant', ant.index,': from', node, 'to', dest)
                file.write('\nant ' + str(ant.index) + ' : moves from ' + node + ' to ' + dest)
        
                ant.steps = ant.steps + 1

                # After moving, get cost to end
                if dest == 'Sd':
                    G.nodes[ant.origin]['to_end'] = 1

                elif G.nodes[dest]['to_end'] < node_nb:
                    cost = G.nodes[dest]['to_end'] + 1
                    
                    if cost < G.nodes[ant.origin]['to_end']:
                        G.nodes[ant.origin]['to_end'] = cost

    # Saves plot data in anthill
    hill1.save_graph_data()

print('END\n')
file.write('\n\nEND')


# Plot animation
step = 0

for data in hill1.plot_data:

    plt.clf()
    plt.title("FOURMILIERE N° " + str(anthill) + '\n Step : ' + str(step))
    nx.draw(G, labels=data[0], with_labels=True, node_color=data[1], edge_color=data[2], pos=hill1.pos)
    plt.savefig(str(step) + ".png")
    step = step + 1
    plt.pause(1)

plt.show()