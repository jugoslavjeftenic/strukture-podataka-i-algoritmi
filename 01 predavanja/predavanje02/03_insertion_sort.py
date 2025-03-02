import os; os.system("cls")

def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        value = list_to_sort[i]
        j = i
        while j > 0 and list_to_sort[j - 1] > value:
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1
        list_to_sort[j] = value
    return list_to_sort

list_to_sort = [4, 3, 2, 7, 1, 6, 5]
print(list_to_sort)
print(insertion_sort(list_to_sort))
