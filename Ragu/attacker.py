class Attacker(object):
	"""docstring for Attacker"""
	def __init__(self, arg):
		super(Attacker, self).__init__()
		self.arg = arg

	def attack(self,sentence):
		return "placeholder, please use specific Attacker instead"


class Ragu(Attacker):
	"""docstring for Ragu"""
	def __init__(self, arg):
		super(Ragu, self).__init__()
		self.arg = arg

	def attack(self,sentence):
		sentence = sentence + "- attacked"
		return sentence
		
		