from tkinter import *

window = Tk()
#window.geometry(350*450)
f = Frame(window)
f .grid(row=3, column=0, columnspan=2)

l1 = Label(window, text="이름")
l1.grid(row=0)
l2 = Label(window, text="전화번호")
l2.grid(row=1)
l3 = Label(window, text="전화번호")
l3.grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(f,text="검색")
b1.grid(row=0,column=0, padx=20)
b2 = Button(f,text="추가")
b2.grid(row=0,column=1, padx=20)
b3 = Button(f,text="삭제")
b3.grid(row=0,column=2, padx=20)
b4 = Button(f,text="출력")
b4.grid(row=0,column=3, padx=20)
b5 = Button(f,text="종료")
b5.grid(row=0,column=4, padx=20)


window.mainloop()
