#week10_03.py

myfile = "c:\\s202444089\\khj_02.txt"

f = open(myfile, 'r')
'''
#type1
d = f.read()
print(d)

#type2
while True:
    d = f.readline()
    if not d:
        break
    print(d.strip())
'''
#type3
d = f.readlines()
for line in d:
    print(line.strip())

f.close()
