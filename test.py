from termcore import termcore
import os

class myTerm(termcore):
	def Exec(self, payload):
		os.system(payload)

	def customCommands(self, command, params):
		if command == 'whoami':
			print("That command is blacklisted")
			return True
		return False
		
term = myTerm("hiddenuser", "kali")