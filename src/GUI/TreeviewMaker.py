import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk

class TreeviewMaker:
    def __init__(self, pos, headings, displaheadings, rowheight, width, theme):
        self.pos = pos
        self.headings = headings
        self.displayHeadings = displaheadings
        self.rowheight = rowheight
        self.width = width
        self.bntFont = Font(family = "Segoe Ui", size = "16")
        self.theme = theme

        self.treeview = ttk.Treeview(self.pos, style = self.theme)
        self.treeview.grid(row=0,column=0)
        self.treeview['columns'] = headings
        self.treeview['displaycolumns'] = self.displayHeadings
        self.treeview.heading('#0', text = '', anchor = 'w')
        self.treeview.column('#0', width=1, anchor = 'w', stretch = tkinter.NO)
        for i in self.displayHeadings:
            self.treeview.heading(i, text = i, anchor = 'w')
            self.treeview.column(i, width = self.width, anchor = 'w')

