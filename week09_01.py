#week09_01.py

data1 = [1, 2, 3, 4]

summary = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = summary / len(data1)

print(summary)
print(maximum)
print(minimum)
print(average)

print("-" * 30)
for i in data1:
    print(i)

print("-" * 30)
for i in range(len(data1)):
    print(i)

print("-" * 30)
for i in range(len(data1)):
    print(f"data1[{i}]:{data1[i]}")

print("-" * 30)
for i in enumerate(data1):
    print(f"data1[{i[0]}]:{i[1]}")

print("-" * 30)
for i,j in enumerate(data1):
    print(f"data1[{i}]:{j}")

data2 = [
     [1, 2, 3]
    ,[10, 20]
    ,[11, 12, 13, 14]
    ]

print("-" * 30)
for i in data2:
    print(i)

print("-" * 30)
for i in data2:
    print("sum",sum(i))
    print("max",max(i))
    print("min",min(i))
    print("avg",sum(i)/len(i))

print("-" * 30)
for j,i in enumerate(data2):
    print(f"{j+1}번째 : {i}")
    print("sum",sum(i))
    print("max",max(i))
    print("min",min(i))
    print("avg",sum(i)/len(i))

print("-" * 30)
for j,i in enumerate(data2):
    print(f"{j+1}번째 :", end = "")
    for v, m in enumerate(i):
        print(f"[{v}]{m} ",end = "")
    print()
    print("sum",sum(i))
    print("max",max(i))
    print("min",min(i))
    print("avg",sum(i)/len(i))

data3 = {
    "김인하":[1, 2],
    "이인하":[10, 20, 30, 40, 50, 60, 70],
    "송인하":[11, 12, 13, 14]
    }

print("-" * 30)

for k in data3:  # data3.keys()키 data3.values()데이터 data3.items()튜플
    print(k)

print("-" * 30)

for k in data3:
    print(data3[k])

print("-" * 30)

for k in data3:
    print(f"{k}:{data3[k]}")

print("-" * 30)

for k in data3:
    v = data3[k]
    print(f"{k} :", end = "")
    for i2, v2 in enumerate(v):
        print(f"[{i2}]{v2} ",end = "")
    print()
    print("sum",sum(v))
    print("max",max(v))
    print("min",min(v))
    print("avg",sum(v)/len(v))











