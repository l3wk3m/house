# House

Python Essentials Project Portfolio - Code Institute

View deployed site [here.](https://house-l3wk3m-f39fc8b11770.herokuapp.com//)

 *House* is a command-line interface program whose main goal is to deliver the experience of a psychological horror themed text-based adventure game. The user if taken straight to the Main Menu where they get to choose to begin the game or not. Upon receiving the user's input, the application will launch into it's main game loop. Subsequently, the user is provided with their current game-state and prompted with two options of which path they would like to take next. The user will ultimately arrive at 1 of 4 different endings. The story was strongly influenced by the famous psychological thriller novel House of Leaves by Mark Z. Danielewski.

## Table of contents

- [User Experience (UX)](#user-experience)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

### User stories

-  *House* is a psychological horror text-based adventure.
- As a user, I want to play *House* to experience a thrill.
- As a user, I want to find the game easy to interact with and to follow along.
- As a user, I want to finish the experience curious about the multiple possible endings I could discover.

## Design

### Data Model

Each feature is described in more depth in the **Features** section later in the ReadMe

#### Classes
There are two classes defined and initialised. One is House(), the class of the game itself. The other is the class of Player(). The Player() is defined in this Object Oriented Programming Paradigm and defined by their attribute of whether or not they possess a key.

#### Dictionaries
The story and all the choices are stored in a dictionary data structure in story.py. Using this model, it is easy to iterate through the key/value pairs to move from story node to story node, beginning at the "start" node.

#### Functions / Methods
These are defined to be called in readable, reusable ways.

#### Input Validation
The main_menu(), restart(), and play() methods all have a form of input validation. As main_menu() and restart() only take values of "y", "yes", "n", and "no", all other inputs are caught in the else part of the if/else blocks that validate them.

After checking for win conditions or if the Player has acquired the key needed for ending 3, the play() method then does input validation to make sure it is being passed a value of either "1" or "2". Any other inputs will restart that particular while loop and request the input "1" or "2" before continuing


#### UI
- **Imagery:**
  The ASCII art used to display the game's main menu was generated using [fsymbols](https://fsymbols.com/generators/carty/)
- **Colour Scheme:**
  I used the colorama library to colour the terminal text differently for when Will is talking and when Mr. Navidson is talking. This will help the user to distinguish different dialogue sources.
  
  In the coloured print of the novel that inspired this story, the word "house" is printed in blue every place it occurs in the text, giving an eerie and unsettling experience. I wanted to emulate this motif in my game, even in cases where the word house appears in character dialogue. I used the colorama library to colour the text for this effect. <br>

- **Typography:**
  Outside of the ASCII art display of the game's title and the manipulation of the colour of the text in the terminal, standardised typography is used throughout this deployment's UX.

### Flowcharts

<details>
<summary> Photos of my early game path flowcharts are pictured below. These helped guide the design of the game and how each of the endings would resolve. </summary>
<br>

![Flowchart](/assets/images/flowchart.webp)

</details>

## Features

### Existing Features

- The game deploys from run.py, calling the main_menu() method.

- The title of the game is displayed for the user in ASCII art and they're asked if they want to play the game

- A while loop is called within main_menu, validating whether or not the program receives the inputs of "no", "n", "yes" or "y". Any other input returns an error and the user is prompted for another input.

- If the user selects "no" or "n", they are told to select "y" or "yes" when they are ready.

- When the user selects "yes", the play() method is called. This is the main function running the gameplay loop.

- The play() method pulls story information and options from a separate file called story.py which is imported at the top of the project. This file stores all of the story information and the story paths in many dictionary data structures within one master dictionary data structure. The beauty of desgining the game around this is it is then very easy to write the code to call the key/value pairs back from the story.py file. Starting at the "start" key, you iterate through choices using a while loop by reading the text, passing your choice of option 1 or option 2 to the program. The choice you make is used to update the key of the text node you are on with this line - "current_node = options[f"option_{choice}"]", updating the story node you're on from "start" to whatever next node in the path you've chosen. Once updated, the while loop repeats, this time calling the text from the new story node you are on, subsequently offering you the two options from that story node. The play() method also looks out for the key "ending", which signal that the player has reached a game ending, triggering text telling them which ending they've gotten and giving the option to restart the game using the restart() method. The play() method also looks out for the "key" key, which I will explain now.

- The Player() class is initialised above the main House() class to create the 'object' of the player. This player has one attribute - 'has_key', either evaluated to True or False. This is because one of the endings, ending 3, the "true" ending, requires that the player acquire a key from Mr. Navidson during the interrogation section before going back to the house. If the player acquired the key, which will update this has_key property to True, when they reach the door out the front of the house, they can use the key they've acquired to unlock the door and escape. If they do not have the key at this stage, they instead get ending 4, perishing in the house. This inclusion of OOP (Object Oriented Programming) Paradigms was important to me for this project as I liked the idea of using this structure to 'describe the world'.

- The restart() method is called when the game reaches any of it's end states. If the user chooses to restart, the main_menu() method passes and the game begins again. If they do not they are thanked for playing and the game exits.

### Features, which I would like to implement in the future

- I would like to update the code block that evaluates the choice made when the user is given either option 1 or option 2 to choose from. I would define a function for this purpose that could be flexibly called within the House() class to this end. I currently don't have the time to implement this feature.

- There is also a variable I've declared called 'escape' that takes a boolean value. I would like to update the code block in the play() method to instead call a function that runs a check if escape passes as true or not. If it does, the user can get ending 3, the 'true ending', escaping the house. The logic of this is already present in the game but in future I would like to use this variable within an external method to more eloquently handly this process.

- I would like to get the try/except block that checks for I/O errors working.

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [Excalidraw](https://excalidraw.com/) was used to create the Flowchart.
- [Code Beautifier](https://codebeautify.org/python-formatter-beautifier) to beautify the code.
- [Colorama](https://pypi.org/project/colorama/)was used to color the text in the terminal.
- [Pixelied](https://pixelied.com/convert/png-converter/png-to-webp) was used to convert png images into wepb images.
- [Tinypng](https://tinypng.com/) was used to compress the webp background-image.

## Testing

1. **Validator Testing**

- **[CI Python Linter](https://pep8ci.herokuapp.com/#)**

  - result for run.py<br>
 . 
    ![result for run.py](/assets/images/linter.webp)<br>
   

2. **Lighthouse Test** <br>
   To measure the website against performance, accessibility, SEO and best practice, I used **Lighthouse**<br>
   - Result for deployed heroku page<br>
  . 
   ![Lighthouse](/assets/images/lighthouse.webp)

3. **Manual testing** <br>
To ensure the pages are responsive, I used the Google Chrome developer tools.

| **Test** | **Test Description** | **Expected Outcome** | **Result**|
|:---|:---|:---|:---|
| What happens if a value other than 1 or 2 is passed as an option? | When prompted for option 1 or 2 - a string of letters was input. | The user would be prompted to try a suitable value. | The while loop reprinted the message "Please choose 1 or 2 and hit return" infinitely to the console. A second input prompt was added to the while loop that validated the code (line 198 at time of writing) to give the user another chance to input the correct format of choice. |
|:---|:---|:---|:---|
| Will the try/except block manage to raise the OSError properly if the story.py file is missing? | This repo was cloned and deployed to a version of VS Code local to my machine where I then locally deleted the story.py file from the repo |The except block would throw an OSError, giving specific more specific details of the I/O problem and would exit the function| Instead of raising the OSError I was hoping for, I got Traceback (most recent call last): File "/Users/admin/Desktop/house/run.py", line 4, in <module>, from story import story_text, ModuleNotFoundError: No module named 'story'
Unfortunately it is too late to try and get this try/except validator to work |
|:---|:---|:---|:---|
| What will happen if a value other than "yes" or "no" is passed when the start game prompt is given? | I ran the program via the Heroku deployment and, when prompted as to whether I wanted to start the game or not, I enterred a number instead and hit return. | The 'else' clause of the code will return "{begin_game} is not a valid choice. Please enter 'y' or 'n' and try again.". | The program executed regardless. Something in the 'if' statement was found to be faulty - addressed in the **Bugs** section |
|:---|:---|:---|:---|
| What will happen if a value other than "yes" or "no" is passed when the restart game prompt is given? | I ran the program via the Heroku deployment and, when prompted as to whether I wanted to restart the game or not, I enterred a number instead and hit return. | The 'else' clause of the code will return "Invalid input. Please type 'Y' or 'N' and hit return". | The program executed regardless. Something in the 'if' statement was found to be faulty - addressed in the **Bugs** section |




4. **Browser Compatibility**<br>
  The tests were conducted using the following browsers:

- Google Chrome Version 120.0.6099.129
- Safari on Mac Version 17.0 (17616.1.27.111.22, 17616) 
- Safari on AndroidOS 14.2
- Edge Version 120.0.2210.61

5. **Bugs**

- The following bugs were uncovered throughout the deployment process:

  1. The game deployed even if the it received the input "no" or "n" when asked to start:

    ![Screenshot of the terminal receiving an "n" input and starting the game anyway](/assets/images/start_game_n_prompt_error.webp)

    given that I also ran into this problem when calling the restart() method, I will describe how I fixed the problem wherein:

  2. The game restarted from the .restart() method even if it received the input "no" or "n":

    ![Screenshot of the terminal receiving an "n" input and starting the game anyway](/assets/images/end_game_prompt_error.webp)

    The fix for both of the above bugs was the same, instead of the if statement being phrased 'if begin_game == "yes" or "y"', it needed to be written 'if begin_game == "yes" or begin_game == "y"'. The same fix needed to be applied to the "no"/"n" inputs for the main_menu and restart methods:

    ![Screenshot of the terminal receiving an "n" input and exiting the game](/assets/images/end_game_prompt_solution.webp)

    Without the if statement written like this, the input would take any value and run anyway:

    ![Screenshot of the start game prompt taking the value of "1" and running regardless](/assets/images/no_validator_error.webp)

  3. The player_char variable was not declared in the correct scope and so attempts to call methods against it failed:

    ![Screenshot of an attempt to call player_char.take_key() failing](/assets/images/take_key_not_working.webp)

    This was solved by instead declaring player_char in the scope of the main '.play()' method, the scope in which methods would be passed against it.

    ![Screenshot of the Player class working as intended when passed methods](/assets/images/take_key_not_working_fix.webp)

  4. Although it wasn't picked up by the linter, my original ASCII art generated on [fsymbols](https://fsymbols.com/generators/carty/) seemed to be breaking pep8 standards:

   ![Screenshot of ASCII art spilling over the side of the terminal](/assets/images/ascii_art_error.webp)



## Deployment

This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:
1. Log in (or sign up) to Heroku.
2. Navigate to the Heroku Dashboard and select 'Create New App'.
3. I then named my deployment house_l3wk3m.
4. Select your region. I'm in Europe so I chose Europe.
5. Click 'Create App'.
6. On the next page, click on the 'Settings' tab.
7. Head to the 'Config Vars' section. In the box for 'KEY' enter PORT and in the box for 'VALUE' enter 8000.
8. Scroll down to the 'Add Buildpack' sectoin and click 'Add Buildpack'. Click on the 'PYTHON' buildpack and click 'Save Changes', then click 'Add Buildpack' again and select 'NODEJS'. Make sure you select these two in this order.
9. Now head down to the deployment section and, under the 'Deployment Method' heading, click 'Connect to Github'.
10. Once connected, click in the search box and search for the 'house' repo (you will need to have cloned the 'House' repo from my github if you are deploying this yourself - in order to do this, please see the 'Cloning This Repository' guide below)
11. Choose either 'Automatic Deploys' or 'Manual Deploys' in order to deploy your project. I chose Automatic for the purposes of testing, but if you're just deploying the app to use it yourself, you can select 'Manual Deploy'.
12. You will see the app being built in the 'Build Master' terminal below the deploy options once you've deployed.
13. When you've seen its done, you will see an 'App successfully deployed' message, with a link to click through to view your project.


- Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*l3wk3m/house*](https://github.com/l3wk3m/house)
3. Click at the top of the repository on the **Fork** button on the right side

- Clone this repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*l3wk3m/house*](https://github.com/l3wk3m/house)
3. In the top right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

## Credits

### Content

- The inspiration for the story was taken from Mark Z. Danielewski's novel 'House of Leaves'
- The content of the story is my own

### Code

- My data structure for calling my story elements and taking inputs from the user using a dictionary structure was suggested by my mentor. The exact format of this was inspired by the story.py file written by [GayatriG19](https://github.com/gayatrig19)
in her project [The Quest](https://github.com/gayatrig19/the-quest-adventures-game/) which I took and implemented in my own way, adding different story, endings and possibilities, like the discovering of a key.

- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [mdn](https://developer.mozilla.org/en-US/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [CodeHS](https://codehs.com/)
  - [Stack Overflow](https://stackoverflow.com/)
  - Slack Community

### Media

- See also: ['House of Leaves' by Mark Z. Danielewski](https://www.amazon.co.uk/House-Leaves-Mark-Z-Danielewski/dp/038560310X/ref=sr_1_1?crid=2WC1THX7CFVV0&dib=eyJ2IjoiMSJ9.rpTtExF5nzhsztBGGQUAIfJZ8Shqs6UAE05vkTwddGPK1utsHBSiIEhQ_XieTJVhK_nfAZ8-UbY9O7KCftW6e2hBfODJ32YKazVd1ZJlUJpgpXoa_nYlOvdi3L4ONk0P5E_H2FD-Hb0m-rYwXuYxvblDXKMCmauoNx5elnsBq50VSoTTLQ_s-ilEoGdBfQyhscQjvCpVMU2bA96EWgvHTOkxWqxn0dY1z3kAgtvYz1E.FUgVOaHFTps19LBt1jB9IB2hB8fTLtfz-juLbWO_-ik&dib_tag=se&keywords=house+of+leaves+mark+z.+danielewski&qid=1709172932&sprefix=house+of+lea%2Caps%2C65&sr=8-1)

### ReadMe

- Thank you to [Queenisabaer](https://github.com/queenisabaer/) from who's ReadMe this structure format was taken
- Thank you to Kate_5P on the Code Institute Slack channel for giving me the format for the testing section of my ReadMe.

### Acknowledgments

- I would like to thank my wonderful mentor Ronan McLeland for his great assistance during the creation of this project and for help structuring this ReadMe.
- Thank you to my Code Institute cohort facilitator Laura Mayock, who has been wonderfully supportive throughout this process.

**This is for educational use.**
