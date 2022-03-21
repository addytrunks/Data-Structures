
numbers = [99,44,6,2,1,5,63,87,283,0,4]

def selectionSort(array):

    for i in range(0,len(array)):
        min = i
        for j in range(i,len(array)):
            if array[j] < array[min]:
                min = j
        array[i],array[min] = array[min],array[i]

    return array
            
