#!/usr/bin/env python
import dice
from termcolor import colored,cprint

import argparse
import sys
print_green = lambda x: cprint(x,'green',attrs=['bold'])
print_red = lambda x: cprint(x,'red',attrs=['bold'])
print_blue = lambda x: cprint(x,'blue',attrs=['bold'])
print_white = lambda x: cprint(x,'white',attrs=['bold'])

import math
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])


def print_roll(args):
	roll = str(args.n)+'d'+str(args.dice)
	d = int(args.dice)
	mod = int(args.m)
	myroll = dice.roll(roll)
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
		print_blue("Total for " + roll + " with modifier of " + str(mod) + ":")
		print_green(sum(myroll)+mod)
	else:
		print_blue("Total for " + roll + ":")
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
