def selection_sort(list1):
    n=len(list1)
    for i in range(n): #Step-1 : Iterate over the array
        #Step-2: Assume the first element is the smallest
        min_index = i

        #Step-3: Find the actual minimum element in the unsorted part
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index=j
        #Step-4 : Swap the found minimum element with the first unsorted element
        list1[i],list1[min_index]=list1[min_index],list1[i]
    return list1
    
#Example Usage
list1=[64,25,34,22,11,90,70]
print("Original Array: ", list1)
sorted_list=selection_sort(list1)
print("Sorted array using selection sort is: ", sorted_list)