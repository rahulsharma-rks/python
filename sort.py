def sort(lst):
    if not  lst:
        return []
    else:
        return (sort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            sort([x for x in lst[1:] if x >= lst[0]]))



str_1 =  ['a','b','k','y','w','v','s','k','m','s','f','j','w','y','a','x',
    'l','s','d','m','b','s','d','f','j','h','g','s','k','l','m','d','f','s']
sorted_list = sort(str_1)
print(sorted_list)
