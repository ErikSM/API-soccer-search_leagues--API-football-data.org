from tkinter import *

from access.basic_information import names_allowed_leagues


class AppPrincipal:

    def __init__(self):
        self.title = 'Soccer Search League'

        self.img_address = None

        self.button_select = None
        self.button_return = None

        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry("700x500+400+100")
        self.window.resizable(False, False)
        self.window.config(bg='#365949')

        self.img_address = PhotoImage(file='../assets/emblem_xx.png')

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.menu.add_command(label='start', command=self.start)

        self.frame_up = Frame(self.window, height=2, bg='black')
        self.frame_up.pack(fill=X)
        self.principal_frame = Frame(self.window, bg='#162E23')
        self.principal_frame.pack()
        self.frame_down = Frame(self.window, height=2, bg='black')
        self.frame_down.pack(fill=X)

        self.label_up = Label(self.frame_up, font='Arial 20', bg='grey', fg='black')
        self.label_up.config(text='App Soccer Search League')
        self.label_up.pack(fill=X)
        self.label_down = Label(self.frame_down, font='Arial 20', bg='grey', fg='black')
        self.label_down.config(text='App Soccer Search League')
        self.label_down.pack(fill=X)

        self.sub_frame_left = Frame(self.principal_frame, bg='#162E23')
        self.sub_frame_left.grid(row=0, column=0)
        self.sub_frame_right = Frame(self.principal_frame, bg='#162E23')
        self.sub_frame_right.grid(row=0, column=2)

        self.list_options = Listbox(self.sub_frame_left, bg='black', fg='white', height=25, width=50)
        self.list_options.grid(row=0, column=0)

        for i in names_allowed_leagues:
            self.list_options.insert(END, i)

        self.label_image = Label(self.sub_frame_right, image=self.img_address, bd=10, bg='black')
        self.label_image.grid(row=0, column=0)
        self.list_information = Text(self.sub_frame_right, bg='black', fg='white', bd=10, height=15, width=50)
        self.list_information.grid(row=2, column=0)

        self.window.mainloop()

    def start(self):
        pass


AppPrincipal()
