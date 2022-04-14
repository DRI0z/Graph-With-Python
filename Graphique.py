# Introduction des bibliothèques ####################################################################

import pandas

import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

# Initialisation des variables #################################################################

c = 0

emplacements = ['g1_0_avg1.txt','g1_95_dg1.txt',"g1_130_fleche_dg1.txt","g1_fonction_45_dg1.txt","g1_fonction_X3_sg1.txt","g2_19.txt","g2_39_avg2.txt","g2_59_avg2.txt","g2_79_apg2.txt","g2_96_dg2.txt","X1_bute_bg2.txt","X2_derriere_stockeur.txt","X3_bout _stockeur.txt","X4_debut_stockeur.txt"]

liste_sender = []
liste_receiver = []

font = {'color':  'black',
        'weight': 'bold',
        'size': 14,
        }
# Prise des valeurs des bandes passantes reçue et envoyée des fichiers texte ####################################################################

# Créer une boucle du nombre de valeur qu'il y a dans la liste emplacements
for e in range(len(emplacements)):
    
    # df_graph est égale a la lecture du fichier x dans la liste emplacements
    df_graph = pandas.read_csv(emplacements[c] ,sep = '\t',header = 0)
    
    # La ligne 60/61 de la colonne 3 est égale à sender/receiver
    sender=(df_graph.iloc[60,3]) 
    receiver=(df_graph.iloc[61,3])
    
    #les flottants sender et receiver sont rangée dans 2 listes diffèrentes 
    liste_sender.append(float(sender))
    liste_receiver.append(float(receiver))
    
    # Permet de changer de fichier texte
    c = c + 1
            
# Code Graphique ######################################################################

# Création des bars
barWidth = 0.4
bars1 = liste_sender
bars2 = liste_receiver 
bars3 = bars1 + bars2


# Position X des bars 
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = r1 + r2

 
# Création des barplot
sns.set_theme(style="darkgrid")
plt.bar(r1, bars1, width = barWidth, color = (0.68,0.84,0.36), label='Envoyée', align = 'center')
plt.bar(r2, bars2, width = barWidth, color = (0.84,0.368,0.51), label='Reçue', align = 'center')

 
# Création de la legende et des titres 
plt.legend(loc="center right")
plt.title('Graphique montrant la moyenne des bandes passantes \n reçues et envoyées par rapport aux lieux', fontdict=(font))
plt.xlabel('Lieux', fontdict=(font))
plt.ylabel('Bande passante (en Mbtis/s)', fontdict=(font))


# Texte sous chaque barplot avec une rotation de 90° 
plt.xticks([r + 0.2 for r in range(len(r3))],['g1_0_avg1','g1_95_dg1',"g1_130_fleche_dg1","g1_fonction_45_dg1","g1_fonction_X3_sg1","g2_19","g2_39_avg2","g2_59_avg2","g2_79_apg2","g2_96_dg2","X1_bute_bg2","X2_derriere_stockeur","X3_bout _stockeur","X4_debut_stockeur"] , rotation=85)
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


# Affiche le graphique 
plt.show()