from tkinter import *

window = Tk()
print(type(window))

window.geometry("150x170")
label01 = Label(window, text="검색")
label01.pack(side =RIGHT)

label02 =Label(window, text="추가")
label02.pack(side=LEFT)

labe03= Label(window, text="삭제")
labe03.pack()

label04 = Label(window, text="4.BUTTON")
label04.pack(side=BOTTOM)

window.mainloop()
