#characters="abcabc"
#document="aabbccc"
def generateDocument(characters, document):
    if len(document) > len(characters) :
        return False
    if len(document) == 0:
        return True
    map1={}
    map2 = {}
    for str in characters:
        if str in map1.keys():
            map1[str]+=1
        else:
            map1[str]=1
    for str in document:
        if str in map2.keys():
            map2[str]+=1
        else:
            map2[str]=1
    for key,value in map2.items():
        if key not in map1.keys():
            return False
        if map1[key] >=value:
            continue
        else:
            return False
    return True
#print(generateDocument("abcabc","aabbccc"))
#print(generateDocument("Bste!hetsi ogEAxpelrt x ","AlgoExpert is the Best!"))
#print(generateDocument("A","a"))
#print(generateDocument("a hsgalhsa sanbjksbdkjba kjx",""))
print(generateDocument("aheaollabbhb","hello"))
