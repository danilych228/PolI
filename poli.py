import requests
from pyfiglet import figlet_format

base_api_uri = "https://text.pollinations.ai" 
program_name = "PolI"
print(figlet_format(program_name))
username = ""


while username.strip() == "":
	username = input(f"{program_name} >>> Enter your name\n >>> ")
running = True
print(f"{program_name} >>> Hello {username}!")
while running:
	prompt = input(f"{username} >>> ")
	if prompt.lower().strip() == "/exit":
		running = False	
	else:
		response = requests.get(requests.utils.requote_uri(f"{base_api_uri}/{prompt}")).text
		print(f"{program_name} >>> {response}")
print(f"{program_name} >>> Goodbye {username}")

