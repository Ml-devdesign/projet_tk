import tkinter as tk



# Fonction appelée lorsque le bouton est cliqué
def on_button_click():
    label.config(text="Bonjour, Tkinter!")


# Créer la fenêtre principale
window = tk.Tk()
window.title("Exemple Tkinter")

# Créer un bouton
button = tk.Button(window, text="Cliquez-moi!", command=on_button_click, width=16, bg='orange')

# Créer une étiquette
label = tk.Label(window, text="Bienvenue dans Tkinter!",font='arial', width=90, height=10, borderwidth=2,background='pink')

# Organiser les widgets à l'intérieur de la fenêtre
label.pack(pady=100)
button.pack(pady=10)


# Lancer la boucle principale de l'application
window.mainloop()
