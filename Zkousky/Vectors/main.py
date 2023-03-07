from modules import *
from os.path import join, dirname, realpath
    

if __name__ == "__main__":
    g = VectorGroup(join(dirname(realpath(__file__)),"vectors.txt"))
    g.add_vector(Vector("n", 7.3, 6.9, -3.5))
    print(g)
    print(g.sum_vectors())
    print(g.vectors[0].diff(g.vectors[1]))
    u = g.get_vector("u")
    v = g.get_vector("v")
    print(u.vect_mult(v))
    print(u.scal_mult(2))
