#!/usr/bin/env python
from __future__ import print_function
import argparse
import sys


from numpy import random
def roll(die=20,num=1):
    die += 1
    random.RandomState()
    return random.randint(1,high=die,size=num)

try:
	from termcolor import colored,cprint
	print_green = lambda x: cprint(x,'green',attrs=['bold'])
	print_red = lambda x: cprint(x,'red',attrs=['bold'])
	print_blue = lambda x: cprint(x,'blue',attrs=['bold'])
	print_white = lambda x: cprint(x,'white',attrs=['bold'])
except ImportError:
	print_green = lambda x: print(x)
	print_red = lambda x: print(x)
	print_blue = lambda x: print(x)
	print_white = lambda x: print(x)

#(Credit: http://stackoverflow.com/a/20007730)
import math
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

def print_roll(args):
	rol = str(args.n)+'d'+str(args.dice)
	d = int(args.dice)
	mod = int(args.m)
	myroll = roll(d,int(args.n))
	i = 0
	for r in myroll:
		i += 1
		if r == d:
			print_green("You rolled a crit! "+ str(r))
		elif r == 1:
			print_red("Critical Miss! "+ str(r))
		else:
			print_white(str(ordinal(i))+" throw is a "+ str(r))
	
	if mod:
		print_blue("Total for " + rol + " with modifier of " + str(mod) + ":")
		print_green(sum(myroll)+mod)
	else:
		print_blue("Total for " + rol + ":")
		print_green(sum(myroll))


try:
	parser = argparse.ArgumentParser()
	parser.add_argument("dice", nargs='?')
	parser.add_argument("-n", help="number of dice to roll", type=str, default=1)
	parser.add_argument("-m", help="modifier to add to total",type=str, default=0)
	args = parser.parse_args()

	if args.dice is None:
		args.dice = '20'

	print_roll(args)

except:
	e = sys.exc_info()[0]
