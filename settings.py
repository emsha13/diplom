from statistics_m import Question

#class for storage language information
class Language():
	def __init__(self, name = 0, dict_ = 0, tuple_ = 0):
		
		#ex. 'English'
		self.name = name
		
		#dictionary of color name and color code in rgb
		#ex. {'red' : (255, 0, 0), 'green' : (0, 255, 0)}
		self.colors = dict_

		#tuple(self.colors.keys())
		#ex. ('red', 'green')
		self.counter = tuple_

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

#colors dictionary of English
colors = {'red' : (255, 0, 0), 'green' : (0, 255, 0), 
			'blue' : (0, 0, 255), 'white' : (255, 255, 255), 
			'black' : (0, 0, 0),  'yellow' : (255, 255, 0), 
			'orange': (255, 127, 0), 'pink' : (255, 0, 127), 
			'grey' : (127, 127, 127)}

#colors dictionary of Russian
tsveta = {'красный' : (255, 0, 0), 'зелёный' : (0, 255, 0), 
			'синий' : (0, 0, 255), 'белый' : (255, 255, 255), 
			'чёрный' : (0, 0, 0),  'жëлтый' : (255, 255, 0), 
			'оранжевый': (255, 127, 0), 'розовый' : (255, 0, 127), 
			'серый' : (127, 127, 127)}

#colors dictionary of Ukranian
colory = {'червоний' : (255, 0, 0), 'зелений' : (0, 255, 0), 
			'синiй' : (0, 0, 255), 'бiлий' : (255, 255, 255), 
			'чорний' : (0, 0, 0),  'жовтий' : (255, 255, 0), 
			'помаранчевий': (255, 127, 0), 'рожевий' : (255, 0, 127),
			'сірий' : (127, 127, 127)}

#colors dictionary of Belorussian
colery = {'чырвоны' : (255, 0, 0), 'зялёны' : (0, 255, 0), 
			'синий' : (0, 0, 255), 'белый' : (255, 255, 255), 
			'чёрный' : (0, 0, 0),  'жëлтый' : (255, 255, 0), 
			'оранжевый': (255, 127, 0), 'розовый' : (255, 0, 127), 
			'серый' : (127, 127, 127)}

#colors dictionary of Greek
grc_colors = {'κόκκινος' : (255, 0, 0), 'πράσινος' : (0, 255, 0), 
			'μπλε' : (0, 0, 255), 'λευκό' : (255, 255, 255), 
			'μαύρος' : (0, 0, 0),  'κίτρινος' : (255, 255, 0), 
			'πορτοκάλι' : (255, 127, 0), 'ροζ' : (255, 0, 127), 
			'γκρί' : (127, 127, 127)}

#counters of previous dictionarys
con_count = tuple(colors.keys())
pos_tsv = tuple(tsveta.keys())
con_col = tuple(colory.keys())
con_colery = tuple(colery.keys())
grc_counter = tuple(grc_colors.keys())

#create the languages instances
eng = Language('English', colors, con_count)
rus = Language('Russian', tsveta, pos_tsv)
ukr = Language('Ukrainian', colory, con_col)
bel = Language('Belorussian', colery, con_colery )
grc = Language('Greek', grc_colors, grc_counter) 

#tuple of all languages app has
all_langs = eng, rus, ukr, grc, bel

#class for calculate number of questions
class Settings:
	
	def __init__(self, langs):
		
		#languages using in test 
		self.langs = langs

		#should be about 7 for each lanuages but total number shold be multiply of 5
		self.q_n = round((len(self.langs)*7)/5)*5