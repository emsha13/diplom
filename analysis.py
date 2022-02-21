import statistics as st
from functools import partial
from copy import copy

from statistics_m import Statistic

class Analysis:

	def __init__(self, stat):
		#statistic instanse
		self.stat = stat
		#langs we use in statistic instance
		self.langs = stat.langs
		#list of questions from statistic instance
		self.questions = self.stat.questions
		#prepare dictionarys for correct and catch answers 
		self.cor_dict = {k : list() for k in self.langs}
		self.catch_dict = {k : list() for k in self.langs}
		#fill dictionarys for correct and catch answers by the questions
		self.generate_dicts()
		#prepare and fill dictionarys and lists for filtered and meaned results of time of questions
		self.cor_result = self.adv_function(self.cor_dict)
		self.catch_result = self.adv_function(self.catch_dict)
		self.list_of_cor_result = list()
		self.list_of_catch_result = list()
		self.generate_list_of_result()
		#create dictionarys variants of combination of statistic instance's languages possible exsist
		if len(self.cor_dict) == len(self.langs):
			self.cor_answer = self.cor_variants()
		if len(self.catch_dict) > 0.1*len(self.langs):
			self.catch_answer = self.catch_variants()
		#final answer depends on catch and correct answers
		self.finish_answer_find()

	#fill dictionarys for correct and catch answers by the questions
	def generate_dicts(self):
		#add to correct and catch dictioarys questions
		for q in self.stat.questions:
			if q.correctly == 1:
				self.cor_dict[q.language].append(q)
			elif q.correctly == -1:
				self.catch_dict[q.language].append(q)

		#remove waste questions
		self.cor_dict = {lan : self.cor_dict[lan] for lan in self.cor_dict if self.cor_dict[lan]}
		self.catch_dict = {lan : self.catch_dict[lan] for lan in self.catch_dict if self.catch_dict[lan]}

	#template for filter functions 
	def functions_for_dicts(self, arr, func, koef, i=0):
		#check list's end -> out of function
		if i >= len(arr) or len(arr) == 1:
			pass
		
		else:
			#remove and save question and position we check
			k = arr.pop(i)
			
			#create new list with time only
			ar4 = list()
			for m in arr:
				ar4.append(m.time)

			#compare quesion's time to rest questions
			#if greater or less than average multy coefficient of rest -> run function in begin
			if k.time > koef*func(ar4) or k.time < func(ar4)/2:
				self.functions_for_dicts(arr, func, koef)
			
			#else return question to its place and check next question
			else:
				arr.insert(i, k)
				i += 1
				self.functions_for_dicts(arr, func, koef, i)

	#fill dictionarys for filtered and meaned results of time of questions
	def adv_function(self, dictan):
		#functions we will use
		list_of_st_funs = st.median, st.mean, st.harmonic_mean, st.geometric_mean
		
		#create list of functions for work with dicts
		filter_functions = list()
		for f in list_of_st_funs:
			for k in [1.5, 2]:
				filter_functions.append(partial(self.functions_for_dicts, func = f, koef = k))

		#create a dict which contains filtered dicts 
		results = dict()
		results[lambda x : x] = dictan
		for fun in filter_functions:
			results[fun] = {k : list() for k in dictan}
			for lan in dictan:
				results[fun][lan] = dictan[lan].copy()
				fun(results[fun][lan])

		#create a dict which contains adv result of filtered dicts
		result = {fil_fun : 
					{st_fun : 
						{lan : st_fun([q.time for q in results[fil_fun][lan]])
		 					for lan in results[fil_fun]} 
		 						for st_fun in list_of_st_funs} 
		 							for fil_fun in results}
		
		return result

	#fill lists for filtered and meaned results of time of questions
	def generate_list_of_result(self):
		for dict_ in self.cor_result.values():
			self.list_of_cor_result.extend(dict_.values())
		for dict_ in self.catch_result.values():
			self.list_of_catch_result.extend(dict_.values())


	#create dictionarys variants of combination of statistic instance's languages possible exsist and count it for correct
	def cor_variants(self):
		dict_of_answer_4 = {st.mean([k[lan] for k in self.list_of_cor_result]) : lan for lan in self.list_of_cor_result[0].keys()}
		
		sorted_ = list(dict_of_answer_4)
		sorted_.sort()
		sorted_.reverse()
		
		answer_4 = {k + 1 : dict_of_answer_4[sorted_[k]] for k in range(len(sorted_))}

		return tuple(answer_4.values())

	#create dictionaries variants of combination of statistic instance's languages possible exsist and count it for catch
	def catch_variants(self):
		dict_of_answer_4 = {st.mean([k[lan] for k in self.list_of_catch_result]) : lan for lan in self.list_of_catch_result[0].keys()}
		
		sorted_ = list(dict_of_answer_4)
		sorted_.sort()

		answer_4 = {k + 1 : dict_of_answer_4[sorted_[k]] for k in range(len(sorted_))}
		
		return tuple(answer_4.values())
	
	#create the finish answer
	def finish_answer_find(self):

		try:
			#if all using languages have at least one correct answer
			if len(self.langs) == len(self.cor_dict):

				#native language is correct answers' native languages
				self.finish_answer = self.cor_answer

			#if at least one language has all catch answer
			elif self.catch_dict:

				#native language is catch answers' language
				self.finish_answer = self.catch_answer

			else:

				#no possible determinate
				self.finish_answer = False	

		except:
			#no possible determinate
			self.finish_answer = False