#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Created: 2th January 2017
# authors: Guillaume Perez
import random
from math import log

class Machine:
	"""
		Machine used for a multi armed bandit selection algorithm
		The UCB1 method is applied
		see Auer, P., Cesa-Bianchi, N., & Fischer, P. (2002). Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2-3), 235-256.
	"""
	def __init__(self, cummulative_reward_argument = 0.):
		self.state = 0
		self.n_glob = 0
		self.choices = 0
		self.cummulative_reward = cummulative_reward_argument

	def reward(self,r):
		self.cummulative_reward += r
		self.choices += 1

	def update(self,glob_choices):
		self.n_glob = glob_choices
		self.state = (self.cummulative_reward/self.choices)+(2 * log(glob_choices) / self.choices)**0.5
#						x_j^bar								sqrt(2*ln(n)/n_j)	
		return self.state

	def getState(self):
		return self.state

	def setState(self, new_value):
		self.state = new_value

	def play(self):
		"""
			return the gain of the play.
			This value must be greater or equal than 0
		"""
		pass
	def clear(self):
		self.state = 0
		self.choices = 0
		self.cummulative_reward = 0
		self.n_glob = 0

class MachineGaussian(Machine):
	def __init__(self,mu,sigma):
		Machine.__init__(self)
		self.mu = mu
		self.sigma = sigma

	def play(self):
		return max(random.gauss(self.mu,self.sigma),0)

	def __str__(self):
		return "Gaussian({},{})".format(self.mu,self.sigma)

class MachinePseudoRandom(Machine):
	def __init__(self,v_min,v_max):
		Machine.__init__(self)
		self.v_min = v_min
		self.v_max = v_max

	def play(self):
		return max(0,self.v_min + random.random()*(self.v_max - self.v_min))

	def __str__(self):
		return "PseudoR({},{})".format(self.v_min,self.v_max)



class MachineList(Machine):
	"""
		Machine whose play at time i is the ieme value of the list given in argument

		:param plays:
	"""
	def __init__(self, plays=[]):
		Machine.__init__(self)
		self.plays = plays
		self.n_glob = 0
		self.name = ""

	def play(self):
		return self.plays[self.n_glob]

	def setName(self,name):
		self.name = name

	def __str__(self):
		return self.name 





class BanditMax:
	def __init__(self, lm, iterations):
		self.lm = lm
		self.iterations = iterations
		self.value = 0.
		self.choice_m = []
		for m in lm:
			m.clear()

	def run(self):
		lg = [m.play() for m in self.lm]
		max_gain = max(max(lg),0.0001) # in case of all the machines return 0.
		for i, g in enumerate(lg):
			self.lm[i].reward(g / max_gain)
			self.choice_m.append(i)
		self.value = sum(lg)
		for it in range(self.iterations):
			states = [m.update(len(self.choice_m)) for m in self.lm]
			max_state = max(states)
			m_id = states.index(max_state)
			g = self.lm[m_id].play()
			max_gain = max(max_gain, g)
			self.lm[m_id].reward(g / max_gain)
			self.choice_m.append(m_id)
			self.value += g



class BanditMin:
	def __init__(self, lm, iterations):
		self.lm = lm
		self.iterations = iterations
		self.value = 0.
		self.choice_m = []
		for m in lm:
			m.clear()

	def run(self):
		lg = [m.play() for m in self.lm]
		min_gain = max(min(lg),0.1) # in case of all the machines return 0.
		for i, g in enumerate(lg):
			self.lm[i].reward(min_gain / g)
			self.choice_m.append(i)
		self.value = sum(lg)
		for it in range(self.iterations):
			states = [m.update(len(self.choice_m)) for m in self.lm]
			max_state = max(states)
			m_id = states.index(max_state)
			g = self.lm[m_id].play()
			min_gain = min(min_gain, g)
			self.lm[m_id].reward(min_gain/g)
			self.choice_m.append(m_id)
			self.value += g







