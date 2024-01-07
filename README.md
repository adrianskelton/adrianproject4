# Family Recipes
<img src="media/mockup.png" ><br>
- [Live Site](https://comingsoon.herokuapp.com/)
- [GitHub Repo](https://github.com/adrianskelton/repo)

Family Recipe is a recipe sharing website where users can upload and share recipes as well as reading others, I thought about this as I have a family recipe book from South Africa and I think it would be great to have a website where family members could share their family recipes with eachother and the world. 
I also wanted a rating system based on the ammount of like and a comment section for recipes. 
<br>

## Table of contents


## Overview
lorumipsum

## UX
Five Planes Of Website Design:<br>
### 1. Strategy<hr>

To create a website with good UI and UX 

- Project Setup
  - Create 

- UX
  - Favicon logo

- Navigation
  - lorumipsum

- CRUD
  - lorumipsum
- Authentication
  - lorumipsum
- Validation
  - lorumipsum
- Administration
  - lorumipsum
- Deployment
  - lorumipsum
- Testing
  - lorumipsum
- Documentation
  - lorumipsum

<br>

**Agile Methodology**<br><br>
I used Agile methodology.<br>
I used [GitHub](https://github.com/) for all the user stories and epics. As the user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress**, **Done** and **Not Implemented** lists.
The board can be viewed [here](https://github.com/users/adrianskelton/projects/5/).

**Kanban Board**<br><br>
<img src="media/kanban.png"><br><br>

<details>
<summary>Sprint 1: Base Setup</summary>

|EPIC|User Story|Description|
|:--|:--|:--|
|Project Setup|Project setup|As a developer, I need to set up the project so that it is ready for implementing the core features.|

</details><br>

<details>
<summary>Sprint 2: Navigation & Account Creation</summary>

|EPIC|User Story|Description|
|:--|:--|:--|
|**Project Setup**|||
|Navigation|Navbar|As a developer I need to create a navbar so that users can navigate the site.|

</details><br>

<details>
<summary>Sprint 3: Styling</summary>

|EPIC|User Story|Description|
|:--|:--|:--|
|CRUD|Create a recipe|As a logged in user I create a recipe.|

</details><br>

<details>
<summary>Sprint 4: CRUD</summary>

|EPIC|User Story|Description|
|:--|:--|:--|
|CRUD|Delete recipe|As a logged in user I can delete a recipe.|

</details><br>

<details>
<summary>Sprint 5: Search & Email</summary>

|EPIC|User Story|Description|
|:--|:--|:--|
|Administration|Admin search|As an admin I can filter and search the recipes so that I can find more relevant recipes easily.|

</details><br>

<details>
<summary>Sprint 6: Testing & Documentation</summary>

|EPIC|User Story|Description|
|:--|:--|:--|
|Testing|Unit Tests|As a developer I need to use testing so that I an sure my code is free of bugs and will not result in site errors.|

</details><br>

### 2. Scope<hr>
**Simple and Intuitive UX**<br>
- Create a website that makes people want to share and read recipes.


**Relevant Content**<br>
- Make all the content easily accessible


**Responsiveness**<br>
- Create a responsive website that works on every device and screen size.<br><br>

### 3. Structure<hr>
The website is designed with the user in mind and has the pages listed below:
- Landing page
  - Recipes
  - Login
- Account Home

There are also 2 pages available to users who are signed in:
- Submit Recipes
- Login


#### Navigation

The navbar is bootstrap .
All users will see:
- lorum ipsum

A user who isn't signed in will see:
- lorum ipsum

<img src="media/navbar_guest.png" alt=""><br>

A user who is signed in will see:
- My Account
- Logout

<img src="media/signed-in-navbar.png" alt=""><br>

Hamburger menu image.<br>
<img src="media/hamburger-menu.gif" alt=""><br>

Hover effect of links.<br>
<img src="media/nav-hover.gif" alt=""><br>

#### Footer

The footer is the same across all the pages and includes:
- Social Media Icons (Facebook, Instagram, Github)
- A copyright statement

Link hover effect to show the link is active.<br>
<img src="media/footer-hover.gif" alt="Video of the footer" width="100%"><br>

#### Pages

##### Landing Page

The landing page is divided into 4 sections:
- Hero Image  Logo
- Recipe section


##### Sign Up Page

<img src="media/.png" alt="" width="60%"><br>

This page uses the allauth template as a base with custom design added.
The username and password fields are mandatory but the email is optional. If the user signs up with and includes and email address they will be sent email updates on:
- lorum ipsum


##### Sign In Page

<img src="media/log-in-page.png" alt="e" width="60%"><br>

This page 

##### Account Home Page

<img src="media/account-home.png" alt="Image of the account home page"><br>

This page shows the users recipes.
On a large screen it is divided into 2 sections:
- lorum ipsum




lorum

##### Admin Account Home Page
<img src="media/search-recipes.png" alt="Image of the admin search panel" width="60%"><br>
The account home page for an Admin user has the addition of a Search recipes panel giving the admin user the ability to search by:
- Date of recipe
- Username

If the number of recipes exceeds 25 the page paginates.<br>

##### Submit Recipte

The Submit recipe has 6 inputs:
- A name of the recipe
- The country of origin
- Description
- Cooking instructions
- Ingredients list

The form has built in validation to alert the user if:
- There are fields missing

Once a recipe has been successfully added the user is taken back to the user account page and a message saying "recipe saved" will dissapear after 5 seconds.<br>

<img src="media/recipe.gif" alt=""><br>


User's View<br>
<img src="media/user.png" alt="Image of" width="70%"><br>
Admin's View<br>
<img src="media/admin.png" alt="Image " width="70%"><br>

##### Update Recipe

If the user clicks on the edit recipe button recipe detail page they are then taken to the recipe selected to edit and save again.
Once a recipe has been successfully edited the user is taken back to the user account page and a message saying "recipe saved" will dissapear after 5 seconds.<br>

##### Confirm Delete Recipe Page
<img src="media/confirm-delete-recipe.png" alt="" width="60%"><br>
If the user clicks on the 'Delete Recipe' they will be asked if they are sure they want to delete it.

#### Sitemap
The project flowcharts for the site structure was created using [LucidChart](https://www.lucidchart.com/).
<details>
<summary>Sitemap:</summary>
<img src="media/sitemap.png"><br>
</details>

### 4. Skeleton<hr>
**Wireframes**

The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed <details>
<summary>Here:</summary>
Homepage<br>
<img src="media/homepage-wireframe.png"><br>
Login/Logout pages<br>
<img src="media/login-logout-wireframe.png"><br>
Submit recipe<br>
<img src="media/submit-recipe-wireframe.png"><br>
</details><br>

**Database**
The project uses ElephantSQL as PostgreSQL relational database for storing the data.
<details>
  <summary>Model</summary>
  <img src="media/database-schema.png"><br>
</details><br>

### 5. Surface<hr>

#### Color Scheme and Fonts

- The fonts used for this site were imported from [Google Fonts](https://fonts.google.com/):
  - Josefin for the headings
  - Crimson for the body

<img src="media/fonts.png" width="60%">

- The colors used were based on the the colors in the logo.
  - #color1
  - #color2
  - #color3

<img src="media/color-palette2.png" width="60%">

#### Visual Effects

**Hover effects**<br>
NavBar<br>
<img src="media/nav-hover.gif" width="100%"><br>
Footer<br>
<img src="media/footer-hover.gif" width="100%"><br>


**Logo**<br>
Logo with effect when hovered<br>
<img src="media/interactive-logo.gif" width="40%"><br>

## Features

### Existing Features

#### Recipe Modal
lorum ipsum

##### Recipe List
Each recipe is displayed on a card on the account home page and contains:
lorumipsum

##### Update Recipe Page
lorumipsum

##### Confirm Delete Recipe Page
lorumipsum

##### Admin Search Panel
lorumipsum

##### Update Email
lorumipsum

##### Change Password
Users can change their password from the account panel in the account home page.

### Potential Future Features
- Allow admin users to edit the services from the account home rather than from the django backend panel


## Responsive Layout and Design
The bootstrap grid system and flexbox was used to create a fully responsive layout and testing on multiple screen sizes and devices was carried out to make sure it each page looks good in many settings.

**Tested devices:**

- iPhone 13


## Tools Used

- [GitHub](https://github.com/) for hosting 



### Python packages

- [Django](https://www.djangoproject.com/) used as the framework 


A full list of the requirements and the versions used can be found in the requirements.txt file. To install them and run them on your own machine first setup a virtual environment with the command to create a venv... <br>
`python3 -m venv venv` <br>
Then this command to run it... <br>
`source venv/bin/activate` <br>
To stop running the environment simply type the command... <br>
`deactivate`

To create the requirements.txt file I ran the following command:<br>
`pip3 freeze > requirements.txt`

## Testing

Tests  [TESTING.md](TESTING.md).

## Bugs

- lorumipsum

## Deployment

### ElephantSQL


### Cloudinary


### Heroku

    
### Fork the repository


### Clone the repository

- lorumipsum

## Credits

To style the forms I watched the following tutorials
- [Style Django Forms With Bootstrap - Django Blog #5](https://www.youtube.com/watch?v=6-XXvUENY_8&ab_channel=Codemy.com)
- [Tip for changing logo based on screen size](https://stackoverflow.com/questions/34984737/display-a-different-logo-on-mobile-and-desktop)

### Content
asdfasdf

### Media
logo [Casdfaa](https://asdfasdafgb/).

### Code

- Django's :
  - [asdfe](asdfasdfa)
  - [sf](asdasdf.html)



## Acknowledgements

- lorumipsum