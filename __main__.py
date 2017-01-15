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
from GUI import *



if __name__ == '__main__':
    fenetre = Tk()
    BMF = BanditMainFrame(fenetre)
    BMF.pack()
    fenetre.mainloop()














