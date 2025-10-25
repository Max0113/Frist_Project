un = []
def remove_duplicates(lst):
    for i in lst :
        if i not in un :
            un.append(i)
    print(un)

remove_duplicates([5 ,5 ,6 ,7 ,8 ,8])