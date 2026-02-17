import numpy as np
import math
# from scipy.constants import m_e, e, hbar

def test():
    print(f"Hello world!")

def meowbot():

    meowing = True
    n_e = 10e18 # m^-3 electron number density
    e = 1.6e-19 #  elementary charge of electron
    m_e = 9.1e-31 # effective mass of an electon
    e_0 = 8.85e-12 # vacuum permittivity
    w = 1.0e12    # angular frequency of em wave

    if meowing:
        w2_p = (e ** 2 * n_e) / m_e * e_0
        return w2_p

def main():
    print(meowbot())
    test()

if __name__ == "__main__":
    main()