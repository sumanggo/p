# week13_C_11_3.py
# id:202444089
# name:kim hyunjun

from week13_C_book import Book2 as Book
from week13_C_book  import TimeStamp
import datetime
from datetime import datetime as dt
import os

dtformat = "%Y-%m-%d %H:%M:%S"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    mypath = "c:\\book2_202444089"

    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = []

    members = os.listdir(mypath)
    for member in members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isfile(member_fullname):
            file_ext = os.path.splitext(member)
            if file_ext and len(file_ext) == 2 and file_ext[-1] == ".txt":
                number = file_ext[0].strip()
                book = Book(number)
                with open(member_fullname, 'r', encoding = "utf-8") as f:
                    for line in f:
                        split_datas = line.strip().split('|')
                        if split_datas and len(split_datas) == 2:
                            intime = dt.strptime(split_datas[0], str_fmt)
                            if split_datas[1].strip():
                                outtime = dt.strptime(split_datas[1], str_fmt)
                            else:
                                outtime = None

                            book.add_timestamp(intime,outtime)
                if book.history:
                    books.append(book)
    
    while True:
        number = input("도서번호:").strip()
        if not number:
            break

        search_book = [book for books in books if book.number == number]

        if not search_book:
            book = Book(number)
            books.append(book)
        else:
            book = search_book[0]
            for timestamp in book.history:
                if timestamp.is_rent():
                    print("반납을 안했어")
                    continue
                
        while True:
            try:
                intime = input("대출시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("반납시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                pass

        #times = {"in": intime, "out": outtime}
        #books[number].append(times)
        book.add_timestamp(intime,outtime)

        book_fullname = os.path.join(mypath, number + "txt")
        with open(book_fullname, 'a', encoding="utf-8") as f:
            intime = dt.strftime(intime,str_fmt)
            if outtime:
                outtime = dt.strftime(outtime,str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")

    for book in books:
        print("책번호",book.number)
        for timestsamp in book.history:
            print(timestamp.renttime["in"], timestamp.returntime)
            print(timestamp.diff_seconds())
