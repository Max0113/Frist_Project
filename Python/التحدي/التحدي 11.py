
# cette functions est pour creay un nevele array que contien le element Similaire entre le deux array input 1 et 2

# input
array1_s = ["hello", 2, 3, 66, 55, 66 , 77]
array2_s = ["hi", "hello", 3, 5, 3, 44, 66]
array3 = []

# functions
def liste(array1,array2) :
    for i in array1 :
        for j in array2 :
            if i == j :
                array3.append(i)
                break
    return array3

# output
print(liste(array1_s,array2_s))