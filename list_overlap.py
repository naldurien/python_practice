a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def overlap(lst1, lst2):
    length1 = len(lst1)
    length2 = len(lst2)
    overlap = []
    if length1 < length2:
        for i in lst2:
            if i in lst1:
                overlap.append(i)
    elif length1 > length2:
        for i in lst1:
            if i in lst2:
                overlap.append(i)
    print(overlap)

overlap(a, b)
