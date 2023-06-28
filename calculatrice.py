import tkinter as tk
root = tk.Tk()
root.title("calculatrice")
root.geometry("285x414")
root.resizable(height=False, width=False)

result = tk.Entry(root, width=20, borderwidth=5, bg="black", fg="red", font=("courier", 24))
result.config(font="white")
result.grid(column=0, row=0, columnspan=4, ipadx=10)

def ajouter_chiffre(chiffre):
    result.insert(tk.END, chiffre)

def soustraction():
    global sauvegarde
    global operateur
    operateur = "-"
    sauvegarde = int(result.get())
    result.delete(0, tk.END)

def addition():
    global sauvegarde
    global operateur
    operateur = "+"
    sauvegarde = int(result.get())
    result.delete(0, tk.END)

def multiplication():
    global sauvegarde
    global operateur
    operateur = "*"
    sauvegarde = int(result.get())
    result.delete(0, tk.END)

def division():
    global sauvegarde
    global operateur
    operateur = "/"
    sauvegarde = int(result.get())
    result.delete(0, tk.END)

def resultat():
    global operateur
    sauvegarde2 = int(result.get())
    result.delete(0, tk.END)
    if operateur == "+":
        result.insert(0, str(sauvegarde + sauvegarde2))
    elif operateur == "-":
        result.insert(0, str(sauvegarde - sauvegarde2))
    elif operateur == "*":
        result.insert(0, str(sauvegarde * sauvegarde2))
    elif operateur == "/":
        if sauvegarde2 == 0:
            result.insert(0, "ERREUR")
        else:
            result.insert(0, str(sauvegarde / sauvegarde2))

def supp_calcul():
    result.delete(0, tk.END)

un = tk.Button(root,text="1",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("1"),)
un.grid(column=0, row=3)

deux = tk.Button(root,text="2",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("2"),)
deux.grid(column=1, row=3)

trois = tk.Button(root,text="3",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("3"),)
trois.grid(column=2, row=3)

quatre = tk.Button(root,text="4",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("4"),)
quatre.grid(column=0, row=2)

cinq = tk.Button(root,text="5",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("5"),)
cinq.grid(column=1, row=2)

six = tk.Button(root,text="6",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("6"),)
six.grid(column=2, row=2)

sept = tk.Button(root,text="7",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("7"),)
sept.grid(column=0, row=1)

huit = tk.Button(root,text="8",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("8"),)
huit.grid(column=1, row=1)

neuf = tk.Button(root,text="9",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("9"),)
neuf.grid(column=2, row=1)

zero = tk.Button(root,text="0",background="#E6E6FA",padx=40,pady=20,command=lambda: ajouter_chiffre("0"),)
zero.grid(column=1, row=4)

plus = tk.Button(root,text="+",background="#a6a6ed",padx=39,pady=20, command=addition)
plus.grid(column=0, row=4)

egal = tk.Button(root,text="=",background="#a6a6ed",padx=39,pady=20, command=resultat)
egal.grid(column=2, row=4)

moin = tk.Button(root, text="-", background="#a6a6ed", padx=41,pady=20, command=soustraction)
moin.grid(column=0, row=5)

fois = tk.Button(root, text="x", background="#a6a6ed", padx=41,pady=20, command=multiplication)
fois.grid(column=1, row=5)

divise = tk.Button(root, text="/", background="#a6a6ed", padx=41,pady=20, command=division)
divise.grid(column=2, row=5)

c = tk.Button(root, text="c", background="#fae6e6", padx=135, pady=20, command=supp_calcul)
c.grid(column=0, row=6, columnspan=3)

root.mainloop()
