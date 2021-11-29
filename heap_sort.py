def heapify(customList,n,i):
    #here i is the root index
    smallest=i
    left_index=2*i+1
    right_index=2*i+2
    if left_index<n and customList[left_index]<customList[smallest]:
        smallest=left_index
    if right_index<n and customList[right_index]<customList[smallest]:
        smallest=right_index

    if smallest!=i:
        customList[i],customList[smallest]=customList[smallest],customList[i]
        heapify(customList,n,smallest)

def heapSort(customList):
    n=len(customList)
    #rearranging the binary heap
    #this will only take the left elements
    for i in range(int(n/2)-1,-1,-1):
        heapify(customList,n,i)

    #extract from heap
    for i in range(n-1,0,-1):
        customList[i],customList[0]=customList[0],customList[i]
        heapify(customList,i,0)
    customList.reverse()


customList=[2,1,7,6,5,3,4,9,8]
heapSort(customList)
print(customList)

