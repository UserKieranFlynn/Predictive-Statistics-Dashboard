## CA326 Testing & Design Refactoring.

**By Kieran Flynn & Eoin OBrien**

## Table Of Contents

- [1. Unit Testing](#1-unit-testing)

- [2. Error Handling](#2-error-handling)

- [3. Device Support](#3-device-support)

- [4. Accessibility](#4-accessibility)

- [5. Nielsen Heuristics](#5-nielsen-heuristics)
. 

## **1. Unit Testing**

Unit testing played a pivotal part in the development of the prediction system for the dashboard. This allowed us to ensure that we were getting correct probabilities of the ways one team can win, lose or draw a match at home or away. It allowed us to examine how the odds program was handling the probability matrix and ensure that the probabilities were consistent &amp; accurate for what opposition and location each team is presented with in said fixture.

Throughout the unit testing process we paid particular attention to the impact that changing the range of goals had on not only the probability of the outcome, but also how the matrix is generated. If you reduce the number of goals allowed in the game, then you can fluctuate the probability of a team winning, drawing or losing a match. As is the case with increasing the number of goals allowed. The more goals you allow to be scored, the more possibilities of a certain result are generated. We concluded that using 12 goals as a limit would be best as it is possible for a match to have a double figure scoreline, though very much rare. But it also means that potentially even high scoring games such as a 6:5 scoreline are also possible. In saying that, we also did not want to exceed 12 goals as the more possibilities that are required to be generated, the greater toll it takes on the efficiency of our program.

Unit testing also helped ensure the accuracy of our program. There are 20 teams in the league, with 3 of which being newly promoted teams that would not have played the other 17 teams in their previous season. This created a problem that we needed to solve. But thankfully, we had data for the previously promoted teams. We then decided to use the data that those 3 previous teams had to find an average of their probabilities &amp; use that for the basis of their probabilities. This meant that not only could the newly promoted teams be compared to the other 17 teams in the league, the promoted teams probabilities would be distinct from that of the previous promoted teams that their average is based off, for example Burnley.

Finally, unit testing allowed us to examine the differences in playing a match at home versus away. While a lot of teams are considerably more likely to win their home matches than their away matches, this does not necessarily extend to all teams in the league. Certain opposition can have impressive away form that significantly impacts the likelihood of the home side getting a positive result. By testing certain fixtures at both locations, we were able to determine how they would impact the the final result for each team in a given fixture.



## **2. Error Handling**

Error handling was performed in two ways throughout the application.

**Application-side input validation**

The first of these methods was a case of ensuring that anywhere the user inputs text that it&#39;s not empty or invalid data. For example when using the prediction tool if either of the &#39;team&#39; text boxes were empty an error message is returned to the user letting them know that they must enter two valid team names for the application to work as intended.

**Flask error handling**

<img src="/Code/Testing/testingPictures/test1.png" alt="test1"
	title="test1" width="400" height="300" />

The above is a code fragment from our main application. Simply put, should the user navigate to a page that doesn't exist / to an invalid route, they will be met with a custom 404 html page to let them know that something went wrong. From there they can choose to return to the previous page or navigate to a new page via the navbar.

The objective of this was to ensure that the user knows that something went wrong rather than something such as a database connection issue which they may not be aware of and can lead to a frustrating user experience.



## **3. Device Support**

In theory the application can be used by a wide range of devices as it is a web application. If it were to &#39;go live&#39;, the data needed would be hosted online therefore all that would be needed is an internet connection and a browser.

We tried to cater to this functionality by including specific html element sizings for different size screens.

As an example of this, see below.

<img src="/Code/Testing/testingPictures/test2.png" alt="test2"
	title="test2" width="300" height="50" />
 

This styling means that on an Extra large screen the element should take up 3 columns (of 12) where as on a medium screen it should take up 6. This dynamic shifting of the layout means that a wide range of users can use the application with minimal effort.









## **4. Accessibility**

There are a number of different issues and audiences that we had to consider when implementing and refining upon our interface design. The target demographic of sports fans is not exclusive to certain genders, age or disability. Many people choose to follow sport in spite of sensory difficulties such as sight getting in the way among other possible barriers of enjoyment. As a result, our dashboard has to adapt to any issues subsections of our demographic may encounter with the site. These subsections can include the following:

- Older people with lesser technological abilities.
- People who may not understand certain grammer used.
- People with limited motor &amp; sensory functionality &amp; disabilities.

In order to combat these issues in our overall design, we used the following techniques to make the process of navigation more friendly to vulnerable users.

- Use metaphorical images alongside certain data(i.e positions, statistics) and operations to provide clearer picture of the information being provided.
- Using simplistic language to avoid vagueness in descriptions of the dashboard operations.
- Ensure that the dashboard can be easily navigated and understood by external support software such as screen readers to avoid blocking entry to users with disabilities.
- Maintain a colour and font scheme that ensures that information &amp; actions available are both readable and accessible to those with visual & reading impairments.

















## **5. Heuristic Analysis**

Another important of the design of our interface was to ensure the dashboard is heuristically sound to ensure that the needs &amp; desires of each consumer is ensured. The problem upon which this project aims to solve is that some sports data websites, such as Squawka, can have issues in terms of efficiency &amp; navigating through certain statistics. By ensuring the dashboard complies with certain laws of heuristic analysis, we were able to ensure that the website completes its end goal & satisfies its demographic. We based the satisfaction of this mission upon the Nielsen principles of interaction design.

**User Control and Freedom**

One significant feature in our website allows users to compare &amp; contrast the contributions of players simultaneously. As a result, users of our website are capable of selecting Premier League players of their choice and view how they performed throughout their 2016/17 campaign. They can view numerical &amp; graphical displays of how the performed &amp; judge how they each compare to one another. Should the user feel they no longer are interested in learning about a certain player, they have the freedom to change which players they wish to study.

**Recognition Rather Than Recall**

The aim of this dashboard is for sports fans to navigate through their desired actions with ease. As part of ensuring that said mission is accomplished, we designed our interface in a way that is recognisable for users of any website rather than that of just sports based website. We used visual metaphors &amp; simplistic language to ensure that users of any background can find the information they desire and understand what said information represents. For example, when displaying statistics about players such as predicted odds, there are symbols integrated to symbolise what it represents. This avoids users having to recall the technical details of our prediction system.

**Consistency and Standards**

Consistency is an integral part of the display of statistics in our system. Users needed to be able to view details about certain matches &amp; players in a way that is continuous throughout the entire dashboard. As a result, when displaying details such as predictions and graphics of players performance statistics, the data is always be presented in a consistent fashion that ensures users can have a clear understanding of the information regardless of what player or club they are interested in investigating.



**Flexibility and Efficiency**

Being a data analytics based project, the efficiency of which data is presented to users and the flexibility they have in viewing said data is of utmost precedence. It was critical when implementing calculations of predictions for match outcomes that odds can be presented to users in a timely manner that avoided significant load times as a result of unnecessary calls inside of the algorithm. While implementing the system for predicting match outcomes we had to minimise the number of iterations for the program to generate probabilities regarding each team &amp; their potential match outcomes. We also had to ensure users had the flexibility in both the probability &amp; comparison systems to compare any team or player eligible for the 2017/18 Premier League season.

**Help & Documentation**

As pointed out in our accessibility section, the targeted demographic of this dashboard can have varying knowledge of sport &amp; contrasting experience with online services. As a result, we ensured that an extra effort was made to guide any of our potential users through the process of navigating our website. We have used our homepage as a means to guide non football users through the process of understanding aspects of the game such as Clean Sheets that they may not understand.

**Aesthetic & Minimalistic Design**

One of the main tasks involved in the development of this project was ensuring that not only was the design of our interface aesthetically pleasing, but also simplistic as to not cause confusion among users. Our interface clearly identifies the actions the consumer can take on and presents it in a minimalist fashion that aims to avoid confusion and possibly blocking a user from completing their intended goals with the interface. We also concentrated heavily on the colour scheme of our website to ensure that the interface was visually appealing but non intrusive with how the user may interact with the dashboard.

**Match Between System & The Real World**

While an aim of the dashboard is to make the use of online football statistics easily accessible to sports fans of any knowledge &amp; background, we also had to ensure that the system was relevant to Premier League football and that the information was presented in a way that would match the way statistics &amp; starting teams were presented in a live football broadcast. Whether that&#39;s using statistics such as win rates for certain kinds of fixtures or for displaying the predicted starting team in the correct top down manner. It was a significant goal for us to ensure that the dashboard presented data in a way that is relevant to sports fans.