from Tkinter import *
import tkFileDialog
import tkSimpleDialog
import tkMessageBox
import os
import Tkinter as tk

window=Tk()
window.title("Tractament de fitxers")
window.minsize(600,500)
ment = StringVar(value = "*.*")
List = []

def work_directory():
	work_directory=(tkFileDialog.askdirectory())#save the path where the files are saved
	directoryList.insert(0,work_directory)

def fillList():
	List_directory.delete(0,END)#Delete de list
	text = ment.get()	#Get text from the TextBox
	directoryString = directoryList.get(0,END)
	os.system('find ' + directoryString[0] + ' > out.txt')
	os.system('sed -i -e "1d" out.txt')#Delete 1rst line
	f=open('out.txt','r')
	del List[:]	#Clean list 
	for text2 in f.readlines()[:]:	# [:] = newline for each directory
		List.append(text2)
		if(text == "*.*"):
			List_directory.insert(END,text2) #Insert the directory to listBox.
	res = filter(lambda k: text in k,List)
	for i in res:#It is made with a loop to insert one by one
		List_directory.insert(END,i)
	f.close()

def hideNoSelected():
	L = []	#New list
	x=0		#count
	indexs = List_directory.curselection()
	con = len(indexs)
	while (x<con):
		L.append(List_directory.get(List_directory.curselection()[x]))
		x=x+1
	List_directory.delete(0, END)#Delete the list for show the new content
	for item in L :
		List_directory.insert( END,item )

def hideSelected():
    items = List_directory.curselection()
    pos = 0
    for i in items :
        idx = int(i) - pos
        List_directory.delete(idx,idx)
        pos = pos + 1

def copyFiles():
	L=[]
	x=0		#count
	text = ""
	indexs = List_directory.curselection()
	con = len(indexs)
	Path_save_directory = (tkFileDialog.askdirectory())
	while (x<con):
		text = text + List_directory.get(List_directory.curselection()[x])
		x=x+1
	os.system('cp ' + text.rstrip('\n') + " " + Path_save_directory)
	print ('cp ' + text.rstrip('\n') + " " + Path_save_directory)

def selectAll():
	List_directory.selection_set(0, END)

def deselectAll():
	List_directory.selection_clear(0,END)

def clean():
	List_directory.delete(0,END)

def exit():
	os.system('rm -f out.txt')
	window.quit()


f1=Frame(window)
Button_ChooseDirectory = Button(f1,text="Escollir directori treball",command=work_directory).pack(side = LEFT)
directoryList = Listbox(f1,width=35,height=1)
directoryList.pack(side=LEFT)
f1.pack(side=TOP,anchor=W)

f2=Frame(window)
Label_FiltredByName = Label(f2,text=" Filtre per nom de fitxer:  ").pack(side = LEFT)
mEntry = Entry(f2,textvariable = ment).pack()
f2.pack(side=TOP,anchor=W)

f3=Frame(window)
Label_List = Label(f3,text="Llista:").pack(side = TOP,anchor=W)
Button_Fill = Button(f3,text="Omplir",command=fillList).pack(side=TOP,anchor=W)
Button_Clean = Button(f3,text="Netejar",command=clean).pack(side=TOP,anchor=W)
Button_HideNoSelected = Button(f3,text="Ocultar No Seleccionats",command=hideNoSelected).pack(side=TOP,anchor=W)
Button_HideSelected = Button(f3,text="Ocultar Seleccionats",command=hideSelected).pack(side=TOP,anchor=W)
f3.pack(side=LEFT,anchor=N)

f4=Frame(window)
scroll = Scrollbar(f4,orient=VERTICAL)
List_directory = Listbox(f4,selectmode = "multiple",yscrollcommand=scroll.set,width=50,height=10)
scroll.config(command=List_directory.yview)
scroll.pack(side=RIGHT,anchor=W,fill=Y)
List_directory.pack(side=TOP,fill=BOTH,expand=TRUE)
scroll.pack(expand=TRUE,fill=Y)
Button_Exit = Button(f4,text="Sortir",command=exit).pack(side=LEFT,anchor=W)
f4.pack(side=LEFT,anchor=N)

f5=Frame(window)
Button_All = Button(f5,text="Tots",command=selectAll).pack(side = TOP,anchor=W)
Button_None = Button(f5,text="Cap",command=deselectAll).pack(side=TOP,anchor=W)
Label_Selected = Label(f5,text="Als seleccionats:").pack(side=TOP,anchor=W)
Button_Copy = Button(f5,text="Copiar",command=copyFiles).pack(side=TOP,anchor=W)
Button_Move = Button(f5,text="Moure").pack(side=TOP,anchor=W)
Button_Delete = Button(f5,text="Esborrar").pack(side=TOP,anchor=W)
Button_Rename = Button(f5,text="Renombrar").pack(side=TOP,anchor=W)
f5.pack(side=TOP,anchor=E)

window.mainloop()