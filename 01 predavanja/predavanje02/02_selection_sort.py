import os; os.system("cls")

def selection_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        min_value = list_to_sort[i]
        min_index = i
        for j in range(i, len(list_to_sort)):
            if list_to_sort[j] < min_value:
                min_value = list_to_sort[j]
                min_index = j
        list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]
    return list_to_sort

list_to_sort = [4, 3, 2, 7, 1, 6, 5]
print(list_to_sort)
print(selection_sort(list_to_sort))
