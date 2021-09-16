import requests

response = requests.get('https://hlms.help.edu.my/login/index.php')
print(response.cookies)


