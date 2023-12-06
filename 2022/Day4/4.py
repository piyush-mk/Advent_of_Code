def prep(line):
  a, b = line.split(',') # split the line into two strings
  a, b = a.split('-'), b.split('-') # split each string into two strings
  a = list(range(int(a[0]), int(a[1])+1)) # convert each string into a list of integers
  b = list(range(int(b[0]), int(b[1])+1)) # convert each string into a list of integers
  return a,b # return the two lists

def contains(line):
  a,b = prep(line) # get the two lists
  return 1 if all(num in a for num in b) or all(num in b for num in a) else 0 # return 1 if all numbers in b are in a or all numbers in a are in b

def overlaps(line):
  a,b = prep(line)  # get the two lists
  return 1 if any(num in a for num in b) else 0 # return 1 if any numbers in b are in a

with open("input4.txt") as text_file:
  pairs = text_file.read().strip().split('\n')  # read the file and split it into a list of strings
  print(sum(map(contains, pairs)))  # print the sum of the results of the contains function
  print(sum(map(overlaps, pairs)))  # print the sum of the results of the overlaps function