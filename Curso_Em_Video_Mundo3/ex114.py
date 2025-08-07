#CHALLENGE 114: Reaching a website
#GOAL: Write code that tests if it was possible to reach the website "pudim.com"
#SKILL: Learning about error and exception handling

import requests

try:
    response = requests.get('https://pudim.com/')
    print('We managed to reach "pudim.com" :) ')

except:
    print('We could not reach "pudim.com" :( ')
