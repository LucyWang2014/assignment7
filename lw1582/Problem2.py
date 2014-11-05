import numpy as np

def divideArray ():
    '''this is the code for all of Problem 2'''

    # generate a 5 x 5 array from o to 24
    a = np.arange(25).reshape(5,5)

    # set the elements of b, an array to be divided by a
    b = np.array([1.,5,10,15,20])
    
    #add x-axis to b and divide each column by b
    c = a / b[np.newaxis,:]
    
    return a, b, c 
    
def main():
    #main function for Problem 2 output
    a, b, c =divideArray()
    print "a is = " + '\n' + np.array_repr(a, precision = 2)
    print "each column divided by b = " + np.array_repr(b, precision = 2)
    print "is equal to " + '\n' + np.array_repr(c, precision = 2)

if __name__ == "__main__":
    main()