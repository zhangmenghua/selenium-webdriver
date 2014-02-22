directions=['north','south','east','west','west','down','up','left','right''back']
verbs=['go','stop','kill','eat']
stops=['the','in','of','from','at','it']
nouns=['door','bear','princess','cabinet']
numbers=[0,1,2,3,4,5,6,7,8,9,91234]
def convert_number(word):
	try:
		return int(word)
	except ValueError:
		return None
class lexicon:	
	sen=[]	
	@classmethod
	def scan(cls,stuff):
		cls.stuff=stuff
		words=stuff.split()

		for word in words:
			if word in directions:
				cls.sen.append(('direction',word))
			elif word in verbs:
				cls.sen.append(('verb',word))
			elif word in stops:
				cls.sen.append(('stop',word))
			elif word in nouns:
				cls.sen.append(('noun',word))
			elif convert_number(word):
				cls.sen.append(('number',convert_number(word)))
			else:
				cls.sen.append(('error',word))
		return cls.sen
class ParserError(Exception):
	pass
class Sentence(object):
	def __init__(self,subject,verb,object2):
		self.subject=subject[1]
		self.verb=verb[1]
		self.object2=object2[1]
	def peek(word_list):
		if word_list:
			word=word_list[0]
			return word[0]
		else:
			return None
	def match(word_list,expecting):
		if word_list:
			word=word_list.pop(0)
			if word[0]==expecting:
				return word
			else:
				return None
		else:
			return None
	def skip(word_list,word_type):
		while peek(word_list)==word_type:
			match(word_list,word_type)
	def parse_verb(word_list):
		skip(word_list,'stop')
		if peek(word_list)=='verb':
			return match(word_list,'verb')
		else:
			raise ParserError("Excepted a verb next.")
	def parse_object(word_list):
		skip(word_list,'stop')
		next=peek(word_list)
		if next=='noun':
			return match(word_list,'noun')
		if next=='direction':
			return match(word_list,'direction')
		else:
			raise ParserError("Excepted a noun or direction next.")
	def parse_subject(word_list,subj):
		verb=parse_verb(word_list)
		obj=parse_object(word_list)
		return Sentence(subj,verb,obj)
	def parse_sentence(word_list):
		skip(word_list,'stop')
		start=peek(word_list)
		if start=='noun':
			subj=match(word_list,'noun')
			return parse_subject(word_list,subj)
		elif start=='verb':
			return parse_subject(word_list,('noun','player'))
		else:
			raise ParserError("Must start with subject,object,or verb not:%s" %start)

