import os; os.system("cls")

# def bubble_sort(list_to_sort):
#     for i in range(len(list_to_sort)):
#         for j in range(len(list_to_sort) - i - 1):
#             if list_to_sort[j] > list_to_sort[j + 1]:
#                 list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
#     return list_to_sort

def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        swapped = False
        for j in range(len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True
        if not swapped:
            break
    return list_to_sort

list_to_sort = [4, 3, 2, 7, 1, 6, 5]
print(list_to_sort)
print(bubble_sort(list_to_sort))
