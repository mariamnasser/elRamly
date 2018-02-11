from tkinter import*
import tkinter.messagebox
tk=Tk()
tk.title("TWO squares")
click =True
activeplayer=1
p1=[]
p2=[]
 
def checker (buttons):
    global click
    if buttons["text"]==" 1"and click ==True :
        buttons["text"]="x"
        
    if buttons["text"]==" 2"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 3"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 4"and click ==True :
        buttons["text"]="x"
        
    if buttons["text"]==" 5"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 6"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 7"and click ==True :
        buttons["text"]="x"
        
    if buttons["text"]==" 8"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 9"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 10"and click ==True :
        buttons["text"]="x"
        
    if buttons["text"]==" 11"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 12"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 13"and click ==True :
        buttons["text"]="x"
        
    if buttons["text"]==" 14"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 15"and click ==True :
        buttons["text"]="x"
    if buttons["text"]==" 16"and click ==True :    
        buttons["text"]="x"
buttons=StringVar()
button1=Button(tk,text=" 1",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2=Button(tk,text=" 2",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(tk,text=" 3",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(tk,text=" 4",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button4))
button4.grid(row=1,column=3,sticky=S+N+E+W)
button5=Button(tk,text=" 5",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button5))
button5.grid(row=2,column=0,sticky=S+N+E+W)
button6=Button(tk,text=" 6",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button6))
button6.grid(row=2,column=1,sticky=S+N+E+W)
button7=Button(tk,text=" 7",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button7))
button7.grid(row=2,column=2,sticky=S+N+E+W)
button8=Button(tk,text=" 8",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button8))
button8.grid(row=2,column=3,sticky=S+N+E+W)
button9=Button(tk,text=" 9",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button9))
button9.grid(row=3,column=0,sticky=S+N+E+W)
button10=Button(tk,text=" 10",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button10))
button10.grid(row=3,column=1,sticky=S+N+E+W)
button11=Button(tk,text=" 11",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button11))
button11.grid(row=3,column=2,sticky=S+N+E+W)
button12=Button(tk,text=" 12",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button12))
button12.grid(row=3,column=3,sticky=S+N+E+W)
button13=Button(tk,text=" 13",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button13))
button13.grid(row=4,column=0,sticky=S+N+E+W)
button14=Button(tk,text=" 14",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button14))
button14.grid(row=4,column=1,sticky=S+N+E+W)
button15=Button(tk,text=" 15",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button15))
button15.grid(row=4,column=2,sticky=S+N+E+W)
button16=Button(tk,text=" 16",font=('Times 26 bold'),height=4,width=8,command=lambda:checker(button16))
button16.grid(row=4,column=3,sticky=S+N+E+W)
def buclick(x):
    global activeplayer
    global p1
    global p2
    if(activeplayer==1):
        setlayout('x')
    print("x:{}".format(x))
tk.mainloop()
