import numpy as np
from cholesky import *
from conjgrad import *
from equation_chaleur import *

def run_test(test):
    if test():
        print(test.__name__ + " PASSED")
    else:
        print(test.__name__ + " FAILED")


def test_cholesky():
    """ """


def test_conjgrad():
    """ Test basique (wikipedia) """    
    A = np.matrix([[4,1],
                   [1,3]])
    
    b = np.matrix([[1],
                   [2]])

    x = np.matrix(np.zeros([2,1]))
    x = conjgrad(A, b, x)

    # Check if result matches expected output    
    expected = np.linalg.solve(A, b)
    
    return np.array_equal(x, expected)


def test_equation_chaleur_radiateur():
    """ Cas d'un radiateur place au centre du carre """

    (A, b) = generate_heat_equation(3)
    b[4,0] = 1

    # Vector solution : 
    x = np.zeros([9,1]);
    x = abs(conjgrad(A,b,x).reshape((3,3)))

    mp.imshow(x)
    mp.show()


def test_equation_chaleur_mur_nord():
    """ Cas d'un mur chaud place au Nord """

    (A, b) = generate_heat_equation(3)
    b[6,0] = 1
    b[7,0] = 1
    b[8,0] = 1

    # Vector solution : 
    x = np.zeros([9,1]);
    x = conjgrad(A,b,x).reshape((3,3))

    mp.imshow(x)
    mp.show()    


def main():
    #run_test(test_cholesky)
    run_test(test_conjgrad)
    test_equation_chaleur_radiateur()
    test_equation_chaleur_mur_nord()    


if __name__ == "__main__":
    main()
