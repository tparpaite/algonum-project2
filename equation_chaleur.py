import numpy as np;
import math;


def generate_block(A, N, i, j):
    for x in range(i, i + N):
        for y in range(j, j + N ):
            if (x == y):
                A[x, y] = -4

                if (x != i + N - 1):
                    A[x+1, y] = 1
                    A[x, y+1] = 1


def generate_neighbour_block(A, N, i, j):
    for x in range(i, i + N):
        for y in range(j, j + N):
            if (x + j == y + i):
                A[x, y] = 1


def generate_matrix(N):
    A = np.matrix(np.zeros([N * N, N * N]))

    for i in range(0, N * N, N):
        for j in range(0, N * N, N):
            if (i == j):
                generate_block(A, N, i, j)

                if (i != N * N - N):
                    generate_neighbour_block(A, N, i + N, j)
                    generate_neighbour_block(A, N, i, j + N)

    return A
                
            
            
    