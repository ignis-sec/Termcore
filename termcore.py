import asyncore
import time
import signal
from threading import Thread
import os

class termcore:
	_name = 'junk'
	_domain = 'junkville'
	_directory = ''
	prompt = _name + "@" + _domain +":" + _directory + "$ "
	_currentProcess = None


	def preExec(self, command):
		return command

	def postExec(self, response):
		return response

	def Exec(self, payload):
		pass

	#loop for imitating a terminal
	def cycle(self):
		#bash style name-domain-directory
		termbanner = "\033[1;31m" + self._name + "@" + self._domain + "\033[1;37m:\033[1;34m" + self._directory + "\033[1;37m$ "
		print(termbanner, end='')

		cmd = input() #Need improvements, i definitely want arrow keys
		#split command and parameters
		parameters = ""
		
		#Run as a thread but wait for the thread to stop. Only reason this is run as a seperate thread is so we can keep a reference to it, and kill it with sigint
		_currentProcess = Thread(target=self._cycle_single_command, args= (cmd, parameters))
		_currentProcess.start()
		_currentProcess.join()

	#cd functions are defined by terminal, running processes have context to only their working directory, not the terminals.
	def cd(self, directory):
		pass

	def customCommands(self,command, params):
		return False

	#Routine for running single command on the system
	def _cycle_single_command(self, command, params = ''):
		if command == "cd":
			self.cd(params[0])
			return None
		if command == "exit":
			exit(0)

		if self.customCommands(command, params):
			return

		_payload 	= self.preExec(command)
		_response 	= self.Exec(_payload)
		_output 	= self.postExec(_response)


	def __init__(self, name,domain,initialDirectory=os.getcwd()):
		self._directory = initialDirectory
		self._name = name
		self._domain = domain
		
		#signal.signal(signal.SIGINT, self._sigintHandler)
		while True:
			self.cycle()


	#Handle sigint so we can pipe \x03 to the running processes, and not kill the pseudoterminal
	def _sigintHandler(self,signum,frame):
		print("Sigint")
		try:
			_currentProcess.kill()
		except:
			print("No processes running")















