#!/usr/bin/env python
from __future__ import print_function
import argparse
import sys
import math
from numpy import random

#Check whether to print colors or not
try:
	from termcolor import colored,cprint
	print_green = lambda x: cprint(x,'green',attrs=['bold'])
	print_red = lambda x: cprint(x,'red',attrs=['bold'])
	print_blue = lambda x: cprint(x,'blue',attrs=['bold'])
	print_white = lambda x: cprint(x,'white',attrs=['bold'])
	print_yellow = lambda x: cprint(x,'yellow',attrs=['bold'])
except ImportError:
	print_green = lambda x: print(x)
	print_red = lambda x: print(x)
	print_blue = lambda x: print(x)
	print_white = lambda x: print(x)
	print_yellow = lambda x: print(x)

#(Credit: http://stackoverflow.com/a/20007730)
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

def roll(die=20,num=1):
    die += 1
    random.RandomState()
    return random.randint(1,high=die,size=num)

def print_roll(args):
	i = 0
	if args.advantage is False and args.disadvantage is False:
		rol = str(args.number)+'d'+str(args.dice)
		myroll = roll(args.dice,args.number)
		for r in myroll:
			i += 1
			if r == args.dice:
				print_green("You rolled a crit! "+ str(r))
			elif r == 1:
				print_red("Critical Miss! "+ str(r))
			else:
				print_white(str(ordinal(i))+" throw is a "+ str(r))

		if args.modifier:
			print_yellow("Total for " + rol + " with modifier of " + str(args.modifier) + ":")
			print_green(sum(myroll) + args.modifier)
		else:
			print_blue("Total for " + rol + ":")
			print_green(sum(myroll))
	else:
		rol = str(args.number)+'d'+str(args.dice)+ ' with ' + ('disadvantage:','advantage:')[args.advantage]
		myroll = roll(args.dice, 2)
		for r in myroll:
			i += 1
			print_white(str(ordinal(i))+" throw is a "+ str(r))

		print_green(rol) if args.advantage else print_red(rol)
		print_blue(max(myroll) if args.advantage else min(myroll))
		if args.modifier:
			print_yellow("with modifier of " + str(args.modifier) + ":")
			print_blue(max(myroll)+args.modifier if args.advantage else min(myroll)+ args.modifier)


try:
	parser = argparse.ArgumentParser(description='DnD Dice Roller')
	parser.add_argument('-d','--dice', help="Type of dice to roll", nargs='?',type=int)
	parser.add_argument('-n','--number', help="Number of dice to roll", type=int, default=1)
	parser.add_argument('-m','--modifier', help="Modifier to add to total",type=int, default=0)
	parser.add_argument('-A','--advantage',help="Roll two dice and return the larger one",action='store_true')
	parser.add_argument('-D','--disadvantage',help="Roll two dice and return the smaller one",action='store_true')
	args = parser.parse_args()

	if args.dice is None:
		args.dice = 20

	print_roll(args)

except:
	e = sys.exc_info()[0]
