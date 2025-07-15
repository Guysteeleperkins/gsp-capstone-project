# GSP Capstone Project

## Documentation to be completed!!

[Streamlit App](https://gspgarmindatasetexplorer.streamlit.app/)

## Introduction 

A Streamlit ETL project using the data obtained from a CSV file that was obtained from my personal Garmin account to test, improve and gain knowledge in technologies such as Python, Pandas and Streamlit. Along with some data extraction, transformation and loading with some data analysis.

Live site:

<hr>

## Table of Contents

- [GSP Capstone Project](#gsp-capstone-project)
  - [Documentation to be completed!!](#documentation-to-be-completed)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Website Goals](#website-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
  - [Sprints](#sprints)
    - [User Stories](#user-stories)
  - [Must Haves](#must-haves)
  - [Should Haves](#should-haves)
  - [Could Haves](#could-haves)
  - [Won't Haves](#wont-haves)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
    - [Security](#security)
- [Features](#features)
  - [User View](#user-view)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
- [Libraries and Frameworks](#libraries-and-frameworks)
  - [Tools and Programs EDIT](#tools-and-programs-edit)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validators](#validators)
    - [Python](#python)
- [Credits](#credits)
  - [Code](#code)
    - [README](#readme)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Overview



# UX - User Experience

## Design Inspiration


### Colour Scheme


# Project Planning

## Strategy Plane


### Website Goals



## Agile Methodologies - Project Management

Garmin Explorer was my third project to implement Agile. With some experience in using Agile in a group hackathon during my time at codeinstitute along with MojoYoga my capstone project for the same bootcamp I knew it would be useful to keep on track and progress. I used pen and paper for user stories and this helped keep motivation up as I could "See" the progress being made as I moved items from "To Do" to "In Progress" to "Complete". I also underwent sprints to finish certain parts of my project - which was fantastic for time management.

### MoSCoW Prioritization 

I used the MoSCoW Prioritization method for MojoYoga:

- **Must Have**: These are the non-negotiable, essential requirements that are critical to the success of the project. Without them, the project cannot be considered complete or successful.

- **Should Have**: These are important but not critical requirements. They add significant value but can be delayed if necessary, as long as they are delivered in the near future.

- **Could Have**: These are nice-to-have features or tasks that would enhance the product but are not vital for its core functionality. If time or resources are tight, these can be omitted without major consequences.

- **Won't Have**: These are requirements that are agreed upon as out of scope for the current project cycle. They may be reconsidered in the future but will not be addressed in the current iteration.

## Sprints
EDIT THIS EVENTUALLY
I had 9 working days to complete this project and had learned from previous projects that sprints worked effectively. Depending on the day and energy levels I would split larger tasks with things like testing and styling as I went to mix up my work to keep motivation high. I found that after the first 3 days I had comnpleted CRUD functionality and changed my spints to regular work periods with a conistent 5-10 minute break every 1-2 hours. This kept me working effeciently and productively.

### User Stories


| Epic                                                 | User Requirements                                                                         |
|------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Epic 1: Data Availability, Quality and Trust         | Analysts need a single, clean dataset combining transaction and demographic data.         |
|                                                      | Data scientists need the cleaned dataset stored in a SQL table for analysis.              |
| Epic 2: Customer Insights                            | Analysts want to analyze spending per customer and identify high-value customers.         |
|                                                      | Business stakeholders would like to identify customers who have spent more than **$500**. |
| Epic 3: Demographic Trends                           | Business stakeholders want insights into age and country trends of key customers.         |
| Epic 4: Data Access and Storage                      | Scientists need assurance that the data is clean, consistent, and accurate.               |
|                                                      | Scientists need the cleaned dataset stored in a SQL table for analysis.                   |
|                                                      | Scientists need to be able to reset and update the data for repeat or future analysis     |

## Must Haves

| **User Story**                                                                                                                                                     | **Acceptance Criteria**                                                                                                                                                                                                                                                                              | **Priority**  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **Data Engineer**, I must be able to **set up the project and environments** so that I can **create a clean and managable working environment**.                                | - I can follow the set up guide and successfully set up the project and environments, alsop documenting the set up so it can be replicated                                    | **MUST HAVE** |



## Should Haves


## Could Haves



## Won't Haves


## Scope Plane

Main features:
- A calming and inviting website that fulfils user needs
- Responsive website for users on all devieces
- User Authentication
- User Profile creation and editing
- Leave a review feature with full CRUD functionality

Due to a lot of new content that had been covered in the course just a few weeks before this project began I wanted to make sure that I didn't overreach and set my goals too high. Due to the new technologies such as Python, Django, Databases and Cloudinary that I had covered recently and were still new to me, I took this project as a learning objective as well as building a fully functional app. 

## Structural Plane

Having had a website to base mine off this was a very easy step. I already had a good basis of what works regarding to where items would be positioned and how they would fit into each other to create a smooth experience for the user. I wanted to keep things simple and as I completed tasks it would free up time to add some of the "Could have" features.

NavBar - Having had some difficulties with this before I knew how to start it straight away. Bootstrap provides an easy to use NavBar which is easily manipulated with custom CSS. In prevous projects had a experiemented with different kinds of buttons within the navbar but the simple text with some button hightlights when hovering always looked the best in my opinion - best not to over complicate it!

Hero Image - As well as the website I was using for inspirations and some previous projects that met the criteria for passing a large hero image that spanned over the whole website on all pages really stuck out as a nice feature and it kept consistency throughout. 

Reviews / Review Details / Forms - Also inspired from another project that was shown to our cohort I loved the background colour of black with the opacity set to 0.5 to let the hero image show through but to create an obvious division between the background and the cards. This was kept consistent throughout the website and looks very smart.


### Security 

**AllAuth**  

Django AllAuth is an installable framework that takes care of the user registration and authentication process. Authentication was needed to determine when a user was registered or unregistered and it controlled what content was accessible on MojoYoga. The setup of AllAuth included:

- installing it to my workspace dependencies
- adding it to my INSTALLED_APPS in my settings.py
- sourcing the AUTHENTICATION_BACKENDS from the AllAuth docs for my settings.py
- adding its URL to my projects 'urls.py'
- run database migrations to create the tables needed for AllAuth

**CSRF Tokens**
Cross-Site Request Forgery tokens are included in every form to help authenticate the request with the server when the form is submitted. Without CSRF the site can be vunerable to attackers manipulation and theft of users data.

# Features

## User View

It is important for MojoYoga to accessible for un registered users, anyone must be able to see the content and see other peoples reviews to help the user decide on whether they would like to go on a retreat. Non-registered users would be prompted to create an account if they clicked on "leave a review" in the navbar and would only be able to leave one if signed in. Only users who created a review can edit and delete their review.

Users also recieve a message depenant on their action. Logging in, Signing up, creating a review, editing a review and deleting a review give a small message after using the features of the site. 


## Feature Showcase


## Future Features

Due to time constraints I could not impliment some of my "Could Haves" from my [Github Projects Board](https://github.com/Guysteeleperkins/mojoyoga/projects). 

These include:
  - Review Likes/Dislike
  - Booking Page
  - User Profile
  - Review Comments
  - Retreat booking integration
  - Multilingual Support
  - Search and filter Reviews

These features I believe are within my capabilties to complete, therefore after my project has been reviewed and tested I will be impliementing these in my own time. I very much look forward to adding more custom models to test my knowledge and increase my experience.


# Technologies & Languages Used 

  - [Git](https://git-scm.com/) used for version control.
  - [Github](https://www.github.com) used for online storage of codebase and Projects tool.

# Libraries and Frameworks


## Tools and Programs EDIT

 - [CodeInstitute](<https://learn.codeinstitute.net/dashboard>) - Using walkthrough projects and lessons
 - [ChatGPT](<https://chatgpt.com/>) - To assist with learning and debugging
 - [GitHub](<https://github.com/>) _ Project board and linking with Herko
 - [Heroku](<https://dashboard.heroku.com/apps>) - Hosting this full-stack project
 - Balsamiq Wireframes - App to create wireframes
 - [Google](<https://www.google.com/>) - To assist with learning and debugging

 
 # Testing

 ## Manual Testing

 ## Validators

 During the testing phase I had very few valiation errors, usually it was some trailing tags in the HTML and missing whitespace for Python.

 ### Python

 
# Credits

## Code

The following complemented my learning for this project.

 - [Code Institute's](https://codeinstitute.net/ie/) Learning Content.
 - [Django Docs](https://www.djangoproject.com/)
 - [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
 - [Code Institute's](https://github.com/Code-Institute-Org>) Blog walkthrough

### README

 - [Github](<https://github.com/amylour/FreeFido_v2/blob/main/README.md?plain=1>) - Amy Lour's FreeFido Project README was used as a basis for this README

## Media

All the media used in this website was sourced from my Mum (Joanna Steele-Perkins) which was also used on her website which this was based off
[MojoYogaMorocco](<https://www.mojoyogamorocco.com/>)


## Acknowledgements

  - Huge thankyou to my Mum who gave me the permission to base my project off her website and use photos she has taken over the years
  - Many thanks to all my friends who helped during testing and pointed out any bugs
  - Thank you to my mentor Alex and everyone in my cohort at CodeInstitute for always being helpful and supportive
  - Thanks to my housemates for providing me with coffee and snacks throughout the most stressfull times of the course