import DataEntryClass
testing.f1.data_creation()
#print(testing.DataEntry.data)
data=testing.DataEntry.data
ar=[[0 for i in range(len(data))] for j in range(len(data))]

for x in range(0,len(data)):
    for y in range(0,len(data)):
        commonVal=list(set(data[x]) & set(data[y]))
        """https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches"""
        if len(commonVal) == 0:
            continue
        else:
            ar[x][y]=len(commonVal)

for x in range(0,len(ar)):
    print(ar[x])

        #print(testing.DataEntry.data[x][y])
    #print()

#class CommonFriends:
    #pass
    # def __init__(self, data):

