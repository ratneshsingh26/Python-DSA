def recursive_bubble_sort(list1,n=None):
    if n is None:
        n = len(list1)
    if n ==1: #Base Case: List of size 1 is already sorted
        return list1
    #Perform One pass of Bubble Sort

    for i in range(n-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]

            #Recusrive call for the remaining unsorted array
    return recursive_bubble_sort(list1, n-1)

#Example usage
list1=[3,2,1,5,4]
print("Sorted list using recursive bubble sort:", recursive_bubble_sort(list1))
