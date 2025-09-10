print("Welcome to the manga reader recommender!")
print("Answer a few questions to find your next read")

Genre = input(" What is your favorite genre? (action, horror, romance):")
Duration = input(" How long should the manga be? (short, medium, long):")
Time = input("Which decade? (2000s, 2010s):")

if Genre == 'action' and Duration == 'short' and Time == '2000':
	print("Manga i recommended for this is 'Death Note' ")
elif Genre == 'action' and Duration == 'short' and Time == '2010':
	print("Manga i recommended for this is 'I Got a Cheat Ability in a Different World, and Became Extraordinary Even in the Real World' ")
elif Genre == 'action' and Duration == 'medium' and Time == '2000':
	print("Manga i recommended for this is 'Blue Exorcist' ")
elif Genre == 'action' and Duration == 'medium' and Time == '2010':
	print("Manga i recommended for this is 'The Eminence in Shadow' ")
elif Genre == 'action' and Duration == 'long' and Time == '2000':
	print("Manga i recommended for this is 'Bleach' ")
elif Genre == 'action' and Duration == 'long' and Time == '2010':
	print("Manga i recommended for this is 'Chainsaw Man' ")


if Genre == 'romance' and Duration == 'short' and Time == '2000':
	print("Manga i recommended for this is 'Masamune-kun's Revenge' ")
elif Genre == 'romance' and Duration == 'short' and Time == '2010':
	print("Manga i recommended for this is 'Tomo-chan Is a Girl!' ")
elif Genre == 'romance' and Duration == 'medium' and Time == '2000':
	print("Manga i recommended for this is 'Sankarea: Undying Love' ")
elif Genre == 'romance' and Duration == 'medium' and Time == '2010':
	print("Manga i recommended for this is 'My Dress-Up Darling' ")
elif Genre == 'romance' and Duration == 'long' and Time == '2000':
	print("Manga i recommended for this is 'Highschool DxD' ")
elif Genre == 'romance' and Duration == 'long' and Time == '2010':
	print("Manga i recommended for this is 'Kaguya-sama: Love Is War' ")


if Genre == 'horror' and Duration == 'short' and Time == '2000':
	print("Manga i recommended for this is 'Highschool of the Dead' ")
elif Genre == 'horror' and Duration == 'short' and Time == '2010':
	print("Manga i recommended for this is 'Gannibal' ")
elif Genre == 'horror' and Duration == 'medium' and Time == '2000':
	print("Manga i recommended for this is 'Sankarea: Undying Love' ")
elif Genre == 'horror' and Duration == 'medium' and Time == '2010':
	print("Manga i recommended for this is 'Mieruko-chan' ")
elif Genre == 'horror' and Duration == 'long' and Time == '2000':
	print("Manga i recommended for this is 'Higanjima' ")
elif Genre == 'horror' and Duration == 'long' and Time == '2010':
	print("Manga i recommended for this is 'Tokyo Ghoul/:re' ")


else:
	print("Invalid genre. I only provide (action, romance, horror)")
