# House

Python Essentials Project Portfolio - Code Institute

View deployed site [here.](https://l3wk3m.github.io/house/)

 *House* is a command-line interface program whose main goal is to deliver the experience of a psychological horro themed text-based adventure game. The user if taken straight to the Main Menu where they get to choose to begin the game or not. Upon receiving the user's input, the application will launch into it's main game loop. Subsequently, the user is provided with their current game-state and prompted with two options of which path they would like to take next. The user will ultimately arrive at 1 of 4 different endings.

![Responsive Mockup](documentation/)

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

## Design

- **Imagery:**
  xxx
- **Colour Scheme:**
  xxx <br>

- **Typography:**
  xxx

### Flowcharts

<details>
<summary> xxx </summary>
<br>

![Flowchart](documentation/)

</details>

## Features

### Existing Features

The ASCII Art "invalid escape sequence" fix: [Adam Johnson](https://adamj.eu/tech/2022/11/04/why-does-python-deprecationwarning-invalid-escape-sequence/)


<details>
<summary> Screenshot x </summary>
<br>

![Screenshot](documentation/)
</details>

### Features, which I would like to implement in the future

- 

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [Excalidraw](https://excalidraw.com/) was used to create the Flowchart.
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) to beautify the code
- [LanguageTool](https://languagetool.org/) was used to check the grammar and spelling in the README and the Code. 
- [Colorama](https://pypi.org/project/colorama/)was used to color the text in the terminal.
- [Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) was used to convert jpg images into wepb images.
- [Tinypng](https://tinypng.com/) was used to compress the webp background-image.

## Testing

1. **Validator Testing**

- **[CI Python Linter](https://pep8ci.herokuapp.com/#)**

  - result for run.py<br>
 . 
    ![result for run.py]()<br>
   

2. **Lighthouse Test** <br>
   To measure the website against performance, accessibility, SEO and best practice, I used [Lighthouse](url).<br>
   - result for index.html<br>
  . 
   ![Lighthouse]()

3. **Manual testing** <br>
To ensure the pages are responsive, I used the Google Chrome developer tools.

| **Test** | **Test Description** | **Expected Outcome** | **Result**|
|:---|:---|:---|:---|
| What happens if a value other than 1 or 2 is passed as an option? | When prompted for option 1 or 2 - a string of letters was input. | The user would be prompted to try a suitable value. | The while loop reprinted the message "Please choose 1 or 2 and hit return" infinitely to the console. A second input prompt was added to the while loop that validated the code (line 198 at time of writing) to give the user another chance to input the correct format of choice. |
|:---|:---|:---|:---|
| Will the try/except block manage to raise the OSError properly if the story.py file is missing? | This repo was cloned and deployed to a version of VS Code local to my machine where I then locally deleted the story.py file from the repo |The except block would throw an OSError, giving specific more specific details of the I/O problem and would exit the function|:---|
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

    [Screenshot of the terminal receiving an "n" input and starting the game anyway]()

      given that I also ran into this problem when calling the restart() method, I will describe how I fixed the problem wherein:

  2. The game restarted from the .restart() method even if it received the input "no" or "n":

    [Screenshot of the terminal receiving an "n" input and starting the game anyway]()

    The fix for both of the above bugs was the same, instead of the if statement being phrased 'if begin_game == "yes" or "y"', it needed to be written 'if begin_game == "yes" or begin_game == "y"'. The same fix needed to be applied to the "no"/"n" inputs for the main_menu and restart methods:

    [Screenshot of the terminal receiving an "n" input and exiting the game]()

    Without the if statement written like this, the input would take any value and run anyway:

    [Screenshot of the start game prompt taking the value of "2" and running regardless]()

  3. The player_char variable was not declared in the correct scope and so attempts to call methods against it failed:

    [Screenshot of an attempt to call player_char.take_key() failing]()

    This was solved by instead declaring player_char in the scope of the main '.play()' method, the scope in which methods would be passed against it.

    [Screenshot of the Player class working as intended when passed methods]()

  4. Although it wasn't picked up by the linter, my original ASCII art generated on [fsymbols](https://fsymbols.com/generators/carty/) seemed to be breaking pep8 standards:

   ![Screenshot of ASCII art spilling over the side of the terminal](/house/assets/images/ascii_art_error.webp)



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

- The background image is from 
- 

### Code

- My data structure for calling my story elements and taking inputs from the user works as follows:

- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [mdn](https://developer.mozilla.org/en-US/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [DevDocs](https://devdocs.io/)
  - [Stack Overflow](https://stackoverflow.com/)
  - Slack Community

### Media

- 

### ReadMe

- Thank you to

### Acknowledgments

- I would like to thank my wonderful mentor Ronan McLeland for his great assistance during the creation of this project and for help structuring this ReadMe.
- Thank you to Kate ____ for giving me the format for testing for my ReadMe.

**This is for educational use.**
