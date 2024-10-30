#week10_01.py

myfile = "c:\\s202444089\\khj.txt"

#1. 열기
#f = open(myfile, 'w') #쓰기모드 (덮어쓰기)
f = open(myfile, 'a') #추가모드

#2. 작업
f.write("김현준\n")
#print(f.read()) 

#3. 닫기
f.close()



f = open(myfile, 'r') #읽기모드
print(f.read())
f.close



