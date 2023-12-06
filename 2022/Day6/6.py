import os
filename = "input6.txt"
with open(filename, "r") as f:
    content = f.read()  
def func(distinct):
    global content
    for i in range(distinct-1, len(content)):               
        templst = [content[i-x] for x in range(distinct)]   # create a list of the last distinct characters
        if templst == list(dict.fromkeys(templst)):        # if the list contains no duplicates
            return str(i+1)                               # return the index of the first character in the list
print("Part 1:", func(4))   # print the index of the first character in the list of the last 4 characters
print("Part 2:", func(14))  # print the index of the first character in the list of the last 14 characters