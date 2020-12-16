[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3684859&assignment_repo_type=AssignmentRepo)

Project Overview
The big project was going to include a button for the user to click on in a website so they will get a random pairing of a song playing and a displayed image. The little piece I managed to perform was a program that asked the user how they were feeling, which direction they are are going and if they were “prepared for their travel” and based on their answers, they may get a random pairing of a song name and location along with a description of an object that is given for the user for travel. 

Project Narrative
To reach Milestone 1, I made two lists, one with song names and another with image names. Then used random.choice to have the program print a random combination of a song and image. For Milestone 2, I divided the song names into three lists, “sad”, “glad”, and “mad.” As for the image names, they have been divided into lists named “North” and “South.” The user would be asked about their mood and which direction they’re going, the result in song and image depends on their answers. 

The concepts from the lessons that were useful for this project were how to make lists and if statements. I had to look elsewhere for information on how to use the random.choice method. 
What surprised me was that I had to type “def main():” in order for the return statements within the if statements to work properly. 

If I were to approach this project again, I would use the if statements and lists to make a story based educational game instead of this song name and location pairing. Perhaps something that would feel like a tour of a place through text. 

Corrections
Your comment on my first milestone called for more complexity by requesting user input. I added user input by dividing the songs and images into different categories and adding the input function on lines 14 and 16 which ask "Feeling sad, mad, or glad?" and “Are you going West or North?" If the user inputs the string “sad” for example, the program will print a song name from the sad list. If the user inputs “North” to answer the directions question, the program will print an image name from the North list. 

For the second milestone, you mentioned receiving an error after inputting an emotion which states that it is undefined and suggested using the string function for the inputs. I addressed this by adding the string function to lines 54 and 56 to the variables feeling, direction,songChoice, and imageChoice. In lines 20, 23, 26, 29, and 41, the if statements detect if a specific input has been entered. I made two versions of each word, one that is capitalized and the other not capitalized so the program would detect the input as true whether it is capitalized or not. 

You also suggested that I add something to the direction entry so I added another input request under the random.choice functions for the North and West variables which asks if the user is ready for their travel and if they answer "no", the program gives them an item along with a brief description.  

