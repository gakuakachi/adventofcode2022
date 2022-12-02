
f = open("1.txt")
datalist = f.readlines()

res = 0
cur = 0

for data in datalist:
  if not data.rstrip():
    res = max(res, cur)
    cur = 0
  else:
    cur += int(data)
print(res)