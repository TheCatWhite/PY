import tkinter as tk
from tkinter import messagebox

contacts = {}

def ajouter_contact():
    nom = entry_nom.get()
    tel = entry_tel.get()
    if nom and tel:
        contacts[nom] = tel
        messagebox.showinfo("Succès", f"Contact '{nom}' ajouté !")
        entry_nom.delete(0, tk.END)
        entry_tel.delete(0, tk.END)
        afficher_contacts()
    else:
        messagebox.showwarning("Erreur", "Remplis tous les champs !")

def afficher_contacts():
    listbox.delete(0, tk.END)
    for nom, tel in contacts.items():
        listbox.insert(tk.END, f"{nom} : {tel}")

def supprimer_contact():
    selection = listbox.curselection()
    if selection:
        item = listbox.get(selection[0])
        nom = item.split(":")[0].strip()
        del contacts[nom]
        afficher_contacts()
        messagebox.showinfo("Supprimé", f"Contact '{nom}' supprimé.")
    else:
        messagebox.showwarning("Erreur", "Sélectionne un contact à supprimer.")

# Interface
root = tk.Tk()
root.title("Gestionnaire de Contacts")
root.geometry("400x400")

tk.Label(root, text="Nom:").pack()
entry_nom = tk.Entry(root)
entry_nom.pack()

tk.Label(root, text="Téléphone:").pack()
entry_tel = tk.Entry(root)
entry_tel.pack()

tk.Button(root, text="Ajouter", command=ajouter_contact).pack(pady=5)

listbox = tk.Listbox(root, height=10, width=40)
listbox.pack(pady=10)

tk.Button(root, text="Supprimer", command=supprimer_contact).pack()

afficher_contacts()
root.mainloop()
