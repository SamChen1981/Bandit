#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Created: 2th January 2017
# authors: Guillaume Perez
from Tkinter import * # python 3 tkinter lowercase 
import turtle
import random
import matplotlib.pyplot as plt

class HistogramTurtleFrame(Frame):
	"""docstring for histogramTurtleFrame"""
	def __init__(self, master, width_canvas = 300, height_canvas = 150, **kwargs):
		Frame.__init__(self, master, **kwargs)
		self.canvas = Canvas(self, width = width_canvas, height = height_canvas)
		self.canvas.pack()
		self.master = master
		self.width_c = width_canvas
		self.height_c = height_canvas
		self.turtle = turtle.RawTurtle(self.canvas)
		self.turtle.hideturtle()
		self.turtle.speed(0)
		self.histo_w = self.width_c - 4
		self.histo_h = self.height_c - 4
		self.left =  -self.histo_w / 2
		self.right = self.histo_w / 2
		self.top = 	self.histo_h / 2
		self.bottom= -self.histo_h / 2
		self.drawOutLine()
		
	def drawHistogram(self,list_values, objs=[]):
		"""
			Draw an bar diagram on the canavas

			:param list_values: is the relative height of the bars
			:param objs: is a list of object to be casted in str and displayed. Optional, number instead
		"""
		if len(objs) == 0: ## optional setting
			objs = range(len(list_values))
		self.turtle.clear()
		self.drawOutLine()
		bar_w = self.histo_w / len(list_values)
		for i in range(len(list_values)):
			bar_h = list_values[i] * (self.histo_h-4) / max(list_values)
			self.drawABar(self.left + i * bar_w, self.bottom , bar_w, bar_h, obj=objs[i])


	def drawABar(self,i, j, bar_w, bar_h, obj):
		self.turtle.penup()
		self.turtle.goto(i, j)
		self.turtle.write(obj)
		self.turtle.goto(i, j)
		self.turtle.setheading(90)
		self.turtle.pendown()
		self.turtle.forward(bar_h)
		self.turtle.right(90)
		self.turtle.forward(bar_w)
		self.turtle.right(90)
		self.turtle.forward(bar_h)
		self.turtle.penup()

	def drawOutLine(self):
		self.turtle.penup()
		self.turtle.goto(self.left,self.bottom)
		self.turtle.pendown()
		self.turtle.goto(self.right,self.bottom)
		self.turtle.goto(self.right,self.top)
		self.turtle.goto(self.left,self.top)
		self.turtle.goto(self.left,self.bottom)
		self.turtle.penup()

	

class HistoGen:
	def __init__(self,list_values, objs=[]):
		"""
			Draw an bar diagram on a new window using matplotlib

			:param list_values: is the relative height of the bars
			:param objs: is a list of object to be casted in str and displayed. Optional, number instead
		"""
		x = range(len(list_values))
		y = list_values
		f = plt.figure()
		ax = f.add_axes([0.1, 0.1, 0.8, 0.8])
		ax.bar(x, y, align='center', color="green")
		ax.set_xticks(x)
		ax.set_xticklabels(objs)
		f.show() 
