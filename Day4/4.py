def prep(line):
  a, b = line.split(',')
  a, b = a.split('-'), b.split('-')
  a = list(range(int(a[0]), int(a[1])+1))
  b = list(range(int(b[0]), int(b[1])+1))
  return a,b

def contains(line):
  a,b = prep(line)
  return 1 if all(num in a for num in b) or all(num in b for num in a) else 0

def overlaps(line):
  a,b = prep(line)
  return 1 if any(num in a for num in b) else 0

with open("input4.txt") as text_file:
  pairs = text_file.read().strip().split('\n')
  print(sum(map(contains, pairs)))
  print(sum(map(overlaps, pairs)))