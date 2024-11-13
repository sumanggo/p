#week12_10.py

def test():
    raise NotImplementedError("test함수 미작성")

while True:
    try:
        dvd = int(input("피제수:"))
        dvs = int(input("제수:"))
        result = dvd / dvs
        print(result)
        test()
    except ValueError:
        print("올바른 값을 넣어줘")
    except ZeroDivisionError:
        print("제수는 0을 넣으면 안돼")
    except Exception as e:
        print(e)
    else:
        print("try문이 완벽히 실행하면 할 것")
    finally:
        print("안녕히계세여")
    #except:
    #    print("미안 죽었다")
        
