    str=" I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"

    #Consider the above text as a string, figure out the average length of the string.

    words = str.split()
    average = sum(len(word) for word in words) / len(words)
    average

    #Lower the text in the string.
    str1=str.lower()
    print(str1)
    import string

    #Try to get the clean text removing the punctuation from the string.

    table = str.maketrans(dict.fromkeys(string.punctuation))

    ## Extract word "Data Science" from the string.

    if "Data Sciences" in str:
        print("Data Science")

    ### Find the frequency of words used in the string

    strs=str.split()
    dict={}
    for word in strs:
        if word in dict.keys():
            dict[word]=dict.get(word)+1
        else:
            dict[word]=1
    print(dict)

    ### Fetch the duplicate pairs used in the string..

    duplicate_words=[ k for k,v in dict.items() if v > 1]
    print(duplicate_words)

    #Can you change the word "Supervised" to "Unsupervised" in the string

    str_repl=str.replace("Supervised","Unsupervised")
    print(str_repl)

    #Splitting of the string with a dot operator(.)

    str_dot=str.split(".")
    print(str_dot)

    ##Find the words from the string which ends with "e"

    endswith=[ word for word in strs if word.endswith("e")]
    print(endswith)

    #Figure out number of a's used in the string.

    print(str.count('a'))

    ''' In the weekend , I purchased 250g of apple, 500g of sugar, 2.5 kg of rice, 2.5 litres of milk and finally 1 dozen of egg.
    Can you help me frame the above purchase in the form of dictionary with commodities as keys to it.
    
    I forgot to mention another item, 1kg of atta packet. Can you also add it ?
    
    Instead of 2.5kg of rice, I bought only 1kg of rice. Can you change the corresponding value ?
    
    Can you list out all these items using a loop. '''

    groc_dict={"apple":.25,"sugar":.5,"rice":2.5,"milk":2.5,"egg":1}
    groc_dict["atta"]="1"
    groc_dict["rice"]="1"
    print(groc_dict)
    for k,v in groc_dict.items():
        print(k,":",v)

    price_dict={"apple":220,"sugar":43,"rice":45,"milk":30,"egg":60}
    total_cost=float(0.0)
    for groc,quant in groc_dict.items():
        if groc in price_dict:
            print("groc:",groc)
            total_cost=float(quant)*float(price_dict.get(groc))+total_cost
    print("total cost:",total_cost)

    ####Questions on List

    ai_companies=['Amazon','Facebook','HiSilicon','Google','Apple','Microsoft','SenseTime']
    #Sort the list in ascending order
    print(sorted(ai_companies))
    #Add multiple companies at once 'Nvidia', 'OpenAI' , 'Qualcomm' and 'Reliance' to the list
    ai_companies.extend(['Nvidia', 'OpenAI' , 'Qualcomm' , 'Reliance'])
    print(ai_companies)
    #Lower the list using List comprehension
    list_lower=[ str.lower() for str in ai_companies]
    print(list_lower)
    #Elimiate 'Reliance' from the list
    ai_companies.remove("Reliance")
    print(ai_companies)
    #Extract 'Facebook', 'Google'  using a single command
    newlist=['Facebook','Google']

    #Questions on Tuple
    #(a)Consider the above standard price problem statement and place the prices in the form of the tuple.
    price_tpl=(220,43,45,30,60)

    #(b)Find out the min and max price among them.
    print(min(price_tpl))
    print(max(price_tpl))
    #(c)Also, convert the above "AI_companies" list to a tuple.
    ai_companies=['Amazon','Facebook','HiSilicon','Google','Apple','Microsoft','SenseTime']
    ai_tpl=tuple(ai_companies)
    print(ai_tpl)
    #(d)Combine two above tuples to a single tuple.

    print(price_tpl+ai_tpl)

    #(e)Compare the length of two tuples.
    a=(5,6)
    b=(1,4)
    if (a>b):
        print("a is bigger")
    else: print("b is bigger")