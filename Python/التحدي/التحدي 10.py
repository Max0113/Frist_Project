# c'est outil pour remplace une lettre dans une texte a un notre lettre moi je peux selecte


word = 'je m appelle younes'
print (word)
def remplace(lettre , lettre_remplace) :
    s = ""
    for i in word :
        if i == lettre :
            s += lettre_remplace
        else :
            s += i
    return s

# input

print (remplace("j","="))
