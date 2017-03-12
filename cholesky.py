import numpy as np

#Nom de la fonction: cholesky
#Parametres: une matrice symetrique definie positive A
#Retourne: une matrice T qui est la decomposition de cholesky de la matrice A

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
#Parametres: une matrice symetrique definie positive A creuse
#Retourne: une matrice T qui est la decomposition de cholesky de la matrice A

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
#Parametres: un entier n
#Retourne: une matrice symetrique definie positive de taille n*n T en generant d'abord aleatoirement une matrice triangulaire inferieure A, en calculant son transpose B et en faisant T = A*B
#Role: permet de tester la fonction cholesky 

def genere(n):
    A = np.matrix(np.zeros([n,n]))
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.rand()
    B = np.matrix.transpose(A)
    return A*B


# Nom de la fonction: generation
#Parametres: deux entiers n et p
#Retourne: une matrice symetrique definie positive creuse de taille n*n T ayantun nombre de valeurs nulles < 2*p en generant d'abord aleatoirement une matrice triangulaire inferieure A, en calculant son transpose B et en faisant T = A*B
#Role: tester la fonction cholesky_incomplet 

def generation(n,p):
    A = np.matrix(np.zeros([n,n]))
    nb = 1
    for i in range(n):
        for j in range(i+1):
            A[i,j] = np.random.rand()
            if( i!=j and nb <= p and np.random.randint(2,3)==2):
                A[i,j] = 0
                nb += 1
    B = np.matrix.transpose(A)
    return A*B


