from tkinter import *

def search() :
    e1.focus_set()
    print("검색")
    t.insert(END, e1.get() + "을 검색 했습니다\n")
    e1.delete(0, END)

def add() :
    e1.focus_set()
    print("추가")
    t.insert(END, e1.get() + "을 추가 했습니다\n")
    e1.delete(0, END)

def delete() :
    e1.focus_set()
    print("삭제")
    t.insert(END, e1.get() + "을 삭제 했습니다\n")
    e1.delete(0, END)

def output() :
    e1.focus_set()
    print("삭제")
    t.insert(END, e1.get() + "을 출력 했습니다\n")
    e1.delete(0, END)

def saveExit() :
    print("저장 & 종료")
    t.insert(END, "저장 & 종료\n")
    exit()

window = Tk()
window.title("친구관리")

# Label 객체 생성 및 배치
Label(window, text="너비").grid(row=0, column=0)
Label(window, text="높이").grid(row=1, column=0)

# Entry 객체 생성 및 배치
e1 = Entry(window, bg="orange")
e2 = Entry(window, bg="orange")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Button 들을 배치하기 위한 Frame 생성 및 배치, window가 부모임
bFrame = Frame(window, pady=10)
bFrame.grid(row=3, column=0, columnspan=2)
Button(bFrame, text='검색', fg="orange", padx=10, command=search).grid(row=0, column=0)
Button(bFrame, text='추가', fg="orange", padx=10, command=add).grid(row=0, column=1)
Button(bFrame, text='삭제', fg="orange", padx=10, command=delete).grid(row=0, column=2)
Button(bFrame, text='출력', fg="orange", padx=10, command=output).grid(row=0, column=3)
Button(bFrame, text='종료', fg="orange", padx=10, command=saveExit).grid(row=0, column=4)

# Text 객체 생성 및 배치
t = Text(window, width=34, height=20, bg="orange")
t.grid(row=4, column=0, columnspan=2)

window.mainloop()
