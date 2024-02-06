import os
import numpy as np

"""
as long as the user's input isn't n, the program will open the file.
if the user doesn't input a valid file the program will ask for one until the input's n or something valid
nw_data.txt
"""

# ----------------------------------------------------classes-----------------------------------------------------------
NWData = 0


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
        file.seek(0, 0)
        """This part just sets up the data array so they it can be appended later on by adding
         the arrays x index into each array in the 2d array"""
        DataEntry.data = [[0 for i in range(1)] for j in range(int(DataEntry.arr[0][0]))]
        for x in range(0, int(DataEntry.arr[0][0])):
            DataEntry.data[x][0] = x

        DataEntry.NoOfIDs = DataEntry.arr[0][0]
        """ this cuts out the first line(it's just to say how may users are in the social network"""
        del DataEntry.arr[0]
        """so it's easier to get rid of it and store it's value somewhere"""

        """the nested for loop here goes through each user ID that's already in
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
        """resets the class"""
        file.seek(0)
        DataEntry.arr = []
        "Returns the information formed about the social network"
        return DataEntry.data

    @classmethod
    def output_data(cls):
        """This pretty prints the data"""
        for p in range(0, int(DataEntry.NoOfIDs)):
            print(p, "->", ', '.join(str(x) for x in DataEntry.data[p]))
        print()


class Member:
    ar = []

    @classmethod
    def cm_forming(cls):
        data = NWData
        """sets up Member.ar so that it's easy to append values to it later"""
        for x in range(0, len(data)):
            Member.ar.append([])
            for y in range(0, len(data)):
                Member.ar[x].append(0)

        print("Common friends")
        """"""

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

    @classmethod
    def friend_recommend(cls, f_id_opt):
        m_id = f_id_opt
        for x in range(len(Member.ar)):
            Member.ar[x][x] = 0
        arrr = np.array(Member.ar)
        i = np.max(arrr[m_id])
        """https://sparkbyexamples.com/numpy/calculate-maximum-numpy-array/"""
        if np.sum(arrr[m_id]) == 0:
            ind = "n/a"
        else:
            ind = Member.ar[m_id].index(i)
        """https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array"""
        print("recommended friends is/are", ind)


class Analytics(Member):
    def __init__(self):
        Member.__init__(self)

    @classmethod
    def display_num_friends(cls, m_id_opt):
        """This sub-feature should allow the user to enter a name or member ID and display the number of friends
        that the user has. It should validate that the input exists and prompt an error message otherwise"""
        try:
            print("User ID", m_id_opt, "has", len(NWData[m_id_opt]), "friends")
        except IndexError:
            print("Invalid member id")

    @classmethod
    def show_least_n_low_friends(cls):
        """Display all the users with the least number of friends and those with no friends at all. Pretty-print your
output on the PyCharm console."""
        smallest_len = 0
        no_friend = []
        smallest_arr = []
        """This for loop finds the number of the smallest amount of friends that's more than 0, and puts member ids with
        no friends into an array"""
        for x in range(0, len(NWData)):
            if 0 < len(NWData[x]) < len(NWData[x - 1]):
                smallest_len = len(NWData[x])
            elif len(NWData[x]) == 0:
                no_friend.append(str(x))
        """This for loop puts the member ids of ppl who have friend counts that match the calculated lowest friend 
        count in an array"""
        for y in range(0, len(NWData)):
            if len(NWData[y]) == smallest_len:
                smallest_arr.append(str(y))
        """pretty prints calculated info"""
        print("Member IDs with the smallest amount of friends:", ', '.join(smallest_arr),
              "\nMember IDs with no friends:", ', '.join(no_friend), "\n")

    @classmethod
    def show_relationships(cls):
        """This sub-feature should allow the user to enter a name or member ID and show all the friends that the
member is connected with in the social network. It should validate that the input exists and prompt an
error message otherwise. The output should display the relationships for that member."""
        rel_opt = int(input("Enter a member id"))
        try:
            print(rel_opt, "'s direct relationships:", ", ".join(str(n) for n in NWData[rel_opt]))
        except IndexError:
            print("Invalid input")

    @classmethod
    def show_indirect_relationships(cls):
        """For every member in the social network find the friends of all the direct friends of that member but do
not include the member themself. Friend of a friend relationships are indirect connections between
people and represent indirect relations between members. This sub-feature should return an appropriate
data structure with those connections and name it as indirect_friends The data structure only needs to
represent the first level of indirect relations (i.e., only contain the friends of direct friends of each
member). Pretty-print the elements of the data structure on the PyCharm console"""

        indi = []
        for z in range(0, len(Member.ar)):
            indi.append([])
            for y in range(0, len(Member.ar[z])):
                if int(Member.ar[z][y]) > 0:
                    indi[z].append(y)
        indirect = []
        for s in range(0, len(Member.ar)):
            indirect.append(list(map(str, (set(indi[s])-set(NWData[s])))))
            print(indirect[s])
        print(indi, "\n", NWData)
        return indirect


# ----------------------------------------------------------------------------------------------------------------------
def validation():
    """Update F1.ii to validate the social network data read from the file after it has been opened successfully.
This sub-feature should check the consistency of friendships (connections) in the network. The network
representation is considered consistent if member A is friends with member B AND member B is also
friends with member A. The network representation is inconsistent otherwise. If the network
representation is found to be inconsistent, raise an exception and prompt the user with an error message"""
    error_count = 0
    for a in range(0, len(NWData)):
        for b in range(0, len(NWData[a])):
            if_present = NWData[int(NWData[a][b])].count(int(a))
            if if_present == 1:
                continue
            else:
                error_count = error_count + 1
    return error_count
# ----------------------------------------------------------------------------------------------------------------------


entry = input("Enter the full name of a file or enter n.\n")
"""as long as the input isn't equal to n, the user's input will be checked to see if it is the name of a file"""
while entry != "n":
    try:
        nw_file = open(entry, "r")
    except FileNotFoundError:
        print("Doesn't work")
    else:
        while os.path.getsize(entry) == 0:
            """https://bobbyhadz.com/blog/python-check-if-file-is-empty"""
            entry = input("The file is empty. Enter the full name of another file or enter n.\n")

        """once it's confirmed that the found file isn't empty,object f1 is
        created and the file name is used in the object. NWdata, which is created is then validated. 
        An exception is raised if there is an inconsistency"""
        f1 = DataEntry(entry)
        NWData = f1.data_creation()
        check = validation()
        if check != 0:
            raise Exception("Network representation is inconsistent")
        else:
            opt = str(input("Do you want to see the data? type y or n\n"))
            while opt != "y" and opt != "n":
                opt = str(input("Invalid output.\nDo you want to see the data? type y or n\n"))
            if opt == "y":
                f1.output_data()
            else:
                print()

            f2 = Member()
            f2.cm_forming()
            id_opt = int(input("Enter a member id\n"))
            f2.friend_recommend(id_opt)
            """an object is created for analytics of the social network"""
            f3 = Analytics()
            """The options correspond to different methods in the analytics class"""
            opt = int(input("1:Display number of friends\n2:show least amount of friends\n"
                            "3:Show relationships\n""4:Show Indirect relationships\n5 to quit\n"))
            while opt != 5:
                if opt == 1:
                    opt2 = int(input("Enter a valid member id\n"))
                    f3.display_num_friends(opt2)
                elif opt == 2:
                    f3.show_least_n_low_friends()
                elif opt == 3:
                    f3.show_relationships()
                elif opt == 4:
                    indirect_friends = f3.show_indirect_relationships()
                    for t in range(0, len(indirect_friends)):
                        if len(indirect_friends[t]) == 0:
                            print("indirect friends of", t, ":", "n/a")
                        else:
                            print("indirect friends of", t, ":", ", ".join(indirect_friends[t]))

                else:
                    print("invalid input")
                opt = int(input("1:Display number of friends\n2:show least amount of friends\n"
                                "3:Show relationships\n""4:Show Indirect relationships\n5 to quit\n"))
    """The program is run until the user inputs n into entry"""
    entry = input("Enter the full name of a file or enter n.\n")

print("program has ended")
