#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import csv
from bandit import *

def get_csv_machine(filename,delim):
	with open(filename,'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=delim)
		machines = []
		for i, row in enumerate(spamreader):
			if i == 0: # extract the names
				machines = [MachineList([]) for c in row]
				for j,c in enumerate(row):
					machines[j].setName(c)
			else:
				for j,c in enumerate(row):
					machines[j].plays.append(float(c))
	return machines
