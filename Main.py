#This is a List of song names to be selected at random. They are in script form because this is just a placeholder.
sadSongs = ["Tahalamot - Tinariwen ", "Toumast anlet - Tamikrest ", "Nanuflay - Tinariwen "]

madSongs = [ "Karambani - Terakraft ", "Kamelemba - Oumou Sangare ", "Tahigren - Bombino "]

gladSongs = ["Ahabib - Terakraft ", "Bamako - Songhoy Blues", "Awa Adounia - Terakraft "]

#This is a List of images to be selected at random. It is also just a placeholder.
north = ["Nubian architecture in Aswan, Egypt", "Ait Ben Haloud in Morocco", "Berber architecture in Mzab Algeria"]
west = ["Palace of the Emir of Kano, Nigeria", "Great Mosque of Djenné in Mali ", "Palace of the Emir of Dutse in Kaduna, Nigeria ", "Emir of Zazzau's palace in Kaduna, Nigeria"]

#This asks the user to type either "sad," "mad," or "glad." This influences which song the user might get. 
print("Feeling sad, mad, or glad?")
feeling = input()
#This asks the user which direction they're going which can influence which image they get.
print("Are you going West or North?")
direction = input()

#This displays the mood and direction the user has typed in. 
print("Since you're feeling " + feeling + ", and going " + direction + ",")

import random
#The user will recieve a random combination of a song name and image name based on their input.
if feeling == "sad":
  songChoice = random.choice(sadSongs)

if feeling == "mad":
  songChoice = random.choice(madSongs)

if feeling == "glad":
  songChoice = random.choice(gladSongs)

if direction == "North":
  imageChoice = random.choice(north)

if direction == "West":
  imageChoice = random.choice(west)

#This prints the random song and image names to the terminal just to make sure the code is working. 
print("The song and image pair is: " + songChoice + "and " + imageChoice)