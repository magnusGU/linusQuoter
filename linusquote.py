#!/usr/bin/python3

import random

lines = open("quotes").readlines()
linee  = random.choice(lines)[:-1:]
print (linee)

