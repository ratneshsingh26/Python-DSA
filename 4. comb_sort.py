def comb_sort(list1):
    def get_next_gap(gap):
        #Shrink gap using a shrink factor of 1.3
        gap = (gap*10)//13
        return max(1,gap)
    n=len(list1)
    gap = n
    swapped=True
    while gap != 1 or swapped:
        gap=get_next_gap(gap)
        swapped=False
        for i in range(0,n-gap):
            if list1[i]>list1[i+gap]:
                list1[i], list1[i+gap]=list1[i+gap],list1[i]
                swapped= True
    return list1

#Example usage
list1=[9,8,8,4,0,1,1,5,7,9]
print("Original Array: ", list1)
print("Sorted array using comb sort is: ", comb_sort(list1))