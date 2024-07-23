# Izzit? Dictionary 
Is it? /'izzit/ - is a responsive phrase, frequently used in conversation meaning 'Is that so?' or 'Really?'.

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
Build the database of slang words commonly used by South Africans to increase communication, conncetion and understanding with this subset of people.

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
* edit words they added to correct possible mistakes or add updates
* delete words they added


## Design choices


### Fonts


### Colours
![colour scheme]()

### Styling


### Backgrounds
The design choice of one solid background colour was made to maintain accessibility for the user. Solid colours were used to make the content stand out.
 
### Content
The Nav bar consists of a logo which is also a link to the main page. There is a drop down browse option which allows users to view words and definitons, by selecting a letter to group the words or browsing the whole dictionary. Or the user may type specific words in the search bar to pull up desired word. If the user is not logged in, there will be a log in button next to the search bar. If the user is logged on, they will have the option to add a new word and definition or view their already added words, which they can edit and delete.

## Wireframes
Designed in balsamiq, there are 3 wireframes for each page. Providing planned layout and views on large screens, medium screens and small screens.



# 2. Features

## Existing Features
When not logged in
* Navigation: Nav bar consists of a logo which is also a link to the main page. There is a drop down browse option which gives the user the option to browse words by selecting a letter, all the words that start with the selected letter will be pulled for the user to view. Below this there is a search bar where the user may search more spefically. If the user is not logged in, there will be a log in button next to the search bar. If the user is logged on, they will have the option to add a new word and definition or view their already added words, which they can edit and delete.

* Registration: Potential users can register their account by providing a unique username and password which is at least 5 characters long. In case of username being already used (input field is not case sensitive) message is displayed. If the password is too short, the user is informed about the minimum length.

* Logging in: User can log in. If username/password are incorrect/don't exsist the user receives a message explaining this.

* Browse: view words and definitons, by selecting a letter to group the words or browsing the whole dictionary. 

* Search: type specific words in the search to pull up desired word/s.

* When logged in: users can addtional, add, edit and delete their own words.

* Log out: log out option is located in the nav bar.


## Left to Implement
* Admin approval before word added by user is published on site. 

# 3. Technology Used
* Languages: HTML, CSS, JavaScript, Python
* Frameworks: Flask, materalise?
* Database: MongoDB
Websites
realfavicongenerator - generate a favicon
Am I Responsive - used to create the mock-up image showing the site
Google Chrome Developer Tools - Used to test the responsiveness of the site
Font Awesome - Used to source icons
Canva - Used to create wireframes and logo
Pixabay - Used to source hero image
Wikipedia - Used to source book cover pictures and book synopsis description
Github - GitHub for versionn control for the development of application up to deployment
Gitpod -An online IDE used to build and develop the website
Heroku- The cloud platform used to host the deployed site
Slack - Used during development and testing to find the solutions for the encountered problems
Stack Overflow - Used to search for the answers to encountered problems
Code Institute - Used to review concepts covered in preceding modules and walk-through projects
RandomKeyGen - Used to generate the Secret Key
W3C CSS Validation Service - Used to validate the CSS code
W3C HTML Validation Service - Used to validate the HTML code
Pep8CI - Used to check the run.py file for PEP8 compliance
ElephantSQL - PostgreSQL database hosting service




# 4. Testing
Testing is done to verify that the software behaves as expected and meets the specified requirements. There are two types of testing, both are undertaken in this project: Manual testing involves human testers executing test cases for verification, while Automation testing involves the use of automation tools to execute tests. Jest is an example of such tools.
## Results
### Manual Testing

### Automation test


## Validation Tests


## Lighthouse Testing


## Bug Problems

# 5. Deployment
Project Creation
CI MongoDB Full Template to create this project:

Click on 'Use this template' and select 'Create a new repository'
Enter your chosen repo name
Click 'Create Repository'
From the new GitHub repo copy the the page URL
Open Code Anywhere and navigate to the 'workspaces' page
Click on 'New Workspace'
Paste the GitHub repo URL in to the 'Repository URL' box
Click 'Create'
Deployment to Heroku
I used Heroku to deploy this project.

To deploy to Heroku:

In Code Anywhere CLI from the main directory run pip3 freeze > requirements.txt to create/update a requirements.txt file containing project dependencies.
In Code Anywhere CLI from the main directory run echo web: python app.py > Procfile to create a Procfile. Check that the file contains the text 'web: python app.py' and delete any blank lines at the bottom.
Push the 2 new files to the GitHub repository
Login to Heroku, select 'Create New App', create a unique name for the app and select your nearest region. Click 'Create App'
Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository by name and click 'connect'.
Navigate to 'settings', click reveal config vars and input the the following:
Key	Value
CLOUD_API_KEY	Cloudinary API key
CLOUD_API_SECRET	Cloudinary API secret
CLOUD_NAME	Cloudinary Name
IP	0.0.0.0
PORT	5000
MONGO_DB	Mongodb Database Name
MONGO_URI	mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.tfci8tb.mongodb.net/<DATABASE>?retryWrites=true&w=majority
SECRET_KEY	Secret Key From env.py required for 'Session' & 'Flash' functions of Flask
Go back to the Deploy tab and click on 'Enable Automatic Deploys'
Click deploy branch
Once build is complete click on 'View' to launch the new app
Local Development
NB: This project will not run locally with database connections unless hte user sets up an env.py file configuring the above environment variables as these are not included in the GitHub files for security reasons.

To Run Locally:

Navigate to the GitHub Repository
Click on 'Code' & select 'Download Zip' to download the files locally and open with an IDE or Copy the URL from the top box
If copying the code open your development editor & in the terminal use the 'Git Clone' command followed by the above URL to create a clone of the project locally.
To Fork Project:

Navigate to the GitHub Repository
Click on the 'Fork' button at the top right of the page
This will duplicate the project for you to work on

## How work on the project code within a local IDE
To clone this project from Github:
1. Follow this link to the Project Github respository; [here](https://github.com/RHuebsch13/)
2. Under respository name; select 'clone or download'
3. Copy the clone URL fro the repository.
4. In your IDE open the terminl.
5. Change the working directory to the location where you want the cloned directory to be made
6. Type git clone and your URL from step 3 

# 6. Credits
## Code


## Content


## Media 

