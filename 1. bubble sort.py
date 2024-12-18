#Bubble Sort

def bubble_sort(list1):
    n=len(list1)
    for i in range(n): # Total number of passes
        swapped =  False
        for j in range(0,n-i-1): #Compare Adjacent Elements up until the last element
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1], list1[j] #Swap the greater value
                swapped =  True
# If no swaps occured then the array is already sorted
        if not swapped:
            break
    return list1
    

#Example usage with an array

list1=[64,34,25,12,22,11,90] #Using a list to store various integers for sorting
print("Original Array: ", list1)
sorted_list = bubble_sort(list1)
print("Sorted array using bubble sort is :", sorted_list)