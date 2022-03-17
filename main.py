import tkinter as tk
from tkinter import ttk, font, BooleanVar, Checkbutton

from time import time

from main_funs import Proc
from settings import all_langs

#create class for the main instanses of app
class StartProc:
	def __init__(self):

		#define the background and texts' colors and fonts, root, frame
		self.bg_clr = '#33CDC7'
		self.text_color1 = '#1D7471'
		self.text_color2 = '#FFFFFF'
		self.button_color = '#006561'
		self.root = tk.Tk()
		self.highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=40, weight='bold')
		self.highlightFont2 = font.Font(family='Helvetica', name='appHighlightFont2', size=20, weight='bold')
		self.highlightFont3 = font.Font(family='Helvetica', name='appHighlightFont3', size=30, weight='bold')
		self.root.title('SpyTest')
		self.root.columnconfigure(0, weight = 1, minsize = 10)
		self.root.rowconfigure(0, weight = 1, minsize = 10)
		self.root.geometry('600x500')
		self.frame = tk.Frame(master = self.root, bg = self.bg_clr)
		self.frame.pack(expand = True, fill = tk.BOTH)
		
		#start title page with app's name
		self.title_page()

	def title_page(self):

		#create the support frame for title page and label of app's name
		self.frame_start = tk.Frame(self.frame, bg = self.bg_clr, height = self.frame['height'])
		self.lb_st = ttk.Label(self.frame_start, padding = 100, text = 'SpyTest', 
							font = self.highlightFont, foreground = self.text_color1, background = self.bg_clr)
		self.frame_start.pack(expand = True, fill = tk.BOTH)
		self.lb_st.pack(expand = True)

		#set the time for showing title page with app's name
		t = time() + 2
		while time() < t:
			self.root.update()
		
		#start the main page for choice languges for test 
		self.chose_page()

	def chose_page(self, *args):

		#cleaning main frame
		for k in self.frame.winfo_children():
			k.destroy()

		#create the support frame for languges choice and label for explain	
		self.frm = tk.Frame(self.frame, background = self.bg_clr)
		self.frm.pack(expand = True, fill = tk.BOTH)
		lb = ttk.Label(self.frm, text = 'Please, choice Laguages you speak.', 
							font = self.highlightFont2, foreground = self.text_color2, background = self.bg_clr)
		lb.place(relx = 0.5, rely = 0.05, anchor = 'n')

		#create checkboxes' variables list and set defualt
		self.checkbox = {lan : BooleanVar() for lan in all_langs}
		self.checkbox[all_langs[0]].set(True)
		self.checkbox[all_langs[1]].set(True)
		self.checkbox[all_langs[2]].set(True)

		#create checkbox widgets' list
		self.checkboxes = [Checkbutton(self.frm, text = lan.name, variable = self.checkbox[lan], 
							font = self.highlightFont2, bg = self.bg_clr, fg = self.text_color1,
							activebackground = self.bg_clr, activeforeground = self.text_color1, selectcolor = self.bg_clr)
							for lan in self.checkbox]

		#locate checkboxes widgets in column
		for k in range(len(self.checkboxes)):
			self.checkboxes[k].place(relx = 0.35, rely = 0.2 + 0.1*k)

		#create button for go to next page
		lb_bt = tk.Button(self.frm, text = 'Next', font = self.highlightFont3, padx = 50, activebackground = self.bg_clr,
									activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr, highlightcolor = self.bg_clr)
		lb_bt.bind('<Button-1>', self.check_number_languages_page)
		lb_bt.place(relx = 0.5, rely = .8, anchor = 'n')

		#create button for exit the app
		but_quit = tk.Button(self.frame, text = 'x', font = self.highlightFont2, activebackground = self.bg_clr,
									activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		but_quit.bind('<Button-1>', quit)
		but_quit.place(relx = 0.91, rely = 0.02)

		#start mainloop app
		self.root.mainloop()
	
	def check_number_languages_page(self, *args):

		#cleaning main frame
		for k in self.frame.winfo_children():
			k.destroy()

		#receive languages from the checkboxes of choice page
		self.langs = [lan for lan in all_langs if self.checkbox[lan].get()]

		#check number of languages
		if len(self.langs) > 1:
			self.start_page()

		else:
			#create the support frame for warning page and label for warning text
			self.frm = tk.Frame(self.frame, background = self.bg_clr)
			self.frm.pack(expand = True, fill = tk.BOTH)
			lb = ttk.Label(self.frm, text = 'Please chose at least two languages', 
								font = self.highlightFont2, foreground = 'white', background = self.bg_clr)
			lb.place(relx = 0.5, rely = 0.2, anchor = 'n')

			#create button for back to chose page with command self.chose_page()  
			lb_bt = tk.Button(self.frm, text = 'Back', font = self.highlightFont3, padx = 50, activebackground = self.bg_clr,
								activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
			lb_bt.bind('<Button-1>', self.chose_page)
			lb_bt.place(relx = 0.5, rely = 0.8, anchor = 'n')

			#create buttons for back and exit 
			but_back = tk.Button(self.frame, text = '<', font = self.highlightFont2, activebackground = self.bg_clr,
									activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
			but_back.bind('<Button-1>', self.chose_page)
			but_back.place(relx = 0.02, rely = 0.02)
			but_quit = tk.Button(self.frame, text = 'x', font = self.highlightFont2, activebackground = self.bg_clr,
									activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
			but_quit.bind('<Button-1>', quit)
			but_quit.place(relx = 0.91, rely = 0.02)
			
	def start_page(self, *args):

		#cleaning main frame
		for k in self.frame.winfo_children():
			k.destroy()
			
		#create the support frame for example page and label for task
		self.frm = tk.Frame(self.frame, background = self.bg_clr)
		self.frm.pack(expand = True, fill = tk.BOTH)
		lb = ttk.Label(self.frm, text = 'After Start, please select \nthe color of the written word.\n\nExample:', 
							font = self.highlightFont2, foreground = 'white', background = self.bg_clr)
		lb.place(relx = 0.5, rely = 0.05, anchor = 'n')

		#create support frame for example looks like in test with label with text
		self.frm1 = tk.Frame(self.frame, background = self.bg_clr)
		self.frm1.place(relx = 0.5, rely = 0.55, anchor = 'center', relheight = 0.4, relwidth = 0.6)
		lb_textes = ttk.Label(self.frm1,  text = 'white', 
					font = self.highlightFont2, foreground = 'red', background = self.bg_clr)
		lb_textes.place(relx = 0.5, rely = 0.07, anchor = 'center')
		
		#create support frame for buttons for example
		self.frm_buts = tk.Frame(self.frm1, background = self.bg_clr)
		self.frm_buts.place(relx = 0.5, rely = 0.5, anchor = 'center', relheight = 0.6, relwidth = 1)

		#create buttons for example with disable state and write variant 
		but1 = tk.Button(self.frm_buts, text = 'white', disabledforeground = self.text_color2, state = 'disable', 
						background = self.bg_clr, font = self.highlightFont2)
		but1.place(relx = 0, rely = 0, relheight = .5, relwidth = .5)
		but2 = tk.Button(self.frm_buts, text = 'black', disabledforeground = self.text_color2, state = 'disable',
						background = self.bg_clr, font = self.highlightFont2)
		but2.place(relx = .5, rely = 0, relheight = .5, relwidth = .5)
		but3 = tk.Button(self.frm_buts, text = 'green', disabledforeground = self.text_color2, state = 'disable', 
						background = self.bg_clr, font = self.highlightFont2)
		but3.place(relx = 0, rely = .5, relheight = .5, relwidth = .5)
		but4 = tk.Button(self.frm_buts, text = 'red', disabledforeground = self.text_color2, state = 'disable',
						background = 'green2', font = self.highlightFont2)
		but4.place(relx = .5, rely = .5, relheight = .5, relwidth = .5)
		
		#create label for explain example 
		lb_ans = ttk.Label(self.frm1, text = 'Correct answer is \'red\'', 
							font = self.highlightFont2, foreground = 'white', background = self.bg_clr)
		lb_ans.place(relx = 0.5, rely = 0.95, anchor = 'center')

		#create button for start test with command self.start()  
		lb_bt = tk.Button(self.frm, text = 'Start', font = self.highlightFont3, padx = 50, activebackground = self.bg_clr,
							activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		lb_bt.bind('<Button-1>', self.start)
		lb_bt.place(relx = 0.5, rely = 0.8, anchor = 'n')

		#create buttons for back and exit 
		but_back = tk.Button(self.frame, text = '<', font = self.highlightFont2, activebackground = self.bg_clr,
								activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		but_back.bind('<Button-1>', self.chose_page)
		but_back.place(relx = 0.02, rely = 0.02)
		but_quit = tk.Button(self.frame, text = 'x', font = self.highlightFont2, activebackground = self.bg_clr,
								activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		but_quit.bind('<Button-1>', quit)
		but_quit.place(relx = 0.91, rely = 0.02)
		
		#start again app's mainloop 
		self.root.mainloop()

	def start(self, *args):

		#create the main instance of process
		self.proc = Proc(self.langs)

		#start the test
		self.fun()

	#function for create a test page with label of question and buttons for answers' variants
	def fun(self, *args):

		#cleaning the main frame
		for k in self.frame.winfo_children():
			k.destroy()

		#create support frame for testword locate
		self.frm1 = tk.Frame(self.frame, background = self.bg_clr)
		self.frm1.pack(expand = True, fill = tk.BOTH)

		#receive the text and text color from the Text_ instance of the Proc instance
		lb_textes = ttk.Label(self.frm1, padding = (10, 150, 10, 0), text = self.proc.text.word, 
					foreground = (lambda tup: '#' + ''.join([hex(x)[2:] if len(hex(x)) == 4 else hex(x)[2:] + '0' for x in tup]))(self.proc.text.color), 
					background = self.bg_clr, font = self.highlightFont,)
		lb_textes.pack()

		#create the support frame for the buttons locate 
		self.frm_buts = tk.Frame(self.frame, background = self.bg_clr)
		self.frm_buts.pack(expand = True, fill = tk.BOTH)

		#create the buttons using Buttons instance of the Proc instance
		buts = list()
		for but in self.proc.buts.text_buttons:
			but = tk.Button(self.frm_buts, text = self.proc.buts.text_buttons[but], pady = 20, activebackground = self.bg_clr,
								activeforeground = self.text_color2, bg = self.bg_clr, fg = self.text_color2,  font = self.highlightFont3)
			but.bind('<Button-1>', self.buts_fun)
			buts.append(but)
		
		#locate buttons 2X2
		buts[0].place(relx = 0, rely = 0, relheight = .5, relwidth = .5)
		buts[1].place(relx = .5, rely = 0, relheight = .5, relwidth = .5)
		buts[2].place(relx = 0, rely = .5, relheight = .5, relwidth = .5)
		buts[3].place(relx = .5, rely = .5, relheight = .5, relwidth = .5)

		#create buttons for back and exit
		but_back = tk.Button(self.frame, text = '<', font = self.highlightFont2, activebackground = self.bg_clr,
								activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		but_back.bind('<Button-1>', self.start_page)
		but_back.place(relx = 0.02, rely = 0.02)
		but_quit = tk.Button(self.frame, text = 'x', font = self.highlightFont2, activebackground = self.bg_clr,
								activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		but_quit.bind('<Button-1>', quit)
		but_quit.place(relx = 0.91, rely = 0.02)
		
	#function for detect the finis of test and return the result or continue the cycle
	def buts_fun(self, *args):

		#receive the answer from the pressed button by attr - 'text'
		answer = args[0].widget['text']

		#cleaning the main frame
		for k in self.frame.winfo_children():
			k.destroy()

		#put answer to the Question instance using the method test_page of Proc instance
		self.proc.test_page(self.proc.i, self.proc.text, answer)
		
		#check finish of test and return the result 
		if self.proc.i == self.proc.settings.q_n:
			#if stop cycle and return result
			self.last_page()
		else:
			#continue the test using the method cycle of Proc instance for generation a new question
			self.proc.cycle(self.proc.i)

			#cycle of test page
			self.fun()

	#function of return the result
	def last_page(self):

		#cleaning the main frame
		for k in self.frame.winfo_children():
			k.destroy()

		#check instance of Analysis has result and convert to readable form
		if self.proc.finish_proc():
			result = str(self.proc.finish_proc()[0])
			text = f'Your native language is {result}'
		else:
			text = 'Immpossible detect your native language'

		#create label of result/answer
		lbl = tk.Label(self.frame, text = text, pady = 200, 
							font = self.highlightFont2, bg = self.bg_clr, fg = self.text_color1)
		lbl.pack()
		lb_bt = tk.Button(self.frame, text = 'Main page', font = self.highlightFont3, padx = 50, activebackground = self.bg_clr,
							activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		
		#create button for go to the chose page and exit the app
		lb_bt.bind('<Button-1>', self.chose_page)
		lb_bt.place(relx = 0.5, rely = 0.8, anchor = 'n')
		but_quit = tk.Button(self.frame, text = 'x', font = self.highlightFont2, activebackground = self.bg_clr,
								activeforeground = self.button_color, fg = self.button_color, background = self.bg_clr)
		but_quit.bind('<Button-1>', quit)
		but_quit.place(relx = 0.91, rely = 0.02)

#start the app
StartProc()