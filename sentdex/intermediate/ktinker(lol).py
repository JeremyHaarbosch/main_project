from tkinter import *
from test.test_decimal import file

#applicatie = app
#Window = venster
#init(iate) = starten

class Window(Frame): #(maakt venster aan)

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_venster()


    def init_venster(self): #(maakt stop knop)

        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        #stop_knop = Button(self, text="stop")
        #stop_knop.place(x=0, y=0)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)

        bestand = Menu(menu)
        bestand.add_command(label="Opslaan", command=self.client_save)
        bestand.add_command(label="Afsluiten", command=self.client_afsluiten)
        menu.add_cascade(label="Bestand", menu=bestand)
        
        edit = Menu(menu)
        edit.add_command(label="Ongedaan maken") 
        menu.add_cascade(label='Aanpassen', menu=edit)
    
    def client_afsluiten(self):
        exit()
        
    def client_save(self):
        pass

root = Tk()

root.geometry("400x300")

app = Window(root) 

root.mainloop()
    
