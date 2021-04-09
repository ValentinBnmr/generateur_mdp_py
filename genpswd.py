# modules
import string
from random import randint, choice
from tkinter import *
import webbrowser as wbr

class GeneratorPassword:

    # Méthodes de l'app


    def __init__(self):
    # Initialise la fenètre UI
        self.window = Tk()
        self.window.title("Générateur de mot de passe")
        self.window.geometry("720x480")
        self.window.iconbitmap("src/pin-code.ico")
        self.window.config(background="#0e0e0e")
        self.frame = Frame(self.window, bg="#0e0e0e")
        self.right_frame = Frame(self.frame, bg="#0e0e0e",)
        self.create_widgets()
        self.frame.pack(expand=YES)
        self.right_frame.grid(row=0, column=1, sticky=W)

    def create_widgets(self):
    # Appel les méthodes de notre app
        self.create_title()
        self.create_img()
        self.entry_password()
        self.create_btn_gene()
    
    def entry_password(self):
        # Initialise un champs où l'utilisateur pourra récupérer son mot de passe
        self.password_entry = Entry(self.right_frame, font=("Roboto",20), bg="#0e0e0e",fg="#fff",justify='center')
        self.password_entry.pack(fill=X)
      

    

    def generate_password(self):
        # Méthode qui génère une str aléatoire à partir de la table ascii via des lettres, ponctuations et des nombres digitaux
        self.password_min = 6
        self.password_max = 12
        self.all_chars = string.ascii_letters + string.punctuation + string.digits
        self.password = "".join(choice(self.all_chars) for i in range(randint(self.password_min, self.password_max)))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, self.password)
        
    
    

    
    def create_title(self):
        # Initialise le titre de l'app
        self.label_title = Label(self.right_frame, text="Générateur de mot de passe", font=("Roboto",20), bg="#0e0e0e",fg="#fff")
        self.label_title.pack()
    
    def create_img(self):
        # Initialise l'image de l'app
        self.width = 200
        self.height = 200
        self.img = PhotoImage(file="src/pin-code1.png")
        self.canvas = Canvas(self.frame, width=self.width, height=self.height, bg="#0e0e0e", bd=0,highlightthickness=0)
        self.canvas.create_image(self.width/2, self.height/2, image=self.img)
        self.canvas.grid(row=0, column=0, sticky=W)

    def create_btn_gene(self):
        # Initialise le bouton qui appel la méthode "generate_password"
        self.btn_generate = Button(self.right_frame,text="Générer", font=("Roboto",20), bg="#4675FC",fg="#fff",cursor="target",relief=FLAT, command=self.generate_password)
        self.btn_generate.pack(fill=X)

app = GeneratorPassword()
app.window.mainloop()