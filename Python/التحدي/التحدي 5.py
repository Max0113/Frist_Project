numbers = [5, 20, 203, 555, 1023, 21, 17, 0, 60, 125, 63]
index = 0
while index < len(numbers) :
    n = numbers[index] % 5
    if n == 0 :
       print (numbers[index])
    index += 1
    if numbers[index] == 0 :
      break