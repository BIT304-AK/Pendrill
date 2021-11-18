import requests


class ScanHeaders:
	def __init__(self, url):
		self.url = url
		response = requests.get(self.url)
		self.headers = response.headers
		self.cookies = response.cookies
	
	def scan_cookie(self, cookie):
		if cookie.secure:
			print("Secure")
		else:
			print("Secure attribute not set")

	def scan_xxss(self):
		try:
			if self.headers["X-XSS-Protection"]:
				print("X-XSS-Protection: PASS")
		except KeyError:
			print("X-XSS-Protection header not present: FAIL")

	def scan_xContent(self):
		try:
			if self.headers["X-Content-Type-Options"].lower() == "nosniff":
				print("X-Content-Type-Options: PASS")
			else:
				print("X-Content-Type-Options header not set correctly: FAIL")
		except KeyError:
			print("X-Content-Type-Options header not present: FAIL")


	def scan_xframe(self):
		try:
			if "deny" in self.headers["X-Frame-Options"].lower():
				print("X-Frame-Options: PASS")
			elif "sameorigin" in self.headers["X-Frame-Options"].lower():
				print("X-Frame-Options: PASS")
			else:
				print("X-Frame-Options header not set correctly: FAIL")
		except KeyError:
			print("X-Frame-Options header not present: FAIL")

	def scan_hsts(self):
		try:
			if self.headers["Strict-Transport-Security"]:
				print("Strict-Transport-Security: PASS")
		except KeyError:
			print("Strict-Transport-Security header not present: FAIL")


	def scan_policy(self):
		try:
			if self.headers["Content-Security-Policy"]:
				print("Content-Security-Policy: PASS")
		except KeyError:
			print("Content-Security-Policy header not present: FAIL")


	def scan_secure(self, cookie):
		if cookie.secure:
			print("Secure: PASS")
		else:
			print("Secure attribute not set: FAIL")

	def scan_httponly(self, cookie):
		if cookie.has_nonstandard_attr('httponly') or cookie.has_nonstandard_attr('HttpOnly'):
			print("HttpOnly: PASS")
		else:
			print("HttpOnly attribute not set: FAIL")


if __name__ == "__main__":
	#https://help.edu.my/
	url = ScanHeaders("https://help.edu.my/")

	for headers in url.headers:
		print(headers, ":", url.headers[headers])

	print()

	url.scan_xxss()
	url.scan_xContent()
	url.scan_xframe()
	url.scan_hsts()
	url.scan_policy()

	for cookie in url.cookies:
		print("Set-Cookie:")
		print(cookie.name + " ===> " + cookie.value)
		url.scan_secure(cookie)
		url.scan_httponly(cookie)
		print()

