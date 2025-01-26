from os import system as sys
import os
from random import randint as rand

def clear(): 
	sys('clear')

clear()
playerage = 5
month = 1
day = 1
playermorale = 10
playername = input("What is your name?\n")
playerintellegence = 0
playerexp = 1
schoolboost=False
schoolboosttimer=None
clear()
statlist = {"NAME":playername, "AGE":playerage, "MORALE":playermorale, "MONTH":month, "DAY":day, "INTELLEGENCE":playerintellegence, "EXP":playerexp, "School Boost":schoolboost}

def stats():
	global day, month, playerage
	print(f"AGE: {playerage} | MONTH: {month} | DAY: {day}\n")

def main():
	global day, month, playerage, schoolboost, schoolboosttimer

	if schoolboosttimer and schoolboosttimer > 0:
		schoolboosttimer -= 1
	elif schoolboosttimer and schoolboosttimer <= 0:
		schoolboost = False
		schoolboosttimer = None
	
	random = rand(1, 100)
	if day > 29:
		day = 1
		month += 1
	if month > 11:
		playerage += 1
		month = 1
		day = 1
	stats()
	if playerage < 23:
		choice = input("Do you:\n1. Go to school\n2. Stay Home\n3. See all stats\n")
		clear()
		if statlist["School Boost"] == True:
			random += 10

		#Go to school
		if choice == "1":
			if random < 80 and random > 20:
				print("You went to school. +1 INTEL")
				statlist["INTELLEGENCE"] += 1
			elif random < 20:
				print("You struggled in school today. -1 INTEL, -1 MORALE")
				statlist["INTELLEGENCE"] -= 1
				statlist["MORALE"] -= 1
			elif random > 80:
				print("You excelled in school today. +2 INTEL, +1 MORALE")
				statlist["INTELLEGENCE"] += 2
				statlist["MORALE"] += 1

		#Stay Home
		elif choice == "2":
			clear()
			stats()
			choicea = input("You decide to stay home. Do you:\n1. Housework\n2. Study\n3. Hobby\n")
			if choicea == "1":
				clear()
				stats()
				randoma = rand(1,2)
				statlist["EXP"] += randoma
				print(f"You decide to spend the day doing housework. +{randoma} EXP")
			elif choicea == "2":
				clear()
				stats()
				randoma = rand(1,4)
				if randoma == 1:
					print("You found a very helpful rescource. +1 INTEL, SCHOOL BOOST ACTIVATED")
					statlist["INTELLEGENCE"] += 1
					schoolboost = True
					schoolboosttimer=5
				elif randoma < 4 and randoma > 1:
					print("You studied. +1 INTEL, -1 MORALE, +1 EXP")
					statlist["INTELLEGENCE"] += 1
					statlist["MORALE"] -= 1
					statlist["EXP"] += 1
				else:
					print("You tried to study, but got distracted. Nothing Changed.")



		#View Stats
		elif choice == "3":
			clear()
			print("ORDER: Name, Age, Morale, Month, Day, Intellegence, EXP")
			statsee = input("Which stat do you wish to see?")
			clear()
			print(f"{statsee.upper()} is:")
			print(statlist[statsee.upper()])
			input("Press enter to continue.")
			clear()
			main()
		elif choice == "":
			main()
	input("Press enter to continue.")
	day += 1
	clear()
	main()

main()
