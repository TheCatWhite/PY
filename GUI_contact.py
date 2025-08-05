import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connexion à la base et création de la table si elle n'existe pas
def init_bdd():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        nom TEXT PRIMARY KEY,
        tel TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def ajouter_contact():
    nom = entry_nom.get()
    tel = entry_tel.get()
    if nom and tel:
        try:
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contacts (nom, tel) VALUES (?, ?)", (nom, tel))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", f"Contact '{nom}' ajouté !")
            entry_nom.delete(0, tk.END)
            entry_tel.delete(0, tk.END)
            afficher_contacts()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Erreur", "Ce contact existe déjà.")
    else:
        messagebox.showwarning("Erreur", "Remplis tous les champs !")

def afficher_contacts():
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nom, tel FROM contacts ORDER BY nom")
    for nom, tel in cursor.fetchall():
        listbox.insert(tk.END, f"{nom} : {tel}")
    conn.close()

def supprimer_contact():
    selection = listbox.curselection()
    if selection:
        item = listbox.get(selection[0])
        nom = item.split(":")[0].strip()
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE nom = ?", (nom,))
        conn.commit()
        conn.close()
        afficher_contacts()
        messagebox.showinfo("Supprimé", f"Contact '{nom}' supprimé.")
    else:
        messagebox.showwarning("Erreur", "Sélectionne un contact à supprimer.")

# Interface graphique
root = tk.Tk()
root.title("Gestionnaire de Contacts de Avotra Ryan")
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

# Initialiser la base et charger les contacts
init_bdd()
afficher_contacts()

root.mainloop()
