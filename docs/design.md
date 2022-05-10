# Project Design
**Team Name**:  Will Code for Lamont Popsicles
**Team Members**: Katelyn Diaz and Kira Seshaiah

## Sprint Planning
### Prototype I
* write a list of tasks / features
* other

- Create the baseline code where it checks if the entry was correct by cycling through the word, and then marks which letter were correct and which were wrong 


### Prototype II
* write a list of tasks / features
* other

- Fully functional with almost all the graphics
- Prints letters of the word that it corresponds where the graphics are located
- Has start screen, game screen, end screen
 

### Prototype III
_Note: We recommend completing your project, in its entirety, by Prototype III. Then using the extra time to fix bugs that you find during demo day and incorporate other ideas._
* write a list of tasks / features
* other..should basically be done.

- Has full dictionary with randomization code to generate a random word when the user starts the game
- Second end screen added for graphics, and graphics are fully done
- Make the game look pretty


## User Personas

1. Mia, a prospective student not wanting to go on a college tour
   - From Colorado, too far away to visit
   - High school senior, learning more about colleges and the application process
   - Wants to learn whats beyond the admissions website
     - Smith Wordle has been curated by actual students, not admins at Smith
2. Claudia, a 60-year old woman who went to Smith and wants to relive her past
  - Walk down memory lane
  - Plays with old friends made at Smith
  - Donates to the school every year and wants to see what new traditions have been formed, or any updates on buildings and current student opinions
3. Pablo, a father of a incoming student and wants to learn more about the college to know what he's paying for and to bond with his daughter
  - Thinks the school is too expensive
  - daughter loves the school, but financial aid package was lacking. Is it worth it?
  - Wants to be a part of the college conversation with his daughter and is not willing to go on an admissions tour
  - Wants to find the issues and convince daughter not to go. 
   
## Project Structure 

_Insert the structure of how components are connected._

This can be found in the `Design Documents` folder under `CSC 111 Final Project Flowcharts` and an updated and more accurate version can be found in `IMG_6024.jpg`.

## Project Rubric

_Insert project rubric._

A rubric for how you think your project should be graded in terms of both implemented features and good coding/design practices

Implemented features:
- The text box on the game screen where you type in a word. It was a difficult feature to figure out as it has to be in a while loop to work, and it needed a "trigger" of sorts to work and pause the game at different points so there is time for the player to see what is appearing on the screen
- Creating a dictionary in terms of a csv file, turning it into a usable dictonary within python using the distributer.py file, and then calling both the key and value (word and fact in this case) throughout the program to make the game run. Another aspect of the dictionary is formatting the fact to make it print within the box on the end game screen if the word is correct
- Coordinating the graphics to if the letter is correct within the six boxes that turn green or white and corresponding the correctness of the letters with x's and o's when the word is printed below the text gox on the game screen

Coding/design practices:
- Good at creating new files to hold code to import into the main file
- Keeping values in variable form or using the variables within the code after defining its value to make it easier to follow the code and know where values come from while on the coding side, making it easier to update values when coding
- Grouping the same code together within main to make it easier to find where graphics are printed, for example
- Adding comments to lines of code to make it easier to follow and explain to someone who didn't code the project