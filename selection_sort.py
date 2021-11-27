def selectionSort(cl):
    for i in range(len(cl)):
        min_index=i
        for j in range(i+1,len(cl)):
            if cl[min_index]>cl[j]:
                min_index=j
        cl[i],cl[min_index]=cl[min_index],cl[i]
    print(cl)


customList=[2,1,7,6,5,3,4,9,8]
selectionSort(customList)