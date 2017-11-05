import numpy as np
import random

def transform(X):
    # Make sure this function works for both 1D and 2D NumPy arrays.
    return X

def ocp_svm(X,Y, l):
    w = np.zeros(X.shape[1])
    for t in range(X.shape[0]):
        eta = 1.0 / np.sqrt(t+1)
        if Y[t]*np.dot(w, X[t]) < 1:
            w += eta*Y[t]*X[t]
            w = w * min(1., 1./(np.sqrt(l)*np.linalg.norm(w)))
    return w

def read_from_string(line):
    line = line.rstrip().split()
    y = float(line[0])
    x = np.array([float(i) for i in line[1:]])
    return y, x

def mapper(key, value):
    # key: None
    # value: one line of input file
    random.seed(22)
    random.shuffle(value)
    w = np.zeros(400) #init w as zero vector
    t = 1 #iteration
    C = 1 #parameter C
    num_ins = len(value) # number of instances
    for line in value:
        y, x = read_from_string(line)
        eta = 1.0 / np.sqrt(t)
        loss = 1 - y*np.dot(w,x)
        if loss > 0:
            w = w - eta*(w/num_ins - C*loss*y*x)
        else:
            w = w - eta*(w/num_ins)

    yield 0, w  # This is how you yield a key, value pair


def reducer(key, values):
    # key: key from mapper used to aggregate
    # values: list of all value for that key
    # Note that we do *not* output a (key, value) pair here.
    W = np.array(values)
    w = np.mean(W, axis=0)
    print(len(w))
    print(w.dtype)
    yield w
