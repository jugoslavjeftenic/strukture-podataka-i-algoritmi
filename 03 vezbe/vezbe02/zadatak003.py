import os; os.system("cls")

def selection_sort(list_to_sort):
    unsorted_idx = 0

    while unsorted_idx < len(list_to_sort):
        lowest_idx = unsorted_idx
        
        for n in range(unsorted_idx + 1, len(list_to_sort)):
            if list_to_sort[lowest_idx] > list_to_sort[n]:
                lowest_idx = n
        
        list_to_sort[lowest_idx], list_to_sort[unsorted_idx] = list_to_sort[unsorted_idx], list_to_sort[lowest_idx]
        unsorted_idx += 1
    
    return list_to_sort

list_to_sort = [5, 6, 3, 2, 7, 0]
print(list_to_sort)
print(selection_sort(list_to_sort))
