from __future__ import division
import numpy as np;
import numpy.linalg as la;
import math;


def conjgrad(A, b, x):
    """ PARAMS : A (matrice), b vecteur connu, x vecteur inconnu
    Resout l'equation Ax = b en utilisant la methode du gradient conjugue """
    r = b - A*x;
    p = r;
    rsold = (np.transpose(r)*r)[0,0];

    end = False
    while end == False:
        Ap = A * p;
        alpha = (rsold / (np.transpose(p) * Ap))[0,0];

        x = x + alpha * p;
        r = r - alpha * Ap;
        rsnew = (np.transpose(r)*r)[0,0];

        if math.sqrt(rsnew) < 1e-10:
              end = True;

        p = r + rsnew/rsold * p;
        rsold = rsnew;
        
    return x


def conjgrad_precond(A, b, x):
    """ Methode du gradient conjugue avec preconditionneur (non acheve) """
    r = b - A*x;
    M = la.cholesky(A); # preconditioner    
    z = la.inv(M)*r;
    p = z;
    rsold = (np.transpose(r)*z)[0,0];

    end = False;
    while end == False:
        Ap = A * p;
        alpha = (rsold / (np.transpose(p) * Ap))[0,0];

        x = x + alpha * p;
        r = r - alpha * Ap;
        z = la.inv(M)*r;
        rsnew = (np.transpose(z)*r)[0,0];
        #print(rsnew)

        if np.sqrt(rsnew) < 1e-10:
              end = True;

        p = z + rsnew/rsold * p;
        rsold = rsnew;
        
    return x
