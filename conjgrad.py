from __future__ import division
import numpy as np;
import math;


def conjgrad(A,b,x):
    r = b - A*x;
    p = r;
    rsold = (np.transpose(r)*r)[0,0];
 
    while True:
        Ap = A * p;
        alpha = (rsold / (np.transpose(p) * Ap))[0,0];

        x = x + alpha * p;
        r = r - alpha * Ap;
        rsnew = (np.transpose(r)*r)[0,0];

        if math.sqrt(rsnew) < 1e-10:
              break;

        p = r + rsnew/rsold * p;
        rsold = rsnew;
        
    return x

#############################

A = np.matrix( [[4,1],
               [1, 3]] )

b = np.matrix( [[1],
               [2]] )

x = np.matrix( [[2],
               [1]] )

print(conjgrad(A, b, x))
