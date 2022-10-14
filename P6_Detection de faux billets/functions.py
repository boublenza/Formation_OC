import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import pandas as pd
import seaborn as sns
import math
import statsmodels.api as sm

def courbe_lorenz(data, nom_col, cat=None) :
    col=data[nom_col].values
    n=len(col)
    lorenz = np.cumsum(np.sort(col))/col.sum()
    lorenz = np.append([0], lorenz) #contient les ordonnées des points, et commence par 0
    xaxis = np.linspace(0-1/n, 1+1/n, n+1) #contient les abcisses
    fig = plt.figure(figsize=(7, 5))
    plt.plot(xaxis,lorenz,drawstyle='steps-post')
    plt.plot([0,1], [0,1]) #tracer la bisséctrice

    major_ticks_top=np.linspace(0,1,11)

    plt.xticks(major_ticks_top)
    plt.yticks(major_ticks_top)

    plt.grid(which="major",alpha=0.6)

    plt.title(f'Courbe de lorenz du \'{nom_col}\' {cat}',fontsize=15)
    #plt.savefig(f'graphes\\lorenz_{nom_col}{cat}.jpg')
    plt.show()

    AUC = (lorenz.sum() -lorenz[-1]/2 -lorenz[0]/2)/n # Surface sous la courbe de Lorenz. Le premier segment (lorenz[0]) est à moitié en dessous de 0, on le coupe donc en 2, on fait de même pour le dernier segment lorenz[-1] qui est à moitié au dessus de 1.
    S = 0.5 - AUC # surface entre la première bissectrice et le courbe de Lorenz
    print('gini =', 2*S)
    return 2*S
    
def display_circles(pcs, n_comp, pca, axis_ranks, labels=None, label_rotation=0, lims=None):
    for d1, d2 in axis_ranks: # On affiche les 3 premiers plans factoriels, donc les 6 premières composantes
        if d2 < n_comp:

            # initialisation de la figure
            fig, ax = plt.subplots(figsize=(7,7))

            # détermination des limites du graphique
            if lims is not None :
                xmin, xmax, ymin, ymax = lims
            elif pcs.shape[1] < 30 :
                xmin, xmax, ymin, ymax = -1, 1, -1, 1
            else :
                xmin, xmax, ymin, ymax = min(pcs[d1,:]), max(pcs[d1,:]), min(pcs[d2,:]), max(pcs[d2,:])

            # affichage des flèches
            # s'il y a plus de 30 flèches, on n'affiche pas le triangle à leur extrémité
            if pcs.shape[1] < 30 :
                plt.quiver(np.zeros(pcs.shape[1]), np.zeros(pcs.shape[1]),
                   pcs[d1,:], pcs[d2,:], 
                   angles='xy', scale_units='xy', scale=1, color="grey")
                # (voir la doc : https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html)
            else:
                lines = [[[0,0],[x,y]] for x,y in pcs[[d1,d2]].T]
                ax.add_collection(LineCollection(lines, axes=ax, alpha=.1, color='black'))
            
            # affichage des noms des variables  
            if labels is not None:  
                for i,(x, y) in enumerate(pcs[[d1,d2]].T):
                    if x >= xmin and x <= xmax and y >= ymin and y <= ymax :
                        plt.text(x, y, labels[i], fontsize='14', ha='center', va='center', rotation=label_rotation, color="blue", alpha=0.5)
            
            # affichage du cercle
            circle = plt.Circle((0,0), 1, facecolor='none', edgecolor='b')
            plt.gca().add_artist(circle)

            # définition des limites du graphique
            plt.xlim(xmin, xmax)
            plt.ylim(ymin, ymax)
        
            # affichage des lignes horizontales et verticales
            plt.plot([-1, 1], [0, 0], color='grey', ls='--')
            plt.plot([0, 0], [-1, 1], color='grey', ls='--')

            # nom des axes, avec le pourcentage d'inertie expliqué
            plt.xlabel('F{} ({}%)'.format(d1+1, round(100*pca.explained_variance_ratio_[d1],1)))
            plt.ylabel('F{} ({}%)'.format(d2+1, round(100*pca.explained_variance_ratio_[d2],1)))

            plt.title("Cercle des corrélations (F{} et F{})".format(d1+1, d2+1))
            plt.savefig(f'graphes\\cercle_correlation_F{d1+1}_F{d2+1}')
            plt.show(block=False)
        
# def display_factorial_planes(X_projected, n_comp, pca, axis_ranks, labels=None, alpha=1, illustrative_var=None, c=None):
#     for d1,d2 in axis_ranks:
#         if d2 < n_comp:
 
#             # initialisation de la figure       
#             fig = plt.figure(figsize=(7,6))
        
#             # affichage des points
#             if illustrative_var is None:
#                 plt.scatter(X_projected[:, d1], X_projected[:, d2], alpha=alpha, c=c,cmap='tab10')
#             else:
#                 illustrative_var = np.array(illustrative_var)
#                 for value in np.unique(illustrative_var):
#                     selected = np.where(illustrative_var == value)
#                     plt.scatter(X_projected[selected, d1], X_projected[selected, d2], alpha=alpha, label=value,c=c,cmap='tab10')
#                 plt.legend()

#             # affichage des labels des points
#             if labels is not None:
#                 for i,(x,y) in enumerate(X_projected[:,[d1,d2]]):
#                     plt.text(x, y, labels[i],
#                               fontsize='14', ha='center',va='center') 
                
#             # détermination des limites du graphique
#             boundary = np.max(np.abs(X_projected[:, [d1,d2]])) * 1.1
#             plt.xlim([-boundary,boundary])
#             plt.ylim([-boundary,boundary])
        
#             # affichage des lignes horizontales et verticales
#             plt.plot([-100, 100], [0, 0], color='grey', ls='--')
#             plt.plot([0, 0], [-100, 100], color='grey', ls='--')

#             # nom des axes, avec le pourcentage d'inertie expliqué
#             plt.xlabel('F{} ({}%)'.format(d1+1, round(100*pca.explained_variance_ratio_[d1],1)))
#             plt.ylabel('F{} ({}%)'.format(d2+1, round(100*pca.explained_variance_ratio_[d2],1)))

#             plt.title("Projection des individus (sur F{} et F{})".format(d1+1, d2+1))
#             plt.show(block=False)

def format_figure(X_projected,pca):
    # détermination des limites du graphique
    boundary = np.max(np.abs(X_projected[:, [0,1]])) * 1.1
    plt.xlim([-boundary,boundary])
    plt.ylim([-boundary,boundary])

    # affichage des lignes horizontales et verticales
    plt.plot([-100, 100], [0, 0], color='grey', ls='--')
    plt.plot([0, 0], [-100, 100], color='grey', ls='--')

    # nom des axes, avec le pourcentage d'inertie expliqué
    plt.xlabel('F{} ({}%)'.format(1, round(100*pca.explained_variance_ratio_[0],2)))
    plt.ylabel('F{} ({}%)'.format(2, round(100*pca.explained_variance_ratio_[1],2)))

    plt.title("Projection des individus (sur F{} et F{})".format(1, 2))
    
    
def display_scree_plot(pca):
    scree = pca.explained_variance_ratio_*100
    plt.bar(np.arange(len(scree))+1, scree)
    plt.plot(np.arange(len(scree))+1, scree.cumsum(),c="red",marker='o')
    plt.xlabel("rang de l'axe d'inertie")
    plt.ylabel("pourcentage d'inertie")
    plt.title("Eboulis des valeurs propres")
    plt.savefig(f'graphes\\eblouis_valeurs_propres')   
    plt.show(block=False)
    
    
def plot_boxplot(x,y,data): 
    fig = plt.figure(figsize=(7, 5))
    ax = sns.boxplot(x=x, y=y,   data=data, hue=x, dodge=False,palette="tab10")
    ax.set_title(f'Boxplot de {y} par {x}',fontsize=15)
  #  plt.savefig(f'graphes\\boxplot_{x}_{y}.jpg')
  
  
