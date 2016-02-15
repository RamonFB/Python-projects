#!/usr/bin/env python

"""
Ramon Forcadell
"""

from Tkinter import *
import tkFileDialog
import tkSimpleDialog
import tkMessageBox
import os
import Tkinter as tk

#Metode per escollir el directori de treball
def dir_treball():
	dir_treball=tkFileDialog.askopenfilename()#Con asksaveasfilename on comptes de asksaveasfile et dona nomes un string amb la ruta+nom del fitxer
	f=open("out.txt",'w')#Creem el fitxer out amb la propietat d'escriure
	f.writelines(dir_treball)#Escric la ruta inicial a out.txt per utilitzarla despres al metode crear
	f.close()
	if dir_treball != '':
		directoriList.delete(0,END)
		directoriList.insert(0,dir_treball)

#Metode Per omplir la primera llista
def Rellegir():
	fileList.delete(0,END)#Cada vegada que li dono a reomplir borra la anterior llista
	f=open("out.txt",'r')#Creem el fitxer out amb la propietat d'escriure
	for text in f.readlines()[:]:
		text2=text#text2=Nom fitxer+ruta
	f.close()
	os.system('tar -tf ' + text2 + ' > x.txt')#Comanda per veure els arxius que hi han dins d'un fitxer 
	
	f=open('x.txt' , 'r')#Obrim el fitxer
	for text in f.readlines()[:]:#Ho faig d'aquesta manera perque readlines[:] fa un salt de linia a cada fixer
		text2=text.split(directoriList.get(0)+"/")[-1]#Agafo la ultima paraula separades per "/"
		fileList.insert(END,text2[:-1])#Insertem els fitxers al listbox. El -1 es per eliminar el caracter del "newline"
	f.close()

#Metode per ocultar els no seleccionats
def ocultaNoSelec():
	x=0#contador
	indexs = fileList.curselection()#Retorna els valors dels fitxers de la llista seleccionats i els guardo en index
	con = len(indexs)#con es el numero total de fitxers seleccionats per utilitzarlo com a limit al for
	L = []#array per introduir els fitxers
	while (x<con):
		L.append(fileList.get(fileList.curselection()[x]))#append afegeix un element al final de la llista. En aquest cas el seleccionats 
		x=x+1#incrementem contador
	fileList.delete(0, END)#Borrem la llista per mostrar el nou contingut
    
	for item in L :
		fileList.insert( END,item )#Inserto el nou continugt

#Metode per ocultar el selecionats
def ocultaSelec():
        items = fileList.curselection()#Retorna els valors dels fitxers de la llista seleccionats i els guardo en index
        pos = 0
        for i in items :
            idx = int(i) - pos#Resto perque quan fem la primera pasada a la llista hi han x element pero quan en borro 1 hi han x-1 elements per tant per borrar el correcte u faig aixi
            fileList.delete(idx,idx)#Determina desde on fins a on borrar
            pos = pos + 1

#Metode per pasar tots els fitxers a la segona llista
def TotsDreta():
	fileList.delete(0,END)#Cada vegada que li dono a reomplir borra la anterior llista
	f=open("out.txt",'r')#Creem el fitxer out amb la propietat d'escriure
	for text in f.readlines()[:]:
		text2=text#text2=Nom fitxer+ruta
	f.close()
	os.system('tar -tf ' + text2 + ' > x.txt')#Comanda per veure els arxius que hi han dins d'un fitxer 
	
	f=open('x.txt' , 'r')#Obrim el fitxer
	for text in f.readlines()[:]:#Ho faig d'aquesta manera perque readlines[:] fa un salt de linia a cada fixer
		text2=text.split(directoriList.get(0)+"/")[-1]#Agafo la ultima paraula separades per "/"
		fileList2.insert(END,text2[:-1])#Insertem els fitxers al listbox. El -1 es per eliminar el caracter del "newline"
	f.close()

#Metode per pasar tots els fitxers de la segona llista a la primera
def TotsEsquerra():
	fileList2.delete(0,END)#Cada vegada que li dono a reomplir borra la anterior llista
	f=open("out.txt",'r')#Creem el fitxer out amb la propietat d'escriure
	for text in f.readlines()[:]:
		text2=text#text2=Nom fitxer+ruta
	f.close()
	os.system('tar -tf ' + text2 + ' > x.txt')#Comanda per veure els arxius que hi han dins d'un fitxer 
	
	f=open('x.txt' , 'r')#Obrim el fitxer
	for text in f.readlines()[:]:#Ho faig d'aquesta manera perque readlines[:] fa un salt de linia a cada fixer
		text2=text.split(directoriList.get(0)+"/")[-1]#Agafo la ultima paraula separades per "/"
		fileList.insert(END,text2[:-1])#Insertem els fitxers al listbox. El -1 es per eliminar el caracter del "newline"
	f.close()

#Metode per pasar tots els fitxers seleccionats de la segona llista a la primera
def SelecionatDreta():
	x=0
	indexs = fileList.curselection()#Retorna els valors dels fitxers de la llista seleccionats i els guardo en index
	con = len(indexs) #total d'arxius seleccionats
	L = []#llista per omplir
	while (x<con):
		L.append(fileList.get(fileList.curselection()[x]))#Afegirem a l'array L les seleccionades
		x=x+1#incrementem contador
    
	for item in L : #Posarem els seleccionats a l'altra llista
		fileList2.insert(END,item)
        pos = 0
        for i in indexs :#Mirem si estan a la llista de seleccionats i els eliminarem de la primera llista
            idx = int(i) - pos#Resto perque quan fem la primera pasada a la llista hi han x element pero quan en borro 1 hi han x-1 elements per tant per borrar el correcte u faig aixi
            fileList.delete(idx,idx)#Determina desde on fins on arribar a borrar
            pos = pos + 1

#Metode per pasar tots els fitxers seleccionats de la primera llista a la segona   
def SelecionatEsquerra():
	x=0
	indexs = fileList2.curselection()
	con = len(indexs) #total d'arxius seleccionats
	L = []
	while (x<con):
		L.append(fileList2.get(fileList2.curselection()[x]))#Afegirem a l'array L les seleccionades
		x=x+1
    
	for item in L : #Posarem els seleccionats a l'altra llista
		fileList.insert(END,item)#Insertem a la primera llista
        pos = 0
        for i in indexs :
            idx = int(i) - pos#Resto perque quan fem la primera pasada a la llista hi han x element pero quan en borro 1 hi han x-1 elements per tant per borrar el correcte u faig aixi
            fileList2.delete(idx,idx)#Determina desde on fins on arribar a borrar
            pos = pos + 1
		
def sortir():
	os.system('rm a.txt x.txt out.txt output.txt')
	window.quit()

def extreu():
	fitxers =""
	f=open("out.txt",'r')#El tinc aqui perque agafo el nom del fitxer .tar
	for text in f.readlines()[:]:#Ho faig d'aquesta manera perque readlines[:] fa un salt de linia a cada fixer
		text2=text.split("/")[-1]#Agafo la ultima paraula separades per "/"
	f.close()
	temp_list = list(fileList2.get(0, tk.END))#Retorna una llista dels fitxers del lintbox2

	if not temp_list:#Si la llista esta buida
		tkMessageBox.showinfo("Error","No hi han fitxers per a comprimir")#Salta aquest missatge
		
	for c in temp_list:
		fitxers = fitxers + " " + c #Concateno els noms dels fitxers a un sol string
	
	f=open('output.txt','r')#Agafo el directori d'extraccio del askdirectory
	for text in f.readlines()[:]:#Ho faig d'aquesta manera perque readlines[:] fa un salt de linia a cada fixer
		dir_extraccio=text
	f.close()
	comanda = ('tar -xf ' + text2+" -C "+ dir_extraccio + " " + fitxers)#String per mostrar al listbox del boto executar
	
	def extreu():#funcio que cridem quan li donem al boto executar
		os.system('tar -xf ' + text2 +" -C "+dir_extraccio + " " + fitxers)#Comanda per descomprimir. text2=nom del fitxer comprimit. Fitxers=nom dels fitxers. x=extract f=file
	
	#Finestra amb el listbox + boto d'executar
	FinestraExecutar=Toplevel()
	FinestraExecutar.title("Comanda a executar")
	FinestraExecutar.minsize(50,50)
	B1FC = Button(FinestraExecutar,text= "Executar", command=extreu).pack(side=RIGHT)
	listt = Listbox(FinestraExecutar,yscrollcommand=sc1f3.set,width=60,bg='#FFFFFF',height=1)
	listt.pack(side=TOP,anchor=W,expand=TRUE,fill=BOTH)
	listt.insert(END,comanda)

def dir_extraccio():
	dir_extraccio=tkFileDialog.askdirectory()#Preguntem a quin directori voleu guardar
	directoriList2.insert(0,dir_extraccio)
	f=open('output.txt','w')
	f.write(dir_extraccio)
	f.close()
	
#MAIN
window=Tk()
window.title("Creacio del Fitxer Comprimit")
window.minsize(900,200)

#Variables per comprovar els checkbox
checked_cap=IntVar()
checked_gzip=IntVar()
checked_bzip2=IntVar()
checked_xz=IntVar()

#BOTO DIRECTORI + LISTBOX ON ES VISUALITZA EL DIRECTORI
f1=Frame(window)
l1f1 = Button(f1,text="Escollir fitxer tar", command=dir_treball).pack(side = LEFT)
scrollist = Scrollbar(f1)
directoriList = Listbox(f1,yscrollcommand=scrollist.set, width=35, height=1,bg="#d9d9d9")
scrollist.config(command=directoriList.yview)
directoriList.pack(side=LEFT)
f1.pack(side=TOP,anchor=W)
######################################################

#Finestra 2
f2=Frame(window)
l1f2=Label(f2,text="Contingut:").pack(side=LEFT)
b1f2=Button(f2,text="Rellegir",command=Rellegir).pack(side=LEFT)
b2f2=Button(f2,text="Ocultar NO seleccionats", command=ocultaNoSelec).pack(side=LEFT)
b3f2=Button(f2,text="Ocultar seleccionat",command=ocultaSelec).pack(side=LEFT)


f1f2=Label(f2,text="    \t    \t    \t").pack(side=LEFT)
b4f2=Button(f2,text="Directori extraccio",command=dir_extraccio).pack(side=LEFT)
scrollist = Scrollbar(f2)
directoriList2 = Listbox(f2,yscrollcommand=scrollist.set, width=35, height=1,bg="#d9d9d9")
scrollist.config(command=directoriList2.yview)
directoriList2.pack(side=LEFT)

f2.pack(side=TOP,anchor=W)

#frame boto sortir
f12=Frame(window) 
b1f12=Button(f12,text="Sortir",command=sortir)
b1f12.pack(side=LEFT)
l1f6=Label(f12, text="\t     \t     \t     \t     \t     \t     \t     \t      \t").pack(side=LEFT)
b1f5=Button(f12,text="Extreu",command=extreu).pack(side=LEFT)
l1f5=Label(f12,text="           ").pack(side=LEFT)
f12.pack(side=BOTTOM,anchor=W)

#frame 3
f3=Frame(window)
sc1f3 = Scrollbar(f3,orient=VERTICAL)
fileList = Listbox(f3,selectmode = "multiple",yscrollcommand=sc1f3.set,width=60,bg='#FFFFFF',height=12)
sc1f3.config(command=fileList.yview)
sc1f3.pack(side=RIGHT,anchor=W,fill=Y)
fileList.pack(side=TOP,anchor=W,expand=TRUE,fill=BOTH)
sc1f3.pack(expand=TRUE,fill=Y)
f3.pack(side=LEFT,anchor=N)


#frame 4 
f4=Frame(window) 
l1f5=Label(f4,text="Tots: ").pack(side = TOP)
b1f3 = Button(f4,text=">>>",command=TotsDreta).pack(side = TOP)
l1f6=Label(f4,text="Als seleccionats: ").pack(side = TOP)
b1f4 = Button(f4,text="--->",command=SelecionatDreta).pack(side = TOP)
b1f5 = Button(f4,text="<---",command=SelecionatEsquerra).pack(side = TOP)
l1f5=Label(f4,text="Tots: ").pack(side = TOP)
b1f3 = Button(f4,text="<<<",command=TotsEsquerra).pack(side = TOP)
f4.pack(side=LEFT,anchor=N)

#frame 5
f5=Frame(window)
sc1f5 = Scrollbar(f5,orient=VERTICAL)
fileList2 = Listbox(f5,selectmode = "multiple",yscrollcommand=scrollist.set,width=45,bg='#FFFFFF',height=12)
sc1f5.config(command=fileList2.yview)
sc1f5.pack(side=RIGHT,anchor=W,fill=Y)
fileList2.pack(side=TOP,anchor=W,expand=TRUE,fill=BOTH)
sc1f5.pack(expand=TRUE,fill=Y)
f5.pack(side=TOP,anchor=W)


window.mainloop()
