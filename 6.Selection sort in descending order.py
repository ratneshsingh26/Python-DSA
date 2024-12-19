def selection_sort_descending(list1):
    n = len(list1)
    for i in range(n):
        # Step-1: Assume the first unsorted element is the maximum
        max_index = i

        # Step-2: Find the actual maximum element in the unsorted part
        for j in range(i+1, n):
            if list1[j] > list1[max_index]:
                max_index = j

        # Step-3: Swap the found maximum element with the first unsorted element
        list1[i], list1[max_index] = list1[max_index], list1[i]

    return list1

# Example usage
list1 = [9, 1, 3, 5, 6, 8, 7, 8]
print("Original array:", list1)
sorted_list = selection_sort_descending(list1)
print("Sorted array using selection sort in descending order:", sorted_list)
