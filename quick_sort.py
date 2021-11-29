def partition(customList,low,high):
    #this is a helper function, so the low and high are according to the partitions
    #main logic is nos greater than pivot stay where they are and less are swapped with i
    #and at last pivot is swapped with non low value, so that larger ones are automatically to 
    #right of pivot
    i=low-1
    pivot=customList[high]
    for j in range(low,high):
        if customList[j]<=pivot:
            i+=1
            customList[i],customList[j]=customList[j],customList[i]

    #Swap the pivot
    customList[i+1],customList[high]=customList[high],customList[i+1]
    #the partion element index is returned
    return (i+1)

def quickSort(customList,low,high):
    if low<high:
        pi=partition(customList,low,high)
        quickSort(customList,low,pi-1)
        quickSort(customList,pi+1,high)
        #pi is already sorted



customList=[2,1,7,6,5,3,4,9,8]
quickSort(customList,0,8)
print(customList)

