"""this part reads the file and simultaneously counts hor many lines are in the file
and stores the value in a variable to be used later in this section(here it's t)
29-30.12.22
"""
f = open("nw_data2.txt", "r")
arr = []
t = 0
for a in f.readlines():
    arr.append(a.split())
    t = t+1
"""This part just sets up the data array so they it can be appended later on by adding
 the arrays x index into each array in the 2d array(mildly unnecessary but meh it 
 makes the rest work so"""
data = [[0 for i in range(1)] for j in range(int(arr[0][0]))]
for x in range(0, int(arr[0][0])):
    data[x][0] = x
print(data)
N = arr[0][0]
""" this cuts out the first line(it's just to say how may users are in the social network"""
del arr[0]
"""so it's easier to get rid of it and store it's value somewhere"""

"""the nested for loop here (WAAAAAAAAAAA) goes through each user ID that's already in
 the data array by default and comparing it with each [x][0] in the array with the unprocessed data """
for z in range(0, len(arr)):
    for y in range(0, int(N)):
        try:
            if int(arr[z][0]) == int(data[y][0]):
                data[y].append(int(arr[z][1]))
                data[int(arr[z][1])].append(int(arr[z][0]))
        except IndexError:
                continue
print(data)
for p in range(0,len(data)):
    del data[p][0]
    data[p]=list(set(data[p]))
    """https://www.simplilearn.com/tutorials/python-tutorial/remove-duplicates-from-list-python#:~:text=If%20the%20order%20of%20the,keep%20the%20order%20of%20elements."""


"""This pretty prints the data...whatever that is"""
opt = input("Do you want to see the data? type y")
if opt == "y":
    for p in range(0, int(N)):
        print(p, "->", ', '.join(str(x) for x in data[p]))
else:
    print("complete")

