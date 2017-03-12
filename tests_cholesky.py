import numpy as np
from cholesky import *

#nom de la fonction: testsCholesky
#Parametre: la taille de la matrice
#Retourne: l'erreur maximum genere par rapport a la fonction cholesky de la bibliotheque numpy en generant une matrice aleatoire de taille n*n

def testsCholesky(n):
    A = genere(n)
    B = cholesky(A)
    C = np.linalg.cholesky(A)
    D = B - C
    max = 0
    for i in range (n):
        for j in range (n):
            tmp = abs(D[i,j])
            if (max < tmp):
                max = tmp
    return max
s = np.random.randint(2,100)
r = testsCholesky(s)
print("l'erreur sur cholesky de la matrice carre symetrique definie positive genere aleatoirement de taille ",s,"est ",r)


#nom de la fonction: testsCholesky_incomplet
#Parametres: n la taille de la matrice, p tel que valeurs nulles de la matrice < 2*p
#Retourne l'erreur maximum genere par rapport a la fonction cholesky de la bibliotheque en utilisant la fonction generation

def testsCholesky_incomplet(n,p):
    A = generation(n,p)
    B = cholesky_incomplet(A)
    C = np.linalg.cholesky(A)
    D = B - C
    max = 0
    for i in range (n):
        for j in range (i):
            tmp = abs(D[i,j])
            if( max < tmp):
                max = tmp
    return max

q = np.random.randint(2,10)
j = testsCholesky_incomplet(q,1)
print("l'erreur sur cholesky_incomplet de la matrice carre definie positive creuse genere aleatoirement de taille",q,"est",j)
