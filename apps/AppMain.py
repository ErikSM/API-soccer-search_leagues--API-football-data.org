from tkinter import *

from access.ApiAccess import ApiAccess
from access.info_about import names_allowed_leagues, api_account_permissions
from access.menus import competition_menu


def start():
    AppMain()


class AppMain:

    def __init__(self):

        self.title = 'Soccer Search League'
        self.img_address = None

        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry("700x500+400+100")
        self.window.resizable(False, False)
        self.window.config(bg='#365949')

        self.img_address = PhotoImage(file='assets/emblem_xx.png')

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        self.menu.add_command(label='Menu', command=self.select, background='black', foreground='white')

        self.frame_up = Frame(self.window, height=2, bg='black')
        self.frame_up.pack(fill=X)
        self.principal_frame = Frame(self.window, bg='#162E23')
        self.principal_frame.pack()
        self.frame_down = Frame(self.window, height=2, bg='black')
        self.frame_down.pack(fill=X)

        self.label_up = Label(self.frame_up, font=("Times", "24", "bold italic"), bg='#3B4641', fg='black')
        self.label_up.config(text='Soccer League Search App')
        self.label_up.pack(fill=X)
        self.label_down = Label(self.frame_down, font=("'Helvetica", "16", "italic"), bg='#3B4641', fg='black')
        self.label_down.config(text='Choose the league and find your favorite team...')
        self.label_down.pack(fill=X)

        self.sub_frame_left = Frame(self.principal_frame, bg='#162E23')
        self.sub_frame_left.grid(row=0, column=0, columnspan=1)
        self.sub_frame_right = Frame(self.principal_frame, bg='#162E23')
        self.sub_frame_right.grid(row=0, column=1, columnspan=2)

        self.list_options = Listbox(self.sub_frame_left, bg='black', fg='white', height=25, width=50)
        self.list_options.grid(row=0, column=0)

        for i in names_allowed_leagues:
            self.list_options.insert(END, i)

        self.button_frame = Frame(self.sub_frame_right, bg='#162E23')
        self.button_frame.grid(row=10, column=1)
        self.image_local_label = Label(self.sub_frame_right, image=self.img_address, bd=10, bg='black')
        self.image_local_label.grid(row=10, column=45)
        self.text_information = Text(self.sub_frame_right, bg='black', fg='white', bd=10, height=15, width=50)
        self.text_information.grid(row=21, rowspan=40, column=0, columnspan=100)

        for i in api_account_permissions:
            self.text_information.insert(END, f"\n {' ' * 5}-  {i.title()}... \n\n")

        self.button_select = Button(self.button_frame, text='Select', command=self.select)
        self.button_select.grid(row=0, column=0)
        self.button_return = Button(self.button_frame, text='return', command=self.clear_all)
        self.button_return.grid(row=1, column=0)

        self.window.mainloop()

    def select(self):
        option_selected = self.list_options.get(ANCHOR)
        selected = names_allowed_leagues[option_selected]

        api_access = ApiAccess()
        competition = api_access.open_resource_info(competition_menu, 'teams', selected)

        print(selected)

        self.clear_all()

        for i in competition:
            if i == 'teams':
                for j in competition[i]:
                    self.list_options.insert(END, j['name'])
                    print(j)

            elif i == 'competition':
                self.text_information.insert(END, competition[i]['name'])
                self.text_information.insert(END, f"\nTemporada: {competition[i]['id']}\n"
                                                  f"Emblema: {competition[i]['emblem']}\n"
                                                  f"Abreviacao: {competition[i]['code']}")

    def clear_all(self):
        self.list_options.delete(0, END)
        self.text_information.delete(1.0, END)
