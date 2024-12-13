from tkinter import *
from tkinter import IntVar
from Core.main import Main
import os
# from tkinter.messagebox import showinfo
import tkinter.messagebox 
from tkinter.ttk import Button, Entry
from tkinter import ttk
import threading
import shutil
from tkinter import filedialog

root = Tk()
ck_new = BooleanVar()
ck_approved = BooleanVar()
ck_committed = BooleanVar()
ck_external = BooleanVar()
ck_test = BooleanVar()
ck_accepted = BooleanVar()
ck_accepted = BooleanVar()
ck_review = BooleanVar()
ck_done = BooleanVar()

class Funcs(Main):
    
    def run_program(self):
        mail_ = self.mail_entry.get() # type: ignore
        pass_ = self.pass_entry.get() # type: ignore
        checks = {
            "New": ck_new.get(),
            "Approved": ck_approved.get(),
            "Committed": ck_committed.get(),
            "External": ck_external.get(),
            "Test": ck_test.get(),
            "Accepted": ck_accepted.get(),
            "Review": ck_review.get(),
            "Done": ck_done.get()
        }

        automation_thread = threading.Thread(target=self.main, args=(mail_, pass_,checks))
        automation_thread.start()
    
    def stop_program(self):
        self.shut_down()

    def create_xlsx(self):
        self.source_file = 'Relatório de PBI.xlsx'

        if os.path.exists(self.source_file):
            file_path = filedialog.asksaveasfilename(
                defaultextension='.xlsx',
                filetypes=[('Excel Files', '*.xlsx'), ('All files', '*.*')],
                title='Relatório de Backlogs'
            )
            if file_path:
                try:
                    shutil.copy(self.source_file, file_path)
                    tkinter.messagebox.showinfo('OK', 'Relatório salvo com sucesso!')
                except Exception as e:
                    tkinter.messagebox.showinfo("Erro.", "Não foi possível salvar o arquivo.")
                    print(f"Erro ao baixar o arquivo:{e}")
        else:
            tkinter.messagebox.showinfo("Não encontrado.", "Necessário executar a aplicação para a obtenção de dados.")


class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_screen()
        self.buttons()
        self.board()
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
        self.btn_run = Button(self.frame_1, text='RUN', command=self.run_program)
        self.btn_run.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.2)

        self.btn_stop = Button(self.frame_1, text='STOP', command=self.stop_program)
        self.btn_stop.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.2)

        self.btn_restart = Button(self.frame_1, text='GERAR EXCEL', command=self.create_xlsx)
        self.btn_restart.place(relx=0.65, rely=0.1, relwidth=0.3, relheight=0.2)

        ## Labels e Input

        self.lb_code = Label(self.frame_1, text = 'E-mail (Azure Devops)', bg='#DFE9F5')
        self.lb_code.place(relx=0.00, rely=0.35, relwidth=0.3, relheight=0.2)

        self.mail_entry = Entry(self.frame_1)
        self.mail_entry.place(relx=0.05, rely=0.5, relwidth=0.3, relheight=0.1)

        self.lb_code = Label(self.frame_1, text = 'Senha (Azure Devops)', bg='#DFE9F5')
        self.lb_code.place(relx=0.00, rely=0.6, relwidth=0.3, relheight=0.2)

        self.pass_entry = Entry(self.frame_1, show="*")
        self.pass_entry.place(relx=0.05, rely=0.75, relwidth=0.3, relheight=0.1)

        ## Checkbox

        # First Line

        self.c_new = Checkbutton(self.frame_1, text='New', bg='#DFE9F5', variable=ck_new)
        self.c_new.place(relx=0.39, rely=0.5, relwidth=0.14, relheight=0.1)

        self.c_approved = Checkbutton(self.frame_1, text='Approved', bg='#DFE9F5', variable=ck_approved)
        self.c_approved.place(relx=0.52, rely=0.5, relwidth=0.14, relheight=0.1)

        self.c_commited = Checkbutton(self.frame_1, text='Committed', bg='#DFE9F5', variable=ck_committed)
        self.c_commited.place(relx=0.65, rely=0.5, relwidth=0.14, relheight=0.1)

        self.c_external = Checkbutton(self.frame_1, text='External', bg='#DFE9F5', variable=ck_external)
        self.c_external.place(relx=0.78, rely=0.5, relwidth=0.14, relheight=0.1)

        ## Second Line

        self.c_test = Checkbutton(self.frame_1, text='Test', bg='#DFE9F5', variable=ck_test)
        self.c_test.place(relx=0.39, rely=0.75, relwidth=0.14, relheight=0.1)

        self.c_accepted = Checkbutton(self.frame_1, text='Accepted', bg='#DFE9F5', variable=ck_accepted)
        self.c_accepted.place(relx=0.52, rely=0.75, relwidth=0.14, relheight=0.1)

        self.c_review = Checkbutton(self.frame_1, text='Review', bg='#DFE9F5', variable=ck_review)
        self.c_review.place(relx=0.65, rely=0.75, relwidth=0.14, relheight=0.1)

        self.c_done = Checkbutton(self.frame_1, text='Done', bg='#DFE9F5', variable=ck_done)
        self.c_done.place(relx=0.78, rely=0.75, relwidth=0.14, relheight=0.1)


    def board(self):
        self.listBacklogs = ttk.Treeview(self.frame_2, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5')) # type: ignore
        self.listBacklogs.heading('#0', text='PBI')
        self.listBacklogs.heading('#1', text='DESCRIÇÃO')
        self.listBacklogs.heading('#2', text='STATUS')
        self.listBacklogs.heading('#3', text='EFFORT')
        self.listBacklogs.heading('#4', text='FEATURE')

        self.listBacklogs.column('#0', width=77)
        self.listBacklogs.column('#1', width=300)
        self.listBacklogs.column('#2', width=77)
        self.listBacklogs.column('#3', width=77)
        self.listBacklogs.column('#4', width=77)

        self.listBacklogs.place(relx=0.005, rely=0.1, relwidth=0.95, relheight=0.85)

        # self.scroolTable = Scrollbar(self.frame_2, orient='vertical')
        # self.listBacklogs.configure(yscroll=self.scroolTable.set)
        # self.scroolTable.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.05)