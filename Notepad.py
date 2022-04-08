from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, askopenfilename,asksaveasfilename
import os


root = Tk()
root.geometry("400x650")
root.wm_iconbitmap("icon.ico")
root.title("Untitled - Notepad")

def NewFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textarea.delete(1.0, END)

def OpenFile():
    global file
    file = askopenfilename(defaultextension="txt",filetypes=[("All Files","*.*"), ("Text Documents","x.txt")])
    if file ==  "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Textarea.delete(1.0, END)
        f = open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()



def SaveFile():

    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
        filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def ExitFile():
    root.destroy()

def cutfile():
    Textarea.event_generate(("<<Cut>>"))

def copyfile():
    Textarea.event_generate(("<<Copy>>"))

def pastefile():
    Textarea.event_generate(("<<Paste>>"))

def About():
        showinfo("Notepad","Notepad Created By Arindam")

# Add Text area

Textarea =Text(root, font="lucida 10",bg="black",fg="white")
file =None
Textarea.pack(fill=BOTH,expand=True)

# Adding MenuBar

MenuBar = Menu(root)

# FileMenu Start
FileMenu = Menu(MenuBar,tearoff=0)

FileMenu.add_command(label="New",command=NewFile)
FileMenu.add_command(label="Open",command=OpenFile)
FileMenu.add_command(label="Save",command=SaveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=ExitFile)

MenuBar.add_cascade(label="File",menu=FileMenu)
# FileMenu Ends

# Edit Menu Start
EditMenu = Menu(MenuBar,tearoff=0)

EditMenu.add_command(label="Cut",command= cutfile)
EditMenu.add_command(label="Copy",command=copyfile)
EditMenu.add_command(label="Paste",command=pastefile)

MenuBar.add_cascade(label="Edit",menu=EditMenu)
# Edit Menu Start

# About Menu Start
HelpMenu = Menu(MenuBar,tearoff=0)

HelpMenu.add_command(label="About App",command=About)
MenuBar.add_cascade(label="Help",menu=HelpMenu)
# About Menu Ends


root.config(menu=MenuBar)

#Adding Scrollbar
scroll = Scrollbar(Textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scroll.set)

root.mainloop()