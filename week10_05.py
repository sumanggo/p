#week10_05.py
import os

mypath = "c:\\s202444089"
myfile = "khj_02.txt"

if False == os.path.exists(mypath):
    os.mkdir(mypath)

myfullfile = mypath + "\\" + myfile

if os.path.exists(myfullfile):
    scores = []
    with open(myfullfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            dict_scores ={}
            sub_scores = line.strip().split('|')
            for sub_score in sub_scores:
                kv = sub_score.split(',')
                dict_scores[kv[0]] = int(kv[1])
            if dict_scores:
                scores.append(dict_scores)
        
    if scores:
        for score in scores:
            print(score)
else:
    f = open(myfullfile, 'w')
    f.close()
