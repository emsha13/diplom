from time import time
from random import randint, choice

from settings import Settings, all_langs, rus
from support_funs import Buttons, Text_
from statistics_m import Statistic, Question
from analysis import Analysis

#class for all internal process in app
class Proc:

	def __init__(self, langs = False):
		
		#languages for tests' questions
		self.langs = langs
		
		#check the number of langs
		if len(self.langs) > 1:
			
			#start the process
			self.start_proc()
		
		else:
			pass

	def start_proc(self):
		
		#main instance of Settings has langs and number of questions
		self.settings = Settings(self.langs)

		#create counter for numbers of questions for each languages use in test
		self.lan_counter = {}.fromkeys(self.langs, 0)

		#create questions list with empty Question instance
		self.questions = [Question() for k in range(self.settings.q_n)]

		#start main cycle of app
		self.cycle()

	def cycle(self, i = 0):

		#compare question's number to number of necessary questions 
		if i < self.settings.q_n:

			#use original languages which was used less than necessary
			lan = self.original_lan()

			#create Text_ and Buttons instances for questions 
			self.text = Text_(lan)
			self.buts = Buttons(self.text)

			self.i = i

			#fill several attributes to the Question instance
			self.gen_question(self.i, self.text)

		else:

			#finish process and return result
			self.finish_proc()

	#compare language counter to average numbers necessary questions
	def original_lan(self):
		lan = choice(self.langs)
		while self.lan_counter[lan] >= round(self.settings.q_n/len(self.langs)):
			lan = choice(self.langs)
		self.lan_counter[lan] += 1

		return lan

	#create instances of Statistic and Analysis classes and return the result
	def finish_proc(self):
		self.statistic = Statistic(self.questions)
		self.analysis = Analysis(self.statistic)
		
		return self.analysis.finish_answer

	#fill several attributes to the Queston's instance
	def gen_question(self, i, text):
		self.questions[i].number = i + 1
		self.questions[i].language = text.lan
		self.questions[i].language_name = text.lan.name
		self.questions[i].text = text.word
		self.questions[i].text_rus = rus.counter[text.lan.counter.index(text.word)]
		self.questions[i].text_color = {color : name for name, color in rus.colors.items()}[text.color]
		self.questions[i].start_time = time()

	#check correction answer and fill rest attributes or rewrite the Question's instance
	def test_page(self, i, text, answer):
		lan = text.lan
		if lan.colors[text.word] == self.buts.lan.colors[answer]:
			self.questions[i].correctly = -1
			self.questions[i].stop_time = time()
			self.questions[i].time = self.questions[i].stop_time - self.questions[i].start_time
			self.i += 1
		elif text.color == self.buts.lan.colors[answer]:
			self.questions[i].correctly = 1
			self.questions[i].stop_time = time()
			self.questions[i].time = self.questions[i].stop_time - self.questions[i].start_time
			self.i += 1
		else:
			self.lan_counter[text.lan] -= 1