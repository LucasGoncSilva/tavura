from tkinter import *
from Core.main import Main
from tkinter.messagebox import showinfo

root = Tk()

class Aplication(Main):
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_screen()
        self.buttons()
        root.mainloop()


    def screen(self):
        self.root.title("Automação AlphaTask")
        self.root.configure(background= '#6abce2')
        self.root.geometry("700x500")
        self.root.resizable(False, False)

    def frames_screen(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#DFE9F5', highlightbackground='white', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#DFE9F5', highlightbackground='white', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def buttons(self):
        self.btn_run = Button(self.frame_1, text='RUN')
        self.btn_run.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.2)

        self.btn_stop = Button(self.frame_1, text='STOP')
        self.btn_stop.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.2)

        self.btn_restart = Button(self.frame_1, text='RESTART')
        self.btn_restart.place(relx=0.65, rely=0.1, relwidth=0.3, relheight=0.2)
