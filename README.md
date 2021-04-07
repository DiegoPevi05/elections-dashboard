# Peru Elections 2021
#### Video Demo:  https://youtu.be/Vr7HUJLGUaE
#### Description: This is a landing page where you can find information about the elections of 2021, see some statistics and simulate a voting situation, that is going to happen on Peru the 11th of April.

#### Aplication.py
> This section is based on the logic of the landing page, here I import some library to use for the Log in, Log out and Register templates.
> Also here I add to the database the information that i extract from the users register and the user answer of the survey that have participated.
> One of the greatest thing that i learn is that i can stablsih some values for the session and re-use it later for complete information of the survey as an example.

#### Index.html
> In this section you will find information of the candidates, sanctions for no voting, and some more information about the elections of Peru in 2021. Is made it with a carousel of images, containers and tables.

#### Candidates.html
> This page show the information of the candidates with their summary of their goverment plans, and some personal information.
> In this page i use some containers and division of class row for the information of the partys and candidates, one the biggest benefits of this pages is that al the informations is store in the database and is interatively extracted wih a fo. It was a challenge of concatenate string variables of python with text to define id, that are going to be referenced with the logos of the partys.
> So there is no need to repeat the insertion of every text and image reducing the space of text.

#### Statistics.html

> This page show some statistics of the Elections by a private poll and the national goverment institution in charge of the elections, also show the personal survey of our databse and the results by president and congress.
> In this page i use some containers for the information and class row, the best part was to insert the graphics of bars and lines that i use from and abroad library call charts.js so the information allocated in the databses are put into the graphics that are showwn.
> This graphic library is based on javascript so i have to convert the information of dictionarys in arrays of unique values to be interpretative for the graphic syntax.

#### answered.html
> Here is a template where you can find a message that is loaded when you already finish the survey. It is allowed to only fill one survey per user.

#### survey.html
> Here is a tempalte of the simulation of voting in ensemble with stles.css and survey.js it dynamically responds to the user make it freandly and correct.

#### styles.css
> This one of the most complicated task for me beacuse i have to learn how to do interactive webpage with css, some colors, orders, animations and values that a i have to add as classes to the objects of my html page, was a huge task for me to understand how does it works everything together in ensemble with javascript.

#### survey.js
> It was really interesting to learn to do interactive values, i have a challenge to pass javascript variables to the application.py with the protocol of getjson(), the information was store in the database but when i tried to render a templated give me error because it was requested by and http page and it has to be https so a quick way to solve it, was to pass the variables as input fields in html and requested as form values from the application.py for me was  huge challenge to solve this i learn a lot about protocols.
> Another big use that i discover was to create empty classes to separate types of input objects and dynamically get a response of every class and store the data.

#### Elections.db
> Here is the database where all information of users, candidates, answers of the survey are store and are loaded every time you check a template at the website.




