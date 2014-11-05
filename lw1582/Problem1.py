'''numpy is used for array calculations'''
import numpy as np

def Problem1():
    '''this is the code for part a to d of Problem 1'''  

    #generate a 5 x 3 array from 1 to 15
    array = np.arange(1,16).reshape(3,5).T
    
    #generate an array that contains the 2nd and 4th row
    a = array[[1,3],:]
    
    #Generate a new array with the 2nd column
    b = array[:,1]
  
    #generate an array that contains elements in the rectangular section between the coordinates [1,0] to [3,2]
    c = array[1:4,0:3]

    #generate new array that only contains elements between 3 and 11; using fancy indexing
    mask = (2 < array) * (array < 12)
    indices = np.where(mask)
    
    d = array[indices]

    

    return array, a, b, c, d

def main():
    
    '''main method for the problem outputs'''
    array, a, b, c, d = Problem1()
    print ("the original array is \n {} \n the new array containing the 2nd and 4th rows is \n {} \n a new array with only the second column is \n {} \n a new array in with coordinates [1,0] to [3,2] is \n {} \n a new array with only elements between the value 3 and 11 is \n {}".format(array, a, b, c, d))

if __name__ == "__main__":
    main()