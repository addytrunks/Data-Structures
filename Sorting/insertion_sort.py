# Useful when the list is almost sorted

numbers = [99,44,6,2,1,5,63,87,283,0,4]

def insertionSort(array):
    end = array[0]
    for i in range(1,len(array)):
        if array[i] < end:
           x = array.pop(i)
           for j in range(0,i):
               if x < array[j]:
                    array.insert(j,x)
                    break
        end = array[i]

    return array
