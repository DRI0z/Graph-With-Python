# Introduction of libraries ####################################################################

import pandas

import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

# Initialization of variables #################################################################

c = 0

emplacements = ['g1_0_avg1.txt','g1_95_dg1.txt',"g1_130_fleche_dg1.txt","g1_fonction_45_dg1.txt","g1_fonction_X3_sg1.txt","g2_19.txt","g2_39_avg2.txt","g2_59_avg2.txt","g2_79_apg2.txt","g2_96_dg2.txt","X1_bute_bg2.txt","X2_derriere_stockeur.txt","X3_bout _stockeur.txt","X4_debut_stockeur.txt"]

liste_sender = []
liste_receiver = []

font = {'color':  'black',
        'weight': 'bold',
        'size': 14,
        }
# Taking the values of the received and sent bandwidths of the text files ####################################################################

# Create a loop of the number of values there are in the list locations
for e in range(len(emplacements)):
    
    # df_graph is equal to the reading of file x in the list locations
    df_graph = pandas.read_csv(emplacements[c] ,sep = '\t',header = 0)
    
    # Line 60/61 in column 3 is equal to sender/receiver
    sender=(df_graph.iloc[60,3]) 
    receiver=(df_graph.iloc[61,3])
    
    # The sender and receiver floats are stored in 2 different lists 
    liste_sender.append(float(sender))
    liste_receiver.append(float(receiver))
    
    # Allows you to change the text file
    c = c + 1
            
# Graphic Code ######################################################################

# Creation of bars
barWidth = 0.4
bars1 = liste_sender
bars2 = liste_receiver 
bars3 = bars1 + bars2


# X position of the bars 
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = r1 + r2

 
# Creation of barplots
sns.set_theme(style="darkgrid")
plt.bar(r1, bars1, width = barWidth, color = (0.68,0.84,0.36), label='Envoyée', align = 'center')
plt.bar(r2, bars2, width = barWidth, color = (0.84,0.368,0.51), label='Reçue', align = 'center')

 
# Creating the legend and titles 
plt.legend(loc="center right")
plt.title('Graphique montrant la moyenne des bandes passantes \n reçues et envoyées par rapport aux lieux', fontdict=(font))
plt.xlabel('Lieux', fontdict=(font))
plt.ylabel('Bande passante (en Mbtis/s)', fontdict=(font))


# Text under each barplot with a 90° rotation 
plt.xticks([r + 0.2 for r in range(len(r3))],['g1_0_avg1','g1_95_dg1',"g1_130_fleche_dg1","g1_fonction_45_dg1","g1_fonction_X3_sg1","g2_19","g2_39_avg2","g2_59_avg2","g2_79_apg2","g2_96_dg2","X1_bute_bg2","X2_derriere_stockeur","X3_bout _stockeur","X4_debut_stockeur"] , rotation=85)
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


# Displays the graph 
plt.show()
