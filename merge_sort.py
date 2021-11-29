def merge(cl,first,middle,last):
    #size of left and right sub array
    n1=middle-first+1
    n2=last-middle
    #left and right sub array 
    L=[0]*n1
    R=[0]*n2

    #adding elements to the left and right sub-array
    for i in range(n1):
        L[i]=cl[first+i]
    for j in range(n2):
        R[j]=cl[middle+1+j]

    i=0
    j=0
    k=first
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            cl[k]=L[i]
            i+=1
        else:
            cl[k]=R[j]
            j+=1
        k+=1

    #For any remaining elems of left or right subs
    while i<n1:
        cl[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        cl[k]=R[j]
        j+=1
        k+=1


def mergeSort(customList,l,r):
    #l-left index , r-right index
    if l<r:
        m=(l+(r-1))//2
        #this is floor division by 2
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)
    return customList


customList=[2,1,7,6,5,3,4,9,8]
print(mergeSort(customList,0,8))

