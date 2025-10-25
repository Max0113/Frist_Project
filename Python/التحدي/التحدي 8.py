def alternate_case(text):
    result = ''
    counte = 0
    for char in text :
        if counte % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
        counte += 1
    return result

# Example usage
strang = "hello world"
output = alternate_case(strang)
print(output)  # Output: HeLlO

# --------  mthode 2  ------------

def lower(text) :
    result2 = True
    hhh = ''
    for i in text :
        if result2 :
            hhh += i.upper()
            result2 = False
        else :
            hhh += i.lower()
            result2 = True
    return hhh
inpute = input()
print(lower(inpute))