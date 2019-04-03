#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

state = {}

def main():
	get_name()
	play()

def exit():
	sys.exit()

# Ask for a name
def get_name():
	state['name'] = raw_input('What is your name? ')
	print ('Nice to meet you {}'.format(state['name']))

# Ask a yes/no question
def ask(question):
	raw_answer = raw_input('>> {} (y/n): '.format(question))
    
	if len(raw_answer) < 1:
		return ask(question)
    
	answer = raw_answer.lower() 
    
	if answer[0] == 'n':
		return False
	elif answer[0] == 'y':
		return True
	else:
		print ('whaT DID YOU SAY?? (ノಠ益ಠ)ノ')
		return ask(question)

# Start the game!
def play():
	answer = ask('Want to play a game?')
	if answer:
		intro()
	else:
		print ('WELL THEN GET OUT\n(╯°□°）╯︵ ┻━┻☆()ﾟOﾟ)')
		exit()
    
def intro():
	greeting = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the cavern of secrets!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Great. Let's get started {}
You enter a dark cavern. It is dark and cold. 
You should have brought a jacket but you didn't 
so you'll need to keep moving to stay warm. 
You also should have brought a flashlight. 
You're not very prepared but lets do our best. 
It is dark and you can only make out a small 
stick on the floor. 
""".format(state['name'])

	print (greeting)

	answer = ask('Do you take it?')
	if answer:
		stick()
	else:
		print ('That is pretty lame. Now what are you going to poke things with? \nI think we better just quit now since you do not really want to play this game.')
		print ('GAME OVER!')
		exit()

def stick():
	print ('Thats the spirit, {}. Lets go poke some things with this stick.'.format(state['name']))
	print ('As you proceed further into the cave, you see a small glowing object.')

	answer = ask('Do you approach the object?')
	if answer:
		approach()
	else:
		print ('You are pretty boring. I guess you do not like adventure.')
		jelly = ask('Are you a big jelly brain who doesn\'t like adventure?')
		if jelly:
			print('Whatever weirdo.')
			exit()
		else:
			print('That\'s the spirit, muffin top!')
			approach()

def approach():
	print ('You approach the object. As you draw closer, you begin to make out \nthe object as an eye! The eye belongs to a giant spider!')
	print ('🕷')

	answer = ask('Do you fight the spider?')
	if answer:
		print ('Damn! You crazy, son! The spider attacks you. Aw snap! \nYou are now dead. Better luck next time {}'.format(state['name']))
		print ('GAME OVER')
		exit()
	else:
		spider()

def spider():
	print ('That is a good decision. That thing looks scary as hell')
	#print ('ʕ　·ᴥ·ʔ 🐻')
	print ('🐻')

	print ('Hold on, there\'s a bear sleeping a few feet away.')

	answer = ask('Should we poke the bear in the face?')
	if answer:
		bear_time()
	else:
		print ('Well this has been a real let down')
		print ('GAME OVER')
		exit()

def bear_time():
	dialogue = """
Dude don't poke that bear.
ʕ； •`ᴥ•´ʔ 🐻
oh shoot IT'S AWAKE
"""
	print(dialogue)

	answer = ask('Should we throw the spider at it?')
	if answer:
		spider_tossing()
	else:
		escape()

def spider_tossing():
	dialogue = """
The spider bit your hand a little, but now that's the bear's problem.
The bear struggles with the spider for a bit but wins eventually 
'cause it's a freaking bear.
ʕ╯• ⊱ •╰ʔ 🐻
That reminds you, you better escape.
"""
	print (dialogue)

	answer = ask('Escape the bear\'s cave?')
	if answer:
		escape()
	else:
		bad_idea = """
After defeating the spider, the bear aproaches you.
You use your only natural defence and play dead.
A few hours later you wake up outside the cave, 
a 'keep out' sign written in angry bear hand writing posted in front.
"""
		print(bad_idea)
		escape()

def escape():
	dialogue = """
That's the bear's cave now, try to remember that in case you have 
bear related issues.
"""
	print (dialogue)
	exit()

main()
