from tkinter import *


class AppMain:

    def __init__(self):
        self.title = 'Soccer Search League'

        self.competition = None
        self.team = None

        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry("800x500+400+100")
        self.window.resizable(False, False)
        self.window.config(bg='#365949')

        self.img_address = PhotoImage(file='assets/emblem_xx.png')

        self.frame_up = Frame(self.window, height=2, bg='black')
        self.frame_up.pack(fill=X)
        self.frame_central = Frame(self.window, bg='#162E23')
        self.frame_central.pack()
        self.frame_down = Frame(self.window, height=2, bg='black')
        self.frame_down.pack(fill=X)

        self.label_up = Label(self.frame_up, font=("Times", "24", "bold italic"), bg='#3B4641', fg='black')
        self.label_up.config(text='Soccer League Search App')
        self.label_up.pack(fill=X)
        self.label_down = Label(self.frame_down, font=("'Helvetica", "16", "italic"), bg='#3B4641', fg='black')
        self.label_down.config(text='Choose the league and find your favorite team...')
        self.label_down.pack(fill=X)

        self.sub_frame_left = Frame(self.frame_central, bg='#162E23')
        self.sub_frame_left.grid(row=0, column=0, columnspan=1)
        self.sub_frame_right = Frame(self.frame_central, bg='#162E23')
        self.sub_frame_right.grid(row=0, column=1, columnspan=2)

        self.entry_title = Entry(self.sub_frame_left, bg='black', fg='white', width=48, bd=10)
        self.entry_title.grid(row=0, column=1)
        self.list_options = Listbox(self.sub_frame_left, bg='black', fg='white', height=22, width=48, bd=10)
        self.list_options.grid(row=1, column=1)

        y_axis = Scrollbar(self.sub_frame_left, orient=VERTICAL, command=self.list_options.yview)
        y_axis.grid(row=1, rowspan=22, column=0, sticky=N + S)
        self.list_options.config(yscrollcommand=y_axis.set)

        self.butt_frame = Frame(self.sub_frame_right, bg='#162E23')
        self.butt_frame.grid(row=10, column=1)
        self.img_label = Label(self.sub_frame_right, image=self.img_address, bd=15, bg='black')
        self.img_label.grid(row=10, column=45)
        self.text_place = Text(self.sub_frame_right, bg='black', fg='white', bd=15, height=17, width=50)
        self.text_place.grid(row=21, rowspan=40, column=0, columnspan=100)

        self.button_select = Button(self.butt_frame)
        self.button_return = Button(self.butt_frame)

    def clear_all(self):
        self.entry_title.delete(0, END)
        self.list_options.delete(0, END)
        self.text_place.delete(1.0, END)

    def setting_button_to(self, command):
        self.button_select.destroy()
        self.button_return.destroy()

        self.button_select = Button(self.butt_frame, bg='#3B4641', fg='white', bd=1, width=5)
        self.button_select.grid(row=0, column=0)

        self.button_select.config(text='select', command=command)

        self.button_return = Button(self.butt_frame, bg='#3B4641', fg='white', bd=1, width=5)
        self.button_return.grid(row=1, column=0)
        self.button_return.config(text='return', command=self.clear_all)

    def error_messege(self, error):
        self.text_place.delete(1.0, END)
        self.text_place.insert(END, f"Error: {error}")
