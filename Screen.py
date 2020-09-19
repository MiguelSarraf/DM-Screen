from tkinter import *
from tkinter.filedialog import askopenfilename
from  PIL import ImageTk, Image
import matplotlib.pyplot as plt
import os.path

root=Tk()
root.geometry("1280x800")
rota=Label(root)
rota.pack()
rota.place(anchor="nw", relx=.49, rely=.05)
mapa=[None]
x=[]
y=[]

def desenha(posx, posy):
	x.append(int(posx))
	y.append(int(posy))
	fig, ax=plt.subplots()
	ax.imshow(plt.imread(mapa[0]), extent=[0,100,0,100])
	plt.scatter(x, y, color="red")
	plt.plot(x, y, color="red")
	plt.savefig("rota.png", dpi=100, bbox_inches="tight", pad_inches=0)
	img=Image.open("rota.png")
	img=img.resize((600,600))
	img=ImageTk.PhotoImage(img)
	rota.configure(image=img)
	rota.image=img

def apaga():
	while len(x)>0:
		x.pop()
		y.pop()
	plt.clf()
	fig, ax=plt.subplots()
	ax.imshow(plt.imread(mapa[0]), extent=[0,100,0,100])
	plt.savefig("rota.png", dpi=100, bbox_inches="tight", pad_inches=0)
	img=Image.open("rota.png")
	img=img.resize((600,600))
	img=ImageTk.PhotoImage(img)
	rota.configure(image=img)
	rota.image=img

def carrega():
	nome=askopenfilename()
	if os.path.exists(nome):
		mapa[0]=nome
		apaga()

labelmov=Label(root, text="Movimentar a party: ", font=("Roboto", 16))
labelmov.pack()
labelmov.place(anchor="nw", relx=.49, rely=.83)
entryx=Entry(root, width=10)
entryx.insert(0, "x")
entryx.pack()
entryx.place(anchor="nw", relx=.68, rely=.84)
entryy=Entry(root, width=10)
entryy.insert(0, "y")
entryy.pack()
entryy.place(anchor="nw", relx=.78, rely=.84)
butdesenha=Button(root, text="Mover", width=10, command=lambda:desenha(entryx.get(), entryy.get()))
butdesenha.pack()
butdesenha.place(anchor="nw", relx=.87, rely=.84)
butlmapa=Button(root, text="Carregar mapa", width=25, command=lambda:carrega())
butlmapa.pack()
butlmapa.place(anchor="nw", relx=.52, rely=.9)
butlimpa=Button(root, text="Apagar rota", width=25, command=lambda:apaga())
butlimpa.pack()
butlimpa.place(anchor="nw", relx=.75, rely=.9)
root.mainloop()
