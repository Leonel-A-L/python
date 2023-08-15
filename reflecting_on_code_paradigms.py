def flatten_sort(lst):
    flat_list = []
    for i in lst:
        for j in i:
            flat_list.append(j)
        
    return sorted(flat_list)


