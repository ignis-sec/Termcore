


class termcore:
	def arrangeInput(command):
		pass

	def arrangeOutput(response):
		pass

	def execute(payload):
		pass

	def cycle():
		termbanner = name + "@" + domain +":" directory + "$ "
		cmd = input(termbanner)
		#split command and parameters
		parameters = ""
		_cycle_single_command(cmd, parameters)

	def cd(directory):
		pass

	def _cycle_single_command(command, params):
		if command == "cd":
			cd(params[0])
		_payload 	= arrange_input(command)
		_response 	= execute(_payload)
		_output 	= arrange_output(_response)

	def __init(name,domain,initialDirectory):
		#handle parameters here
		while True:
			cycle()


