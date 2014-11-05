
'''numpy is used for array calculations and matplotlib used for plotting'''
import numpy as np
import matplotlib.pyplot as plt

def Problem4():
    '''this is the code for part a to c of Problem 4'''

    '''set max and threshold. due to overflow warnings, I'm setting the values at 10'''
    N_Max = 10
    some_threshold = 10
    
    '''construct a grid of c = x + 1j*y values in range [-2,1] x [-1.5,1.5]'''

    x,y = np.ogrid[-2:1:50j,-1.5:1.5:50j]
    c = x + 1j*y
    
    z = 0
    
    '''do the iteration'''
    for v in range(N_Max):
        z = z**2 + c
        mask = np.abs(z) < some_threshold
    
    '''i had originally set the mask to be outside of the loop, but to avoid overflow, i moved it inside the for loop. keeping the original code here for future needs'''
    # mask = np.abs(z) < some_threshold

    '''plot the result'''
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.show()
    plt.savefig('mandelbrot.png')

    return None

def main():
    '''main for Problem 4 output'''
    Problem4()

if __name__ == "__main__":
    main()