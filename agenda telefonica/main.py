from tkinter import *

azul = '#005CAA'
branco = "#ffffff"
preto = "#000000"

class agenda_telefonica:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1200x600')
        self.window.title('Agenda Telefônica')
        self.window.resizable(False, False)

        self.principal_frame = Frame(self.window, bg=azul)
        self.principal_frame.place(x=0, y=0, w=1200, h=600)


#   <---------- tela de cadastro de contato ---------->   #
    def window_register_contact(self):
#   <--- frames --->
        self.register_frame = Frame(self.principal_frame, bg=branco)
        self.register_frame.place(x=100, y=50, w=1000, h=500)

        self.line_frame = Frame(self.principal_frame, bg=preto)
        self.line_frame.place(x=300, y=200, w=700, h=1)

        self.line_frame = Frame(self.principal_frame, bg=preto)
        self.line_frame.place(x=300, y=280, w=700, h=1)

        self.line_frame = Frame(self.principal_frame, bg=preto)
        self.line_frame.place(x=300, y=360, w=700, h=1)

        self.line_frame = Frame(self.principal_frame, bg=preto)
        self.line_frame.place(x=300, y=440, w=700, h=1)

#   <--- texts --->
        self.principal_title = Label(self.principal_frame, text='Agenda Telefônica', bg=branco, fg=preto, font='bold 35')
        self.principal_title.place(x=430, y=70)

        self.entry_info_nome = Label(self.register_frame, text='Nome:', bg=branco, fg=preto, font='inter 15')
        self.entry_info_nome.place(x=100, y=120)

        self.entry_info_number1 = Label(self.register_frame, text='Numero 1:', bg=branco, fg=preto, font='inter 15')
        self.entry_info_number1.place(x=100, y=200)

        self.entry_info_number2 = Label(self.register_frame, text='Numero 2:', bg=branco, fg=preto, font='inter 15')
        self.entry_info_number2.place(x=100, y=280)

        self.entry_info_number3 = Label(self.register_frame, text='Numero 3:', bg=branco, fg=preto, font='inter 15')
        self.entry_info_number3.place(x=100, y=360)

#   <--- intput --->
        self.entry_nome = Entry(self.register_frame, font='inter 15', bg=branco, borderwidth=0)
        self.entry_nome.place(x=200, y=120, w=700, h=30)

        self.entry_number_for_contact1 = Entry(self.register_frame, font='inter 15', borderwidth=0)
        self.entry_number_for_contact1.place(x=200, y=200, w=700, h=30)

        self.entry_number_for_contact2 = Entry(self.register_frame, font='inter 15', borderwidth=0)
        self.entry_number_for_contact2.place(x=200, y=280, w=700, h=30)

        self.entry_number_for_contact3 = Entry(self.register_frame, font='inter 15', borderwidth=0)
        self.entry_number_for_contact3.place(x=200, y=360, w=700, h=30)

#   <--- buttons --->
        self.button_register = Button(self.register_frame, text='Cadastrar Contato', fg=preto, font='inter 18')
        self.button_register.place(x=300, y=420)

        self.button_view_contacts = Button(self.register_frame, text='Ver Contatos', fg=preto, font='inter 18')
        self.button_view_contacts.place(x=550, y=420)


app = agenda_telefonica()
app.window_register_contact()
app.window.mainloop()