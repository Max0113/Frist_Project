valeur1 = input ("hi , are you buy desk or chair or no? ")
valeur2 = input ("hi , are you buy chair or desk or no? ")
if (valeur1 == "desk" and valeur2 == "chair") or (valeur1 == "chair" and valeur2 == "desk") :
    print ("you have 90$")
elif (valeur1 == "chair" or valeur2 == "chair") or (valeur1 == "desk" or valeur2 == "desk") :
    print ("you have 50$")
else :
    print ("you have 0$")
