import numpy as np

class DataEntry:
    lineCount = 0
    arr = []
    data = []
    NoOfIDs = 0

    def __init__(self, file_name):
        self.FileName = file_name

    def data_creation(self):

        """this part reads the file and simultaneously counts hor many lines are in the file
        and stores the value in a variable to be used later in this section(here it's t)
        29-30.12.22
        """
        file = open(self.FileName, "r")

        for a in file.readlines():
            DataEntry.arr.append(a.split())
            DataEntry.lineCount = DataEntry.lineCount+1
        """This part just sets up the data array so they it can be appended later on by adding
         the arrays x index into each array in the 2d array(mildly unnecessary but meh it 
         makes the rest work so"""
        DataEntry.data = [[0 for i in range(1)] for j in range(int(DataEntry.arr[0][0]))]
        for x in range(0, int(DataEntry.arr[0][0])):
            DataEntry.data[x][0] = x

        DataEntry.NoOfIDs = DataEntry.arr[0][0]
        """ this cuts out the first line(it's just to say how may users are in the social network"""
        del DataEntry.arr[0]
        """so it's easier to get rid of it and store it's value somewhere"""

        """the nested for loop here (WAAAAAAAAAAA) goes through each user ID that's already in
         the data array by default and comparing it with each [x][0] in the array with the unprocessed data """
        for z in range(0, len(DataEntry.arr)):
            for y in range(0, int(DataEntry.NoOfIDs)):
                try:
                    if int(DataEntry.arr[z][0]) == int(DataEntry.data[y][0]):
                        DataEntry.data[y].append(int(DataEntry.arr[z][1]))
                        DataEntry.data[int(DataEntry.arr[z][1])].append(int(DataEntry.arr[z][0]))
                except IndexError:
                    continue
        for p in range(0, len(DataEntry.data)):
            del DataEntry.data[p][0]
            DataEntry.data[p] = list(set(DataEntry.data[p]))
            """https://www.simplilearn.com/tutorials/python-tutorial/remove-duplicates-from-list-python"""

    def output_data(self):
        """This pretty prints the data...whatever that is"""
        print(DataEntry.data)
        for p in range(0, int(DataEntry.NoOfIDs)):
            print(p, "->", ', '.join(str(x) for x in DataEntry.data[p]))

class Member(DataEntry):
    ar=[]
    def __init__(self, file_name,user_id):
        super().__init__(file_name)
        self.m_ID=user_id

    def CMForming(self):
        data = DataEntry.data
        Member.ar = [[0 for i in range(len(data))] for j in range(len(data))]

        for x in range(0, len(data)):
            for y in range(0, len(data)):
                commonVal = list(set(data[x]) & set(data[y]))
                """https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches"""
                if len(commonVal) == 0:
                    continue
                else:
                    Member.ar[x][y] = len(commonVal)
        for x in range(len(Member.ar)):
            print(x,"->",Member.ar[x])
        print()


    def FriendReccomend(self):
        ind=0
        for x in range(len(Member.ar)):
            Member.ar[x][x]=0
        arrr=np.array(Member.ar)
        i=np.max(arrr[self.m_ID])
        """https://sparkbyexamples.com/numpy/calculate-maximum-numpy-array/"""
        if np.sum(arrr[self.m_ID]) == 0:
            ind = "n/a"
        else:
            ind = Member.ar[self.m_ID].index(i)
        """https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array"""

        print("recommended friends is/are",ind)





f1 = Member("nw_data.txt",6)
f1.data_creation()
f1.CMForming()
f1.FriendReccomend()