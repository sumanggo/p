#week10_04.py

myfile = "c:\\s202444089\\khj_02.txt"

#type1
f = open(myfile, 'r')
pass #작업
f.close()

#type2
with open(myfile, 'r') as f:
    pass #작업
print()
