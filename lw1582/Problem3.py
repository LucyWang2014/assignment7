import numpy as np

def Problem3():
    '''this is the code for part a to c of Problem 3'''

    #generate a 10 x 3 array of random numbers in range [0,1]
    array = np.random.rand(10,3)

    #sort index of each row by number that's closest to 0.5 
    order = np.argsort(abs(array-0.5), axis=1)

    #rearrange each row so the first column is the number that's closest to 0.5
    a = array[np.arange(array.shape[0])[:, None],order]
    
    # using argmin to find the column for each of the numbers closest to 0.5
    b = np.argmin(abs(array-0.5), axis = 1)

    #extract the numbers into an array
    c = [array[i, b[i]] for i in range(0,b.size)]

    return array, a, b, c

def main():
    '''this is the main function for Problem 3 outputs'''
    array, a, b, c = Problem3()

    print ("the 10 * 3 array is \n {} \n the number closest to 0,5 for each row is in the first column \n {} \n to the column with closest value to 0.5 for each row is \n {} \n and these numbers are: \n {} \n".format(array, a, b, c))

if __name__ == "__main__":
    main()
