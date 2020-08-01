#!/usr/bin/python
from os import listdir
from os.path import isfile, join
import random
import os

p = "ascii"
p = "sfw_ascii"
files = [f for f in listdir(p) if isfile(join(p, f))]

print files

while True:
  os.system("date | figlet -f big > /dev/ttyUSB0")
  f = random.choice(files)
  cmd = "cat " + p + "/" + f + " > /dev/ttyUSB0"
  #print(cmd)
  os.system(cmd)
  #sleep(1)

