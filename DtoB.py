from tkinter import *

root = Tk()
list=[]

def show():
    if list != " ":
        list.clear()

    var0=inputText.get("0.0","end-1c")
    varfo=float(var0)
    varp=int(varfo)
    var2=int(varp)
    outputText.insert(END, "2|")
    outputText.insert(END, var2)
    outputText.insert(END, "\n")
    x=0
    while 1<=var2:
        var3=int(var2%2)
        var2=int(var2/2)
        list.append(var3)
        if var2 >= 1:
            outputText.insert(END, "2|")
        else:
            outputText.insert(END, "  ")

        outputText.insert(END,var2)
        outputText.insert(END, "--")
        outputText.insert(END,var3)
        outputText.insert(END, "\n")
        x+=1
    outputText.insert(END,varp)
    outputText.insert(END,"=")
    var5=list
    var5.reverse()
    outputText.insert(END, var5)
    outputText.insert(END, "\n")


def dele():
    outputText.delete("1.0","end")
    inputText.delete("1.0", "end")
    list.clear()

root.title('Decimal to Binary')
lable=Label(root, text="Enter any Decimal Number")
inputText = Text(root, height=2, width=30, )
button = Button(root, text="Show", command=show,)
clear = Button(root, text="Delete", command=dele )
outputText = Text(root, height=10, width=30, )
root.geometry('300x280')
root.resizable(width=False, height=False)
lable.place(x=30, y=10)
inputText.place(x=30, y=40)
button.place(x=100, y=80)
clear.place(x=150, y=80)
outputText.place(x=30, y=110)

mainloop()