from app.AppMain import AppMain
from app.menu import create_menu, open_menu_competitions


def start():
    Start()


class Start(AppMain):

    def __init__(self):
        super().__init__()

        create_menu(self)
        open_menu_competitions(self)

        self.window.mainloop()
