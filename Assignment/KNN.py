import math
def euclideanDistance(instance1,instance2,length):
    distance=0
    for i in range(length):
        distance+=pow((instance1[i]-instance2[i]),2)
    return math.sqrt(distance)

data1=[2,2,2,'a']
data2=[4,4,4,'b']
distance=euclideanDistance(data1,data2,3)
print('distance:'+repr(distance))

from operator import itemgetter

def getNeighbors(trainingset,traininginstance,k):
    distances=[]
    for data in range(len(trainingset)):
        print(trainingset[data])
        distance=euclideanDistance(trainingset[data],traininginstance,3)
        distances.append((trainingset[data],distance))
    print(distances)
    distances.sort(key=itemgetter(1))
    neibors=[]
    for x in range(k):
        neibors.append(distances[x][0])
    return neibors
import operator
def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response] +=1
        else:
            classVotes[response]=1
    sortedVotes=sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]
trainingset=[[2,2,2,'a'],[4,4,4,'b']]
traininginstance=[5,5,5]
print("neighbors")
print(getNeighbors(trainingset,traininginstance,1))

neighbors=[[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
response=getResponse(neighbors)
print("response")
print(response)

def getAccuracy(testset,predictions):
    correct=0
    for x in range(len(testset)):
        if predictions[x] == testset[x][-1]:
            correct+=1
    return (correct/float(len(testset)))*100
testset=[[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
predictions=['a','a','a']
accuracy=getAccuracy(testset,predictions)
print("accuracy:"+str(accuracy))