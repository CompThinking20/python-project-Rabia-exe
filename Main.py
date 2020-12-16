def main():
#This is a List of song names to be selected at random. They are in script form because this is just a placeholder.
  sadSongs = ["Tahalamot - Tinariwen ", "Toumast anlet - Tamikrest ", "Nanuflay - Tinariwen "]

  madSongs = [ "Karambani - Terakraft ", "Kamelemba - Oumou Sangare ", "Tahigren - Bombino "]

  gladSongs = ["Ahabib - Terakraft ", "Bamako - Songhoy Blues", "Awa Adounia - Terakraft "]

  #This is a List of images to be selected at random. It is also just a placeholder.
  north = ["Nubian architecture in Aswan, Egypt", "Ait Ben Haloud in Morocco", "Berber architecture in Mzab Algeria"]
  west = ["Palace of the Emir of Kano, Nigeria", "Great Mosque of Djenné in Mali ", "Palace of the Emir of Dutse in Kaduna, Nigeria ", "Emir of Zazzau's palace in Kaduna, Nigeria"]

  #This asks the user to type either "sad," "mad," or "glad." This influences which song the user might get. 
  feeling = input("Feeling sad, mad, or glad? ")
  #This asks the user which direction they're going which can influence which image they get.
  direction = input("Are you going West or North? ")

  import random
  #The user will recieve a random combination of a song name and image name based on their input.
  if feeling == "sad" or feeling == "Sad":
    songChoice = random.choice(sadSongs)

  if feeling == "mad" or feeling == "Mad":
    songChoice = random.choice(madSongs)

  if feeling == "glad" or feeling == "Glad":
    songChoice = random.choice(gladSongs)

  if direction == "North" or direction == "north":
    imageChoice = random.choice(north)
    #If the user answers no to the question, the song and image is given, otherwise, the program ends here.
    print("Are you prepared for your travel?")
    prepareNorth = input()
    if prepareNorth == "no" or prepareNorth == "No":
      print("Take this scimitar with you!")
      print("A scimitar is a sword with a curved blade.")
    else:
      print("Watch out for the carnivorous camels!")
      return

  if direction == "West" or direction == "west":
    imageChoice = random.choice(west)
    #If the user answers no to the question, the song and image is given, otherwise, the program ends here.
    print("Are you prepared for your travel?")
    prepareWest = input()
    if prepareWest == "no" or prepareWest == "No":
      print("Take this pirogue with you!")
      print("A pirogue is a fishing boat that will help you sail down the river.")
    else:
      print("You drowned in the river!")
      return

  #This displays the mood and direction the user has typed in. 
  print("Since you're feeling " + str(feeling) + ", and going " + str(direction) + ",")
  #This prints the random song and image names to the terminal just to make sure the code is working. 
  print("The song and location are: " + str(songChoice) + "and " + str(imageChoice))

main()