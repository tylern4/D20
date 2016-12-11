---
layout: post
title: The Final Countdown
modified: 2016-01-29
tags: [Code,Linux,OSX]
share: true
---

#D20 

A Simple dice roller for playing dnd.

## Use
To roll a d20
* `d20`
* Critical hits give:

You rolled a crit! 20
Total for 1d20:
20

* Critical misses give:

Critical Miss! 1
Total for 1d20:
1

### Mupltiple rolls, Differet dice, Modifers
To roll say 6 d8 with a +4 modifer:

* `d20 -d 8 -n 6 -m 4`

### Can also roll with advantage or disadvantage
To roll two and get the higher of the two rolls:

* `d20 -A`

Or the lower of the rolls:

* `d20 -D`

## TODO
* Make requirements.txt for pip
* Make my own dice roller and check if it's fair
