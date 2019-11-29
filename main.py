import matplotlib.pyplot as plt
from sympy import *
import numpy as np

ALPHA = 0.2
THETA = 0.2
B = 1.2
GAMMA = 1.38
C_0_CONST = 0
L_0_CONST = 0
N = 100

# двумерная OLG система
def f(c, l):
    return pow(pow(l, GAMMA) - pow(c, THETA), 1 / ALPHA), B * (l - c)


# точки покоя
def equilibrium():
    c = symbols('c')
    x = np.array(solve(c ** ALPHA - (B * c / (B - 1)) ** GAMMA + c ** THETA))
    y = B * x / (B - 1)
    return x, y


def plot(c_0=C_0_CONST, l_0=L_0_CONST):
    C = []
    L = []
    plt.scatter(c_0, l_0, s=10, color='red')
    for _ in range(N):
        c_0, l_0 = f(c_0, l_0)
        print(c_0, l_0)
        C.append(c_0)
        L.append(l_0)
    plt.scatter(C, L, s=1)
    plt.xlabel('$с$')
    plt.ylabel('$l$')
    #plt.title("$\\alpha = {2}, \\theta = {3}, c = {4}, l = {5}, \\gamma = {0}$, N = {1}".format(GAMMA, N, ALPHA, THETA, C_0_CONST, L_0_CONST))
    plt.show()
    #plt.savefig('C:\\Users\\user\\Desktop\\SPBU\\magistracy\\diploma\\fig\\OLG2mapHaoticAttractor.pdf')


x, y = equilibrium()
plot(x[1], y[1])

