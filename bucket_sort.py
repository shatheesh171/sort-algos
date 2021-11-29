import math
from insertion_sort import insertionSort

def bucketSort(cl):
    numberOfBuckets=round(math.sqrt(len(cl)))
    maxValue=max(cl)
    arr=[]

    for i in range(numberOfBuckets):
        arr.append([])
    for j in cl:
        index_b=math.ceil(j*numberOfBuckets/maxValue)
        arr[index_b-1].append(j)
        
    for i in range(numberOfBuckets):
        arr[i]=insertionSort(arr[i])

    k=0
    for i in arr:
        for j in i:
            cl[k]=j
            k+=1
    return cl


customList=[2,1,7,6,5,3,4,9,8]
print(bucketSort(customList))

