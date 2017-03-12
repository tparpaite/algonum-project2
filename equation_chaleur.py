import numpy as np;
import matplotlib.pyplot as mp
import math;
from conjgrad import *


def generate_block(A, N, i, j):
    """ PARAMS: A (matrice), N (taille bloc), i et j : entiers
    Genere un bloc avec une diagonale de -4 et
    deux diagonales de 1 (au-dessus et en-dessous) "
    
    for x in range(i, i + N):
        for y in range(j, j + N ):
            if (x == y):
                A[x, y] = -4

                if (x != i + N - 1):
                    A[x+1, y] = 1
                    A[x, y+1] = 1


def generate_neighbour_block(A, N, i, j):
    """ PARAMS: A (matrice), N (taille bloc), i et j : entiers
    Genere un bloc avec une diagonale de 1 "
    
    for x in range(i, i + N):
        for y in range(j, j + N):
            if (x + j == y + i):
                A[x, y] = 1


def generate_heat_equation(N):
    """ N : taille des blocs (pour la discretisation
    Genere l'equation de la chaleur, c'est-a-dire la matrice A
    et le vecteur b tels que Ax = b """
    
    # First generate matrix A
    A = np.matrix(np.zeros([N * N, N * N]))

    for i in range(0, N * N, N):
        for j in range(0, N * N, N):
            if (i == j):
                generate_block(A, N, i, j)

                if (i != N * N - N):
                    generate_neighbour_block(A, N, i + N, j)
                    generate_neighbour_block(A, N, i, j + N)

    # Then generate vector B
    b = np.zeros([N * N, 1]);
    
    return (A, b)
               


