import tkinter as tk
from tkinter import ttk


class Tabela:

    def __init__(self):

        self.column_names = None
        self.treeview = None
        self.table_data = None

        self.window = tk.Tk()
        self.window.title('Tabela Teste')

        # Treeview
        self.column_names = ('Ranking', 'Team', 'points')

        # sticky=tk.N + tk.S + tk.W + tk.E
        self.treeview = ttk.Treeview(self.window, columns=self.column_names, show='headings')
        self.treeview.grid(row=0, column=0)
        self.treeview.configure()

        # Rolagem
        y_axis = tk.Scrollbar(orient=tk.VERTICAL, command=self.treeview.yview)
        y_axis.grid(row=0, column=1, sticky=tk.N + tk.S)
        x_axis = tk.Scrollbar(orient=tk.HORIZONTAL, command=self.treeview.xview)
        x_axis.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.treeview['yscroll'] = y_axis.set
        self.treeview['xscroll'] = x_axis.set

        # Cabeçalho
        for i in self.column_names:
            self.treeview.heading(i, text=i)


        # Dados:
        primeiro = (1, 'Botafogo', 15)
        segundo = (2, 'Palmeiras', 13)
        terceiro = (3, 'Fortaleza', 11)
        exemplo = (4, 'exemplo', 0)

        self.table_data = [primeiro, segundo, terceiro]
        cont = 0
        while cont < 18:
            self.table_data.append(exemplo)
            cont += 1

        for i in self.table_data:
            self.treeview.insert('', 'end', values=i)

        self.window.mainloop()


Tabela()
