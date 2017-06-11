#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from sys import exit
from os import path

# PyInstaller needs to find the resource files
# in its temp folder.
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
def res_path(rel_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = path.abspath(".")
	return path.join(base_path, rel_path)

file = res_path("thetext.txt")

thetext = open(file, "r")
# Put all the file in an array, one item per line
verses = thetext.readlines()
thetext.close()

thenow = date.today()
# Making sure today's date is in the format we need
theend = date(thenow.year,thenow.month,thenow.day)
# Converting the 1st day of the year to the format we need
theone = date(thenow.year,1,1)
# The subtraction gives hours:mins:secs too,
# we want only the days part
theday = (theend - theone).days

if (theday < 0) or (theday > 366):
    exit("Something went wrong with the calculations. Sorry.")

# 1st day is line 0, so we subtract one
print("%d. %s") % (theday, verses[theday-1])