print("------------- mthode 1 ----------")

def max_and_min(array) :
    maxumal = array[0]
    minmal = array[0]
    for i in array :
        if i > maxumal :
            maxumal = i 
    for i in array :
        if i < minmal :
            minmal = i 
    return maxumal , minmal 

array1 = [10,20,30,5,100,22,6,7]
print(max_and_min(array1))

print("------------- mthode 2 ----------")

array2 = [12, 23, 334, 45, 3 ,4 ,44]
n = max(array2)
u = min(array2)
print((n , u))