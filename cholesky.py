import numpy as np

#Nom de la fonction: cholesky
#Paramètres: une matrice symétrique définie positive A
#Retourne: une matrice T qui est la décomposition de cholesky de la matrice A"

def cholesky(A):
    n = len(A)
    T = np.matrix(np.zeros([n,n]))
    for i in range (n):
        for j in range (i,n):
            if(i==j):
                T[i,i] = A[i,i]
                if(i>0):
                    for k in range (i):
                        T[i,i] -= (T[i,k])**2
                T[i,i] = np.sqrt(T[i,i])
            else:
                T[j,i] = A[i,j]
                if(i>0):
                    for k in range (i):
                        T[j,i] -= (T[i,k])*(T[j,k])
                T[j,i] /= T[i,i]
    return T


#Nom de la fonction: cholesky_incomplet
#Paramètres: une matrice symétrique définie positive A qui a un nombre non nul de valeurs nulles
#Retourne: une matrice T qui est la décomposition de cholesky de la matrice A

def cholesky_incomplet(A):
    n = len(A)
    T = np.matrix(np.zeros([n,n]))
    for i in range (n):
        for j in range (i,n):
            if(A[i,j] == 0):
                T[j,i] = 0
            elif(i==j):
                T[i,i] = A[i,i]
                if(i>0):
                    for k in range (i):
                        T[i,i] -= (T[i,k])**2
                T[i,i] = np.sqrt(T[i,i])
            else:
                T[j,i] = A[i,j]
                if(i>0):
                    for k in range (i):
                        T[j,i] -= (T[i,k])*(T[j,k])
                T[j,i] /= T[i,i]
    return T


#Nom de la fonction: genere
#Paramètres: un entier n
#Retourne: une matrice symétrique définie positive de taille n*n T en générant d'abord aléatoirement une matrice triangulaire inférieure A, en calculant son transposé B et en faisant T = A*B
#Rôle: permet de tester la fonction cholesky 

def genere(n):
    A = np.matrix(np.zeros([n,n]))
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.rand()
    B = np.matrix.transpose(A)
    return A*B


# Nom de la fonction: generation
#Paramètres: deux entiers n et p
#Retourne: une matrice symétrique définie positive de taille n*n T ayant 2*p valeurs nulles en générant d'abord aléatoirement une matrice triangulaire inférieure A avec p valeurs nulles, en calculant son transposé B et en faisant T = A*B
#Rôle: tester la fonction cholesky_incomplet 

def generation(n,p):
    A = np.matrix(np.zeros([n,n]))
    nb = 1
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.rand()
            if( i!=j and nb <= p):
                A[i,j] = 0
                nb += 1
    B = np.matrix.transpose(A)
    return A*B

