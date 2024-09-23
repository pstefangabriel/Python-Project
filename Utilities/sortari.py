def partition(l,left,right, key, reverse, cmp):
    """
    Split the values:
    smaller pivot greater
    return pivot position
    post: left we have < pivot
    right we have > pivot
    """
    pivot = l[left]
    i = left
    j = right
    if key != None:
        if reverse == False:
            while i!=j:
                while key(l[j])>=key(pivot) and i<j:
                    j = j-1
                l[i] = l[j]
                while key(l[i])<=key(pivot) and i<j:
                    i = i+1
                l[j] = l[i]
        elif reverse == True:
            while i != j:
                while key(l[j]) <= key(pivot) and i < j:
                    j = j - 1
                l[i] = l[j]
                while key(l[i]) >= key(pivot) and i < j:
                    i = i + 1
                l[j] = l[i]
    else:
        if cmp == None:
            if reverse == False:
                while i != j:
                    while l[j] >= pivot and i < j:
                        j = j - 1
                    l[i] = l[j]
                    while l[i] <= pivot and i < j:
                        i = i + 1
                    l[j] = l[i]
            elif reverse == True:
                while i != j:
                    while l[j] <= pivot and i < j:
                        j = j - 1
                    l[i] = l[j]
                    while l[i] >= pivot and i < j:
                        i = i + 1
                    l[j] = l[i]
        else:
            if reverse == False:
                while i != j:
                    while cmp(l[j], pivot) >= 0 and i < j:
                        j = j - 1
                    l[i] = l[j]
                    while cmp(l[i], pivot) <= 0 and i < j:
                        i = i + 1
                    l[j] = l[i]
            elif reverse == True:
                while i != j:
                    while cmp(l[j], pivot) <= 0 and i < j:
                        j = j - 1
                    l[i] = l[j]
                    while cmp(l[i], pivot) >= 0 and i < j:
                        i = i + 1
                    l[j] = l[i]
    l[i] = pivot

    return i

def quickSortRec(l, left, right, key = None, reverse = False, cmp = None):
    #partition the list
    pos = partition(l, left, right, key, reverse, cmp)
    #order the left part
    if left<pos-1:
        quickSortRec(l, left, pos-1, key, reverse, cmp)
    #order the right part
    if pos+1<right:
        quickSortRec(l, pos+1, right, key, reverse, cmp)

#lista = ["apple", "banana", "kiwi", "orang"]
#quickSortRec(lista, 0, 3, key = lambda x : len(x))
#print(lista)

# lista = ["banana", "apple", "orange", "kiwi"]
# quickSortRec(lista, 0, 3, cmp = lambda x, y : 0 if x == y else
#                                                         1 if x > y else
#                                                         -1 if x < y else 0)
# print(lista)

def gnomeSort (l, key = None, reverse = False, cmp = None):
    index = 0

    while index < len(l):
        if index == 0:
            index += 1
        if key == None:
            if cmp == None:
                if reverse == False:
                    if l[index] >= l[index - 1]:
                        index += 1
                    else:
                        aux = l[index]
                        l[index] = l[index - 1]
                        l[index - 1] = aux
                        index -= 1
                else:
                    if l[index] <= l[index - 1]:
                        index += 1
                    else:
                        aux = l[index]
                        l[index] = l[index - 1]
                        l[index - 1] = aux
                        index -= 1
            else:
                if reverse == False:
                    if cmp(l[index], l[index - 1]) >= 0:
                        index += 1
                    else:
                        aux = l[index]
                        l[index] = l[index - 1]
                        l[index - 1] = aux
                        index -= 1
                else:
                    if cmp(l[index], l[index - 1]) <= 0:
                        index += 1
                    else:
                        aux = l[index]
                        l[index] = l[index - 1]
                        l[index - 1] = aux
                        index -= 1
        else:
            if reverse == False:
                if key(l[index]) >= key(l[index - 1]):
                    index += 1
                else:
                    aux = l[index]
                    l[index] = l[index - 1]
                    l[index - 1] = aux
                    index -= 1
            else:
                if key(l[index]) <= key(l[index - 1]):
                    index += 1
                else:
                    aux = l[index]
                    l[index] = l[index - 1]
                    l[index - 1] = aux
                    index -= 1

#lista = ["apple", "bananaa", "kiwi", "orange"]
#gnomeSort(lista, key = lambda x : len(x), reverse = False)
#print(lista)

# lista = ["banana", "apple", "orange", "kiwi"]
# gnomeSort(lista, reverse = True, cmp = lambda x, y : 0 if x == y else
#                                                      1 if x > y else
#                                                     -1 if x < y else 0)
# print(lista)