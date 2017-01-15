#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Created: 2th January 2017
# authors: Guillaume Perez
import random
from math import log
from Tkinter import * # python 3 tkinter lowercase 
import turtle
from bandit import *
from histo import *


class BanditAddFrame(Frame):
    """docstring for BanditAdd"""
    def __init__(self, master , main_window, **kwargs):
        Frame.__init__(self,master,**kwargs)
        self.master = master
        self.main_window = main_window
        self.type_var = IntVar()
        self.type_var.set(0)
        self.entry_1_var = StringVar()
        self.entry_1_var.set(0)
        self.entry_2_var = StringVar()
        self.entry_2_var.set(0)
        possible_machines = ["Gaussian", "Pseudo Random"]
        self.radios = []
        for i, m in enumerate(possible_machines):
            self.radios.append(Radiobutton(self, text=m, value=i, variable=self.type_var, command=self.set_config))
        self.entry_1 = Entry(self,textvariable = self.entry_1_var ,width=10)
        self.entry_2 = Entry(self,textvariable = self.entry_2_var ,width=10)
        self.label_entry_1 = Label(self, text="")
        self.label_entry_2 = Label(self, text="")
        self.valid_button = Button(self,text="Add", command=self.add)
        #Placement
        for i,br in enumerate(self.radios):
            br.grid(row=i,column=0)
        self.label_entry_1.grid(row=0,column=1)
        self.label_entry_2.grid(row=1,column=1)
        self.entry_1.grid(row=0,column=2)
        self.entry_2.grid(row=1,column=2)
        self.valid_button.grid(row=2,column=1)
        # 
        self.set_config()

    def set_config(self):
        if self.type_var.get() == 0: ## Gaussian
            self.label_entry_1['text'] = "Mu"
            self.label_entry_2['text'] = "Sigma"
        elif self.type_var.get() == 1: ## Pseudo Random
            self.label_entry_1['text'] = "Min"
            self.label_entry_2['text'] = "Max"


    def add(self):
        if self.type_var.get() == 0: ## Gaussian
            mu = float(self.entry_1_var.get())
            sigma = float(self.entry_2_var.get())
            self.main_window.list_machines.append(MachineGaussian(mu,sigma))
        elif self.type_var.get() == 1: ## Pseudo Random
            min_value = float(self.entry_1_var.get())
            max_value = float(self.entry_2_var.get())
            self.main_window.list_machines.append(MachinePseudoRandom(min_value,max_value))
        self.main_window.update_machines()
        self.master.destroy()


class BanditSel(Frame):
    """docstring for BanditSel"""
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.add_button = Button(self,text='add', command = self.add_bandit)
        self.list_machines = []
        self.list_label = []
        self.add_button.pack(side=BOTTOM)

    def update_machines(self):
        self.list_label.append(Label(self,text=self.list_machines[-1]))
        self.list_label[-1].pack()
        self.master.run_button['state'] = 'normal'

    def add_bandit(self):
        """
            Create an Graphic Interface for adding a Bandit
        """
        new_window = Toplevel()
        BAF = BanditAddFrame(new_window,self)
        BAF.pack()


class BanditMainFrame(Frame):
    """docstring for BanditMainFrame"""
    def __init__(self, master,**kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.label = Label(self, text = "Number of iterations : ")
        self.value = StringVar()
        self.value.set('256')
        self.label_resultat = Label(self, text = "")
        self.label_resultat.grid(row = 1, column = 1)
        self.nb_iter = Entry(self, textvariable=self.value, width=30)
        self.run_button = Button(self, text='run', command=self.LanceBandit)
        self.run_button['state'] = DISABLED
        self.BDS = BanditSel(self)
        self.histo = HistogramTurtleFrame(self)
        #placement
        self.label.grid(row = 0, column = 0)
        self.run_button.grid(row = 1, column = 0)
        self.nb_iter.grid(row = 0, column = 1)
        self.BDS.grid(row=2, column = 1)
        self.histo.grid(row=2,column=0)

    def LanceBandit(self):
        lm = self.BDS.list_machines
        bandit1 = Bandit(lm, int(self.value.get()))
        bandit1.run()
        self.label_resultat['text'] = "Total : " + str(bandit1.value) + ", average = {0:.2f}".format(bandit1.value / float(self.value.get()))
        stats = [sum([1 for m in bandit1.choice_m if m == i]) for i in range(len(lm))]
        self.histo.drawHistogram(stats,lm)
        HistoGen(stats,lm)








