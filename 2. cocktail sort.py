
def cocktail_sort(list1):
    n=len(list1)
    start = 0
    end = n-1
    swapped = True
    while swapped:
        swapped = False
        #Left to Right Swappping similar to Bubble Sort
        for i in range(start,end):
            if list1[i]>list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = True
        if not swapped: #Break if no swaps are made
            break
        swapped =  False
        end -=1 #Reduce the range as the largest element is already in its place

        #Right to left pass

        for i in range(end-1, start-1,-1):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
                swapped =  True
        start +=1 #Increment the range as the smallest element is already in its place
    return list1

#Example usage 
list1 = [64,34,25,12,22,11,90]
print("Original Array: ", list1)
sorted_list = cocktail_sort(list1)
print("Sorted array using cocktail sort is: ", sorted_list)

#Biderectional Bubble sort is also known as Cocktail Sort
#In this sort, we sort the array in both directions alternatively
#The first pass sorts the array from left to right
#The second pass sorts the array from right to left
#This process continues until no swaps are made
#The array is then sorted
#The sort is stable and adaptive
#The sort is not suitable for datasets with vectors, heaps, matrices, arrays, tuples, sets, dictionaries, graphs, trees, linked lists, hash tables, queues, stacks, strings, floating point values, negative values, duplicate values, small values, large values, nearly sorted datasets, large datasets
#The sort is suitable for datasets with integers, positive values, unique values, medium sized datasets, random datasets, small datasets

#Time Complexity: O(n^2)
#Space Complexity: O(1)
#Stable: Yes
#Adaptive: Yes
#Method: Exchanging
#In-Place: Yes

