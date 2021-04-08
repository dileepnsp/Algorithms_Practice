dict={}
def runLengthEncoding(string):
    # Write your code here.
    prev=""
    count=0
    result=""
    for i in string:
        if prev == "":
            prev=i
        if prev == i:
            count+=1
        else:
            count=0
            prev=i

        nines=0
        rest=0
        if value >= 10:
            nines=value//9
            rest=value%9
            result=result+nines*(str(9)+key)
            if rest > 0:
                result=result+str(rest)+key
        else:
            result = result + str(value)+str(key)
        #print(result)

    return result
print(runLengthEncoding("AAAAAAAAAAAAbbbbbbbbbbbbbccccccccccd111111111"))