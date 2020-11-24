#This is a List of song names to be selected at random. They are in script form because this is just a placeholder.
songList = ["Ahabib - Terakraft ", "Awa Adounia - Terakraft ", "Tahalamot - Tinariwen ", "Toumast anlet - Tamikrest "]

#This is a List of images to be selected at random. It is also just a placeholder.
imageList = ["img_1", "img_2", "img_3", "img_4"]


import random
#This makes a random selection from the lists because the final project would have a button to click which would radomly pair an image with a song. 
songChoice = random.choice(songList)
imageChoice = random.choice(imageList)

#This prints the random song and image names to the terminal just to make sure the code is working. 
print("The song and image pair is: " + songChoice + "and " + imageChoice)