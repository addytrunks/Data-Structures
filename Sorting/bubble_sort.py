
numbers = [43,44,6,2,1,5,63,87,283,4,0]

def bubbleSort(array):
    length = len(array)
    # Outer Loop for checking the number of elements to push the highest digit to the left
    for i in range(0,length-1):
        # Inner loop for swapping the numbers
        for j in range(0,length-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
