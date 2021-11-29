def insertionSort(cl):
    for i in range(1,len(cl)):
        key=cl[i]
        j=i-1
        #Check if key is smaller than the sorted part, if it is then move elems to the right 
        #until key can be inserted
        while j>=0 and key<cl[j]:
            cl[j+1]=cl[j]
            j-=1
        cl[j+1]=key
    return cl

if __name__=='__main__':
    customList=[2,1,7,6,5,3,4,9,8]
    print(insertionSort(customList))
    