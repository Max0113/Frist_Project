student = [
    [10,20,10],
    [5,7,9],
    [2,1,9]
]

j = 0
u = 0
y = 0

for i in student[0] :
    j += i
for n in student[1] :
    u += n
for m in student[2] :
    y += m

student[0].append(j)
student[1].append(u)
student[2].append(y)

print (student)