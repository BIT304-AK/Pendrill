import requests


class ScanHeaders:
	def __init__(self, url):
		self.url = url
		response = requests.get(self.url)
		self.headers = response.headers
		self.cookies = response.cookies
	
	def scan_cookie(self, cookie):
		if cookie.secure:
			return("Secure")
		else:
			return("Secure attribute not set")

	def scan_xxss(self):
		try:
			if self.headers["X-XSS-Protection"]:
				return("X-XSS-Protection: PASS")
		except KeyError:
			return("X-XSS-Protection header not present: FAIL")

	def scan_xContent(self):
		try:
			if self.headers["X-Content-Type-Options"].lower() == "nosniff":
				return("X-Content-Type-Options: PASS")
			else:
				return("X-Content-Type-Options header not set correctly: FAIL")
		except KeyError:
			return("X-Content-Type-Options header not present: FAIL")


	def scan_xframe(self):
		try:
			if "deny" in self.headers["X-Frame-Options"].lower():
				return("X-Frame-Options: PASS")
			elif "sameorigin" in self.headers["X-Frame-Options"].lower():
				return("X-Frame-Options: PASS")
			else:
				return("X-Frame-Options header not set correctly: FAIL")
		except KeyError:
			return("X-Frame-Options header not present: FAIL")

	def scan_hsts(self):
		try:
			if self.headers["Strict-Transport-Security"]:
				return("Strict-Transport-Security: PASS")
		except KeyError:
			return("Strict-Transport-Security header not present: FAIL")


	def scan_policy(self):
		try:
			if self.headers["Content-Security-Policy"]:
				return("Content-Security-Policy: PASS")
		except KeyError:
			return("Content-Security-Policy header not present: FAIL")


	def scan_secure(self, cookie):
		if cookie.secure:
			return("Secure: PASS")
		else:
			return("Secure attribute not set: FAIL")

	def scan_httponly(self, cookie):
		if cookie.has_nonstandard_attr('httponly') or cookie.has_nonstandard_attr('HttpOnly'):
			return ("HttpOnly: PASS")
		else:
			return("HttpOnly attribute not set: FAIL")

	def doAll(self):
		text = ""
		for headers in self.headers:
	 		text += headers + ":" + "".join(self.headers[headers])
		text += "\n" + self.scan_xxss()
		text += "\n" + self.scan_xContent()
		text += "\n" + self.scan_xframe()
		text += "\n" + self.scan_hsts()
		text += "\n" + self.scan_policy()
		for cookie in self.cookies:
			
			text += "\nSet-Cookie:" + cookie.name + " ===> " + cookie.value
			text += "\n" + self.scan_secure(cookie)
			text += "\n" + self.scan_httponly(cookie)
		return text
		# for headers in url.headers:
	 	# 	print(headers, ":", url.headers[headers])

if __name__ == "__main__":
	#https://help.edu.my/
	url = ScanHeaders("https://help.edu.my/")

	# for headers in url.headers:
	# 	return(headers, ":", url.headers[headers])

	# return()

	# url.scan_xxss()
	# url.scan_xContent()
	# url.scan_xframe()
	# url.scan_hsts()
	# url.scan_policy()

	# for cookie in url.cookies:
	# 	return("Set-Cookie:")
	# 	return(cookie.name + " ===> " + cookie.value)
	# 	url.scan_secure(cookie)
	# 	url.scan_httponly(cookie)
	# 	return()

