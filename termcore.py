import asyncore
import time
import signal
from threading import Thread

class termcore:
	_name = 'junk'
	_domain = 'junkville'
	_directory = '/some/jonk'
	prompt = _name + "@" + _domain +":" + _directory + "$ "
	_currentProcess = None


	def preExec(self, command):
		pass

	def postExec(self, response):
		pass

	def Exec(self, payload):
		pass

	#loop for imitating a terminal
	def cycle(self):
		#bash style name-domain-directory
		termbanner = self._name + "@" + self._domain + ":" + self._directory + "$ "
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

	#Routine for running single command on the system
	def _cycle_single_command(self, command, params):
		if command == "cd":
			self.cd(params[0])
		if command == "exit":
			exit(0)
		else:
			time.sleep(100000)
		_payload 	= self.preExec(command)
		_response 	= self.Exec(_payload)
		_output 	= self.postExec(_response)


	def __init__(self, name,domain,initialDirectory):
		_name = name
		_domain = domain
		_directory = initialDirectory
		signal.signal(signal.SIGINT, self._sigintHandler)
		while True:
			self.cycle()


	#Handle sigint so we can pipe \x03 to the running processes, and not kill the pseudoterminal
	def _sigintHandler(self,signum,frame):
		print("Sigint")
		try:
			_currentProcess.kill()
		except:
			print("No processes running")
















term = termcore("junk", "junkville", "/root/junk")