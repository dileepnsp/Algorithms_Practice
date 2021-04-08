str=" I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"
strs=str.split()
cnt=0
len=0
'''
for word in strs:
    print("word:",word," length:",word.strip().__len__())
    len=len+word.strip().__len__()
    cnt+=1
print("total words:",cnt,"words length:",len)
'''
len=0
words_length_list=[len+word.strip().__len__() for word in strs]
print("sum:",sum(words_length_list))
print("length:",words_length_list.__len__())
print("avg length:",(sum(words_length_list) / words_length_list.__len__()))

