# Izzit? Dictionary 
Is it? /'izzit/ - is a responsive phrase, frequently used in conversation meaning 'Is that so?' or 'Really?'.

As a South African living in Wales, I often get puzzled looks when I use some of my South Africanisms. For this reason, I took the opportunity to create this dictionary. Whether you’re a homesick South African, like me or someone curious about new jargon, I hope you find it both helpful and entertaining. Enjoy!

![The Site](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/responsive.png?raw=true)

# Table of Contents

1. [UX](#ux)
   - [Project goals](#project-goals)
   - [User Goals](#user-goals)
   - [User Stories](#user-stories)
   - [Design choices](#design-choices)
2. [Features](#features)
3. [Technology Used](#technology-used)
4. [Testing](#testing)
   - [Results](#results)
   - [Manual Testing](#manual-testing)
   - [Automation test](#automation-test)
   - [Validation Tests](#validation-tests)
   - [Lighthouse Testing](#lighthouse-testing)
   - [Bug Problems](#bug-problems)
5. [Deployment](#deployment)
6. [Credits](#credits)

# 1. UX
## Project goals
Build the database of slang words commonly used by South Africans to increase communication, connection and understanding with this subset of people.


## User Goals
This project aims to assist user in:
* Understanding local conversations: Decode slang used in everyday South African conversations, social media, and local media.
* Imporve cultural integration: Integrate better into South African people groups.
* Travel and tourism: Navigate interactions with locals more effectively when traveling within South Africa.
* Entertainment and media consumption: Better enjoy South African music, films, and literature by understanding the slang used and engage more deeply with South African pop culture and media.
* Building social connections: Build stronger relationships with South African friends, family, or partners by speaking their slang.

## User Stories
### As a User I would like to:
* search for specific words in the dictionary
* browse words alphabetically
* add, edit and delete words and definitions
* log in to manage my words added the dictionary

### Developer goals
Allow users to easily:
* register to the website
* log in to the website
* navigate through the site
* add words and definitions they want to share with others
* edit words they've added, to correct possible mistakes or add updates
* delete words they've added


## Design choices
Clean, simple styling was used, with minimal images to give a clutter free visual while maintaining accessibility for the site. Design draws subtle lines to South African themes. Examples of this would be the use of the South African flag as the favicon and the colour scheme is after the South African national flower; the Protea.

### Fonts
Fonts are simple and easy to read.

### Colours
![colour scheme](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/colors.jpg?raw=true)

### Styling
Site sturcture and layout aims at explicitness. Making the users access to the jargon and terms unhindered, there are no tricky protocols and learning can begin instantly. Icons used are familar to most users so discerning each's use should not be difficult.

### Backgrounds
The design choice of one solid background colour was made to maintain accessibility for the user. Solid colours were used to make the content stand out.
 
### Content
The Nav bar consists of a logo which is also a link to the main page. There is a drop down browse option which allows users to view words and definitons, by selecting a letter to group the words or browsing the whole dictionary. Or the user may type specific words in the search bar to pull up desired word. If the user is not logged in, there will be a log in button next to the search bar. If the user is logged on, they will have the option to add a new word and definition or view their already added words, which they can edit and delete.

## Wireframes
Designed in balsamiq, there are 3 wireframes for each page. Providing planned layout and views on large screens, medium screens and small screens.
![Big Screens](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/Bscreen.png?raw=true)
![Medium Screens](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/Mscreen.png?raw=true)
![Small Screens](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/Sscreen.png?raw=true)

# 2. Features

## Existing Features
When not logged in
* Navigation: Nav bar consists of a logo which is also a link to the main page. There is a drop down browse option which gives the user the option to browse words by selecting a letter, all the words that start with the selected letter will be pulled for the user to view. Below this there is a search bar where the user may search more spefically. If the user is not logged in, there will be a log in button next to the search bar. If the user is logged on, they will have the option to add a new word and definition or view their already added words, which they can edit and delete.

* Registration: Potential users can register their account by providing a unique username and password which is at least 5 characters long. In case of username being already used (input field is not case sensitive) message is displayed. If the password is too short, the user is informed about the minimum length.

* Logging in: User can log in. If username/password are incorrect/don't exsist the user receives a message explaining this.

* Browse: view words and definitons, by selecting a letter to group the words or browsing the whole dictionary. 

* Search: type specific words in the search to pull up desired word/s.

When logged in: 
* Users may still navigate through the various search options and view terms as when not logged in.

* Users can only add new terms and edit/delete their own additions while logged in.

* Log out: log out option is located in the nav bar.


## Left to Implement
* Admin approval before a word added by user is published on site. 

# 3. Technology Used
* Languages: HTML, CSS, JavaScript, Python
* Frameworks: Flask, Bootstrap
* Database: MongoDB
* WireFrames: Balsalmiq
* Favicon: Realfavicongenerator 
* Mock-up image of site: Am I Responsive 
* Responsiveness of the site: Google Chrome Developer Tools - Used to test the 
* Icons: Font Awesome
* Logo: Canva 
* Version Control: Github 
* IDE : codeinstitute-ide
* deployment: Heroku
* Trouble shooting: Slack, tutor support.
* Secret Key: RandomKeyGen 
* Validation: W3C Validation Services (CSS and HTML), Pep8CI(Python), jshint(Javascript)


# 4. Testing
Testing is done to verify that the software behaves as expected and meets the specified requirements. There are two types of testing, both are undertaken in this project: Manual testing involves human testers executing test cases for verification, while Automation testing involves the use of automation tools to execute tests. Jest is an example of such tools.
## Results
### Manual Testing
## CREATE

**Objective**: Verify that users can create new terms and definitions and that input fields adhere to validation rules.

**Fields to Test**:
- **Term**: Required, can be any length
- **Definition**: Required, should be at least 50 characters long

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Create a new term with various special characters and lengths. | New term created and displayed in the list. | Passed |
| Create a new term without filling in the term field. | Form does not submit. Request to fill the field pops up. | Passed |
| Create a new term without filling in the definition field. | Form does not submit. Request to fill the field pops up. | Passed |
| Create a new term with valid inputs, and verify that the new term appears in the list. | New term appears in the list. | Passed |

## READ

**Objective**: Ensure that terms and definitions are displayed correctly and are sortable/filterable as expected.

| Test | Expected Outcome | Result |
|------|------------------|--------|
| View terms on the homepage while logged in. | All terms are shown with edit and delete options for terms added by the logged-in user. | Passed |
| View terms on the homepage while not logged in. | All terms are shown with no edit and delete options. | Passed |

## UPDATE

**Objective**: Confirm that users can update terms and definitions, and that updates are reflected correctly.

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Edit a term without filling in the term field. | Form does not submit. Request to fill the field pops up. | Passed |
| Edit a term without filling in the definition field. | Form does not submit. Request to fill the field pops up. | Passed |
| Edit a term with a definition having fewer than 50 characters. | Form does not submit. Request to use at least 50 characters pops up. | Passed |
| Update a term and verify the updated information is displayed. | Updated term information is shown on the list and detail page. | Passed |
| Try to update a term that was not created by the logged-in user. | Form does not submit or shows an error message. | Passed |

## DELETE

**Objective**: Ensure that users can delete terms and that terms are removed from the list as expected.

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Delete a term created by the logged-in user. | Term is deleted and a confirmation message is displayed. | Passed |
| Attempt to delete a term created by another user. | Form does not submit or shows an error message. | Passed |

## LOGIN

**Objective**: Verify that the login functionality works as expected and provides access to appropriate features.

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Input existing username and correct password. | User is logged in.| Passed |
| Input username that does not exist. | Form does not submit. "Invalid Details" message pops up.| Passed |

## GUARDING FROM FORCED ACTIONS

**Objective**: Ensure that unauthorized actions are properly guarded and result in appropriate error messages.

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Force URL to add/edit/delete term while not logged in. | Redirected to main page. | Passed |

## NAVIGATION

**Objective**: Test the functionality of navigation links across the site.

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Click on the logo from any page. | Redirects to the homepage. | Passed |
| Click on the log in icon. | Redirects to log in and registration forms. | Passed |
| Click "Log out" button from any page (while logged in). | User gets logged out. "You have been logged out." message shows. | Passed |
| Click on back buttons. | Redirects to the homepage. | Passed |

### Automation test
Automation testing is a software testing process that uses specialized tools and scripts to automatically execute test cases, compare actual results with expected outcomes, and report discrepancies. An example of this software is jest. Only manual testing will be used for this development.

## Validation Tests
![Python](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/python_validation_updated.png?raw=true)

![Javascript](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/JS_validation.png?raw=true)

[View the PDF - CSS Validation](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/CSS_validation.pdf)

[View the PDF - HTML Validation](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/HTML_validation.pdf)

## Lighthouse Testing
[View the PDF - mobile](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/lighthouseDesktop.pdf)

[View the PDF - desktop](https://github.com/RHuebsch13/Izziy-Dictionary-/blob/main/docs/lighthouseMobile.pdf)

## Friends and Family 
* Noted that there was no back button after searching with the search bar and this made naviagtion a bit more difficult. Since, a back button was built.

## Bug Problems
1. Bugs in intial building:
* Connecting the mongoDB database was an issue. WIth help from tutor support, the error was corrected. The connection string being used initially was missing the database name. Incorrect connection string: mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.tfci8tb.mongodb.net/?retryWrites=true&w=majority. Correct connection string, including the database name: mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.tfci8tb.mongodb.net/<DATABASE>?retryWrites=true&w=majority
* Materialize not displaying cards in the way that was requred, switched to bootstrap, according to suggestions on slack.

2. After deployment:
* When the app was being run off Heroku, clicking on the following letters; A, E, G, H, I, L, M, N, P, R, S, V, W, X, Y, Z would cause a security error. Heroku logs were checked, the problem wasn't being cause by the deployment platform.The code was checked for any external APIs that could be causing the error. None were found as APIs not used. Therefore, the error was reported as an incorrect phishing warning and this seems to have corrected the problem. Tutor support assisted with this.

3. Issues picked up during testing:
* No back button after searching with the search bar, this was noted while in testing phase. A back button that returns the user to home page has been installed and is functional.
* Searching with the search bar and if no results were found, there was no message to communicate this to the user. A message has been installed that tells the user that "No results found".
* No cancel button when the edit/add term function is used. These have been added.
* If invalid details are entered when the user is loggin in, there is no message to explain why the log in failed. A message to notify the user has been added.

# 5. Deployment

#### CI MongoDB Full Template to create this project:
* Click on 'Use this template' and select 'Create a new repository'
* Enter your chosen repo name
* Click 'Create Repository'
* From the new GitHub repo copy the the page URL
* Open codeinstitute-ide and navigate to the 'workspaces' page
* Click on 'New Workspace'
* Select a Repository and paste/search the GitHub repo URL in to thebox
* Click 'Create'

#### How work on the project code within a local IDE:
To clone this project from Github:
1. Follow this link to the Project Github respository; [here](https://github.com/RHuebsch13/)
2. Under respository name; select 'clone or download'
3. Copy the clone URL fro the repository.
4. In your IDE open the terminl.
5. Change the working directory to the location where you want the cloned directory to be made
6. Type git clone and your URL from step 3 


#### Deployment to Heroku:
1. Set Up Your Local Environment
* Ensure git is installed. Check by running git --version in your terminal.
* Ensure Heroku CLI is installed. Check by running heroku --version in your terminal.

2. Prepare Your Flask Application
* Ensure your Flask application follows a standard structure.
* Create a virtual environment: python -m venv venv

3. Install necessary packages; Flask, Pymongo etc.
* Run pip3 freeze > requirements.txt to create/update a requirements.txt file containing project dependencies.
* Run echo web: python app.py > Procfile to create a Procfile. Check that the file contains the text 'web: python app.py' and delete any blank lines at the bottom.
* Push the 2 new files to the GitHub repository

4. On Heroku, log in:
* Select 'Create New App', create a unique name for the app and select your nearest region. 
* Click 'Create App'
* Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository by name and click 'connect'.
* Navigate to 'settings', click reveal config vars and input the the following: IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY.
* Go back to the Deploy tab and click on 'Enable Automatic Deploys'
* Click deploy branch
* Once build is complete click on 'Open app' to launch the new app

# 6. Credits
## Code
* Tim Nelson from Code institute's; Mini Project, Putting It All Together.
* W3schools - schemas: [here](https://www.w3schools.com/xml/schema_example.asp)
* W3schools - session.pop() use [here](https://www.w3schools.com/jsref/prop_win_sessionstorage.asp#gsc.tab=0)
* Stack Overflow - session.pop() [here](https://stackoverflow.com/questions/33952800/how-to-pop-a-second-value-in-session)
* Session management - [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
* Error handling - [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)
* Decorators - [here](https://flask.palletsprojects.com/en/3.0.x/patterns/viewdecorators/#view-decorators)
* User authenication - [here](https://flask-login.readthedocs.io/en/latest/#flask_login.login_required)
* Use of insert_one() - [here](https://pymongo.readthedocs.io/en/stable/operations.html#insert-operations) and [here](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html)
* Use of redirect - [here](https://www.geeksforgeeks.org/python-flask-redirect-and-errors/)
* Python functions - [here](https://docs.python.org/3/library/functions.html#str)
* Use of find.one() - [here](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one)
* Use of None - [here](https://docs.python.org/3/library/constants.html#None)
* Docstrings - [here](https://peps.python.org/pep-0257/)
* CRUD opperations - [here](https://www.mongodb.com/docs/manual/crud/)
* Tutor Support with database connection problem.
* Slack for general problem solving tips.

## Content
* List of South African slang words found at: [here](https://aforathlete.fandom.com/wiki/List_of_South_African_slang_words)

## Media 
* Logo created with Canva
* Picture used to create favicon: [here](https://www.istockphoto.com/vector/south-african-national-flag-official-flag-of-south-africa-accurate-colors-true-color-gm936590950-256225275)

## Design Inspiration
* [Urban Dictionary](www.urbandictionary.com)

