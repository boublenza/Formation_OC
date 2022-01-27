# Le code de ces fonctions est repris du cours "Nettoyez et analysez votre jeu de données"

import math
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.api as sm


def regression_lineaire(data, c1, c2):
    Y = data[c1]
    X = data[[c2]]
    X = X.copy() # On modifiera X, on en crée donc une copie
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit() # OLS = Ordinary Least Square (Moindres Carrés Ordinaire)
    a,b = result.params[c2],result.params['intercept']
    plt.plot(data[c2],data[c1], "o")
    plt.plot(np.arange(100),[a*x+b for x in np.arange(100)])
    plt.xlabel(c2)
    plt.ylabel(c1)
    plt.title(f'Régression linéaire entre {c1} et {c2}',fontsize=14)
    plt.savefig('achat_age_sans_outliers')
    plt.show()

def courbe_lorenz(data, nom_col, cat='') :
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
    plt.savefig(f'graphes\\lorenz_{nom_col}{cat}.jpg')
    plt.show()

    AUC = (lorenz.sum() -lorenz[-1]/2 -lorenz[0]/2)/n # Surface sous la courbe de Lorenz. Le premier segment (lorenz[0]) est à moitié en dessous de 0, on le coupe donc en 2, on fait de même pour le dernier segment lorenz[-1] qui est à moitié au dessus de 1.
    S = 0.5 - AUC # surface entre la première bissectrice et le courbe de Lorenz
    print('gini =', 2*S)
    return 2*S


def eta_squared(x,y):
    moyenne_y = y.mean()
    classes = []
    for classe in x.unique():
        yi_classe = y[x==classe]
        classes.append({'ni': len(yi_classe),
                        'moyenne_classe': yi_classe.mean()})
    SCT = sum([(yj-moyenne_y)**2 for yj in y])
    SCE = sum([c['ni']*(c['moyenne_classe']-moyenne_y)**2 for c in classes])
    return SCE/SCT


def sturges_rule(n):
    return round(1 + math.log2(n))

