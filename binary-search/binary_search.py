def binary_search(lst, to_find):
    if to_find in lst:
        mid = len(lst)//2
        while lst[mid] != to_find:
            if lst[mid] > to_find:
                mid = len(lst[:mid])//2
            else: 
                mid = (len(lst[mid:])//2)+len(lst[:mid])
        return mid
    return -1