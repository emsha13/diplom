from time import strptime, asctime
import functools as ft

#class for storage statistic instance and write it to the file
class Statistic():
	
	def __init__(self, questions):

		#create the name of statistic instance using the current date and time
		s = str()
		for k in range(6):
			if len(str(strptime(asctime())[k])) < 2:
				s += '0' + str(strptime(asctime())[k])
			else:
				s += str(strptime(asctime())[k])
			s += '_'
		self.name = s[:-1]

		#copy list of questions
		self.questions = questions

		#find languages used in current test
		self.langs = tuple({q.language for q in questions})

		#crate statistics instance
		self.stat = self.gen_stat()

		#write statistic instance to the file
		self.write_stat()
	
	def gen_stat(self):
		ar = [self.name]
		for k in self.questions:
			ar.append([k.number, k.language_name, k.text, k.text_rus, k.text_color, k.time, k.correctly])
		return ar
	
	def write_stat(self):
		try:
			fname = 'statistics_fles\\' + self.stat[0] + '.txt'
			with open(fname, 'w', encoding = 'utf-8') as f:
				for k in self.stat:
					f.write(str(k) + '\n')
		except FileNotFoundError:
			fname = self.stat[0] + '.txt'
			with open(fname, 'w', encoding = 'utf-8') as f:
				for k in self.stat:
					f.write(str(k) + '\n')

#class for storage main atributes of tests' questions
class Question():
	def __init__(self):

		#number of test's question 
		self.number = 0

		#question's language instance 
		self.language = 0

		#question's languages name
		self.language_name = 0

		#question's text
		self.text = 0

		#questions color
		self.color = 0

		#translate question's text to the russian language
		self.text_rus = 0

		#translate question's color to the russian language
		self.text_color = 0

		#start time point
		self.start_time = 0

		#stop time point
		self.stop_time = 0

		#time was spent for answer
		self.time = self.stop_time - self.start_time
		
		#check the answer's correctly, if correct: 1, if catch: -1, else: 0
		self.correctly = 0
	
	def __repr__(self):
		return str(self.time)