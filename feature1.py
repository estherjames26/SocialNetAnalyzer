import os
import numpy as np
"""
as long as the user's input isn't n, the program will open the file.
if the user doesn't input a valid file the program will ask for one until the input's n or something valid
nw_data.txt
28-30.12.22
"""
# ----------------------------------------------------classes-----------------------------------------------------------


class DataEntry:
    lineCount = 0
    arr = []
    data = []
    NoOfIDs = 0

    def __init__(self, file_name):
        self.FileName = file_name

    def data_creation(self):

        """this part reads the file and simultaneously counts for many lines are in the file
        and stores the value in a variable to be used later in this section(here it's t)
        29-30.12.22
        """
        file = open(self.FileName, "r")

        for a in file.readlines():
            DataEntry.arr.append(a.split())
            DataEntry.lineCount = DataEntry.lineCount + 1
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
        for p in range(0, int(DataEntry.NoOfIDs)):
            print(p, "->", ', '.join(str(x) for x in DataEntry.data[p]))


class Member(DataEntry):
    ar = []

    def __init__(self, file_name, user_id):
        super().__init__(file_name)
        self.m_ID = user_id

    def cm_forming(self):
        data = DataEntry.data
        Member.ar = [[0 for i in range(len(data))] for j in range(len(data))]

        for x in range(0, len(data)):
            for y in range(0, len(data)):
                commonval = list(set(data[x]) & set(data[y]))
                """https://stackoverflow.com/questions/1388818/how-can-i-
                compare-two-lists-in-python-and-return-matches"""
                if len(commonval) == 0:
                    continue
                else:
                    Member.ar[x][y] = len(commonval)
        for x in range(len(Member.ar)):
            print(x, "->", Member.ar[x])
        print()

    def friend_reccomend(self):
        for x in range(len(Member.ar)):
            Member.ar[x][x] = 0
        arrr = np.array(Member.ar)
        i = np.max(arrr[self.m_ID])
        """https://sparkbyexamples.com/numpy/calculate-maximum-numpy-array/"""
        if np.sum(arrr[self.m_ID]) == 0:
            ind = "n/a"
        else:
            ind = Member.ar[self.m_ID].index(i)
        """https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array"""
        print("recommended friends is/are", ind)


class Analytics:
    def __init__(self):
        pass

    def display_no_friends(self):
        pass

    def show_least_n_low_friends(self):
        pass

    def show_relationships(self):
        pass

    def show_indirect_relationships(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------
entry = input("Enter the full name of a file or enter n.\n")


if entry != "n":
    try:
        nw_file = open(entry, "r")
    except FileNotFoundError:
        entry = input("Doesn't work. Enter the full name of a file or enter n.\n")
    else:
        while os.path.getsize(entry) == 0:
            """https://bobbyhadz.com/blog/python-check-if-file-is-empty"""
            entry = input("The file is empty. Enter the full name of another file or enter n.\n")

        f1 = DataEntry(entry)
        f1.data_creation()
        opt = str(input("Do you want to see the data? type y or n"))
        while opt != "y" and opt != "n":
            opt = str(input("Invalid output.\nDo you want to see the data? type y or n\n"))
        if opt == "y":
            f1.output_data()
        else:
            print()
        id_opt = int(input("Enter a member id"))
        f2 = Member(entry, id_opt)
        f2.cm_forming()
        f2.friend_reccomend()


print("program has ended")
