#week10_02.py

myfile = "c:\\s202444089\\khj_02.txt"

scores = {}

f = open(myfile, 'a')

while True:
    scores['m'] = int(input('math:'))
    scores['k'] = int(input('kor:'))
    scores['e'] = int(input('eng:'))

    data = ""
    for k, v in scores.items():
        if data:
            data += "|"
        data += f"{k}, {v}"
    f.write(f"{data}\n")

    if 'y' == input("종료(Y):").lower():
        break

f.close()

'''
myfile = "c:\\s202444089\\khj_01.txt"

scores = {}

f = open(myfile, 'a')

while True:
    scores['m'] = int(input('math:'))
    scores['k'] = int(input('kor:'))
    scores['e'] = int(input('eng:'))

    for k, v in scores.items():
        f.write(f"{k}, {v}\n")
    if 'y' == input("종료(Y):").lower():
        break

f.close()


myfile = "c:\\s202444089\\khj_01.txt"

scores = {'m':90, 'k':100, 'e':40}

f = open(myfile, 'a')

for k, v in scores.items():
    f.write(f"{k}, {v}\n")

f.close()
''' 
