class Attacker(object):
	"""docstring for Attacker"""
	def __init__(self, task):
		super(Attacker, self).__init__()
		self.arg = task

	def attack(self,sentence):
		return "placeholder, please use specific Attacker instead"


class Ragu(Attacker):
	"""docstring for Ragu"""
	def __init__(self, task):
		super(Ragu, self).__init__(task)


	def attack(self,sentence):
		sentence = sentence + "- attacked"
		return sentence
		
		
