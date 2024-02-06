"""
F1 – Feature 1: Social Network Data
i. Open social network file:
this sub-feature should allow the user to enter a file name and prompt an error message if the file cannot be
opened. The process should continue to as ask for a valid file name until the file can be opened or the user
types "n".
7
0 2
2 1
2 4
3 5
4 1
6

or
Adam
Chris
Amir
Bob
Zia Mia
 Liz
Page 5 | 17
ii. Simulate the social network structure:
• Get social network data:
once the file is opened successfully, read the file (following the format described in nw_data1.txt)
and dynamically create an appropriate data structure named social_NW to hold the social network so
that it can be used elsewhere in the code;
• Display social network:
ask the user where they want to display the social network read from the file. If they do, pretty print
(display nicely formatted) the social network on the PyCharm console
"""