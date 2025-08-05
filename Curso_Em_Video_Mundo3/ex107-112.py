#CHALLENGE 107-112: Reporting on an amount
#GOAL: Write code that imports functions made by you in a module (coin.py) so that you can print 
#some information about a monetary value. Since the exercises 107 through 112 were all about building 
#more and more functions on top of each other, I opted to just do ex112, which is the most complete one
#SKILL: Learning about modules and packets

import coin
coin.info(coin.validation(), currency='R$', reduce=40, increment=60)