#week09_02.py

data2 = [
     [1, 2, 3]
    ,[10, 20]
    ,[11, 12, 13, 14]
    ]

data3 = {
    "김인하":[1, 2],
    "이인하":[10, 20, 30, 40, 50, 60, 70],
    "송인하":[11, 12, 13, 14]
    }
def print_info(datas):
    for i2, v2 in enumerate(datas):
        print(f"[{i2}]{v2} ",end = "")
    print()
    print("sum",sum(datas))
    print("max",max(datas))
    print("min",min(datas))
    print("avg",sum(datas)/len(datas))

def analyze_list(datas):
    for i,v in enumerate(datas):
        print(f"{i+1}번째 :", end = "")
        print_info(v)

def analyze_dict(datas):
    for k in datas:
        v = datas[k]
        print(f"{k} :", end = "")
        print_info(v)

def analyze_score(datas):
    if isinstance(datas, list):
        analyze_list(datas)
    elif isinstance(datas, dict):
        analyze_dict(datas)
    else:
        print("분석 불가")

analyze_list(data2)
analyze_dict(data3)
analyze_score(data3)



