etudents = ["younes", "hamza", "mohamed", "ahmad"]
x = input ("quel le nam de le etudent?")
n = False
for i in etudents :
    if i == x :
        n = True
        break
if n == True :
    print (x ,"is there")
else :
    print (x ,"is not there")
    inscription = input ("please give me your name ? ")
    etudents.append(inscription)
print (etudents)