import multiprocessing
import time



def square(x):
    return x*x



   
if __name__ == '__main__':
    #multiprocessing pool object
    
    pool = multiprocessing.Pool()
    # pool object with number of element
    
    pool = multiprocessing.Pool(processes=4)
    
    #input list
    inputs = [0,1,2,3,4]
    
    #map the function to the list and pass
    #function and input list as arguments 
    outputs = pool.map(square, inputs)
    
    print("Input: {}".format(inputs))
    print("Output: {}".format(outputs))