from random import choice, shuffle

from settings import eng

#support class for create text for answer options
class Buttons:
	def __init__(self, text):

		#app's language 
		self.lan = eng
		
		#rgb codes colors
		self.colors = list(self.lan.colors.values())

		#create inverted dictionary of languages colors
		#ex. simple - {'key1' : 'val1', 'key2' : 'val2'}
		#  inverted - {'val1' : 'key1', 'val2' : 'key2'}
		self.inv_d = {color : name for name, color in self.lan.colors.items()}

		#receive from the Text_ instance correct answer
		self.correct_button = text.color

		#remove from the list of colors
		self.colors.remove(self.correct_button)

		#receive from the Text_ instance catch answer
		self.catch_button = text.catch

		#remove from the list of colors
		self.colors.remove(self.catch_button)
		
		#create other options
		self.zero_button_1 = choice(self.colors)
		self.colors.remove(self.zero_button_1)
		self.zero_button_2 = choice(self.colors)
		
		#create the list of buttons and shuffle it
		self.buttons = [self.correct_button, self.catch_button, self.zero_button_1, self.zero_button_2]
		shuffle(self.buttons)
		
		#create the dictionary of answer options
		self.text_buttons = dict()
		for but in self.buttons:
			self.text_buttons[but] = self.inv_d[but]

#support class for create a question attributes
class Text_:
	
	def __init__(self, lan):

		#receive the question's language 
		self.lan = lan

		#rgb code text color
		self.color = choice(list(lan.colors.values()))

		#create the the text of question, color of text and their codes
		self.gen_text()

	def gen_text(self):

		#text
		self.word = choice(self.lan.counter)
		
		#choice the origin color, not match to self.color
		while self.lan.colors[self.word] == self.color:
			self.word = choice(self.lan.counter)

		#rgb code of text
		self.catch = self.lan.colors[self.word]