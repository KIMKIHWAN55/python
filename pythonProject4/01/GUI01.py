# tkinter를 이용한 친구관리 GUI

from tkinter import *

def search() :
    e1.focus_set()
    print("검색")
    t.insert(END, e1.get() + "을 검색 했습니다\n")
    e1.delete(0, END)

def add() :
    e1.focus_set()
    print("추가")
    t.insert(END, e2.get() + "을 추가 했습니다\n")
    e1.delete(0, END)

def delete() :
    e1.focus_set()
    print("삭제")
    t.insert(END, e1.get() + "을 삭제 했습니다\n")
    e1.delete(0, END)

def output() :
    e1.focus_set()
    print("출력")
    t.insert(END, e1.get() + "을 출력 했습니다\n")
    e1.delete(0, END)

def saveExit() :
    print("저장 & 종료")
    t.insert(END, "저장 & 종료\n")
    exit()

window = Tk()
window.title("친구관리")

# Label 객체 생성 및 배치
l1 = Label(window, text="이름", pady=5)
l1.grid(row=0, column=0, sticky=W)
l2 = Label(window, text="전화번호")
l2.grid(row=1, column=0, sticky=W, pady=5)
l3 = Label(window, text="주소")
l3.grid(row=2, column=0, sticky=W, pady=5)

# Entry 객체 생성 및 배치
e1 = Entry(window, bg="orange", width=26)
e2 = Entry(window, bg="orange", width=26)
e3 = Entry(window, bg="orange", width=26)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

# Button 들을 배치하기 위한 Frame 생성 및 배치, window가 부모임
bFrame = Frame(window, pady=5)
bFrame.grid(row=3, column=0, columnspan=2)
b1 = Button(bFrame, text='검색', width=6, command=search)
b1.grid(row=0, column=0, padx=2)
b2 = Button(bFrame, text='추가', width=6, command=add)
b2.grid(row=0, column=1, padx=2)
b3 = Button(bFrame, text='삭제', width=6, command=delete)
b3.grid(row=0, column=2, padx=2)
b4 = Button(bFrame, text='출력', width=6, command=output)
b4.grid(row=0, column=3, padx=2)
b5 = Button(bFrame, text='종료', width=6, command=saveExit)
b5.grid(row=0, column=4, padx=2)

# Text 객체 생성 및 배치
t = Listbox(window, bg="orange", height=12, width=33, border=0)
t.grid(row=4, column=0, columnspan=2, pady=2)

# Create scrollbar
scrollbar = Scrollbar(window, orient='vertical')
scrollbar.grid(row=4, column=2, sticky=N+S)
# Set scroll to listbox
t.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=t.yview)
# Bind select
# t.bind('<<ListboxSelect>>', select_item)

window.mainloop()