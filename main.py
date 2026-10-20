from todo import *
from typing import List
def main():
    list[Todo]=[]
    while True:
        cho=input("add|list|complete|delete|exit 任务名")
        cho=cho.split()
        if cho[0]=="add":
            add_todo(cho[1])
            continue
        elif cho[0]=="list":
            show_todo()
            continue
        elif cho[0]=="delete":
            delete_todo(cho[1])
            continue
        elif cho[0]=="exit":
            break

if __name__=="__main__":
    main()



