## CA326 FUNCTIONAL SPECIFICATION

### Predictive Football Statistics Dashboard

#### Kieran Flynn

###### &

#### Eoin O’Brien

##### Submission Date: (07/12/2018)

# 0

## Table of Contents


```
1 Introduction .........................................................................................................3
1.1 Overview
1.2 Business Context
1.3 Glossary
2 General Description ..................................................................................................4
2.1 Product / System Functions
2.2 User Characteristics / Objectives
2.3 Operational Scenarios 5
2.4 Constraints 6
2.5 Predictive Tool Testing
3 Functional Requirements ..............................................................................................7
```
```
3.1 Navigate the application
3.2 View previous results
3.3 View upcoming fixtures..............................................................................................8
3.4 View team statistics
3.5 View individual player statistics...................................................................................9
3.5 Compare players
3.7 View upcoming match predictions.....................................................................................10
3.8 View player performance predictions
3.9 View formation and starting line-up suggestions.....................................................................11
4 System Architecture ..................................................................................................12
```
```
4.1 System Architecture Diagram (Fig 4.1)
4.2 Website
4.3 Application Framework
4.4 MySQL Database
5 High-Level Design ....................................................................................................13
```
```
5.1 High-Level Design diagram
5.2 High-Level Design diagram description...............................................................................14
6 Preliminary Schedule ................................................................................................ 15
```
```
6.1 GANTT Charts
7 Appendix ............................................................................................................ 16
```



# 1


__1.1 Overview__

The system being developed is a web-based statistics dashboard for a football club. For this project that football club with be Liverpool FC, however in theory it would work for any club with an equal amount of available data. The application aims to have two parts:

- A dynamic display featuring in depth statistics that the user can interact with in an
    accessible and easy to use manner.
- A tool that aims to accurately (within reason) predict results, scores and player
    performance based on historical data.

Due to the nature of the project, data objectivity and reputability is an incredibly important factor. As such, to be as fair as possible, the data used throughout the application is from various sources. The primary two sources are the official Premier League website and Squawka (Both referenced below). The data from the two of these websites will be averaged where applicable. Some statistics are only found on one of the sites and not the other so in those cases the data will be the original figures.


__1.2 Business Context__

This system is targeted towards sports fans; both soccer and Liverpool fans, and has a lot of potential as there are few statistical resources openly available that are predictive in their analysis of team’s performances. The sites referenced below (Section 7) have in depth statistics about the performances of the teams & players in matches that have already occurred, but they do not have data about how the teams & players may perform in the future. Tools such as this are used by betting companies to generate odds, and by games such as Fantasy Football to decide the prices that players be bought for. The only online, open source application of any sports data that attempts to predict player performances is the NFL Fantasy Football game that predicts how many fantasy points a player will earn on matchday. To provide a system that fans can use to see how their favourite players could potentially perform would fill a significant hole in the soccer statistics market.

__1.3 Glossary__

- __The Team__

    Any references made to ‘The Team’, or data related to said team, are assumed to be
    in relation to Liverpool FC unless explicitly stated to be otherwise.

- __MySQL__

    MySQL is an open source relational database management system that relies on
    SQL to manipulate the data in a given database.

- __HTML__

    Hypertext Markup Language is the standard markup language for creating web
    pages and web applications.

- __Flask__

    Flask is a micro web framework written in Python.

## Introduction


# 2

__2.1 Product / System Functions__

The Statistics Dashboard element of the application aims to display a wide range of
information such as (but not limited to) the following:

- Upcoming fixtures
- Previous match results
- Goal scorers, Assists, Saves, Clean Sheets
- Shots, Shots on target
- Penalties, Free Kicks
- Yellow Cards, Red Cards
- Player specific information

The data displayed is dependent on the sources from which they are being taken, therefore
the list above is not all-inclusive.

The Predictive Tool element of the application aims to be able to:

- Predict the outcome and score of future matches & performances based on historical
    results, current player performance and opponent form.
- Make suggestions about formation, starting line-ups etc.
It should be noted that although we are aiming to have this tool be as accurate as possible
(Testing is discussed later) it’s difficult to say how accurate it will be due to the volatile nature
of football and the unpredictability involved in predicting outcomes.

__2.2 User Characteristics and Objectives__

As the application will be a web based one, the system is accessible to anybody with a
computer and access to the Internet. We predict the main user group to be males between
the ages of 18-30, as this is large percentage of football supporters, however this target
audience does not necessarily preclude users from outside of that demographic from using
the application.

The site will be easily accessible with a dynamic and user-friendly dashboard interface to
accommodate users with little to no knowledge of computing. Ideally the application would
also be mobile friendly, however as the primary focus is on Desktop access that wouldn’t be
at the top of our priorities for the timeframe we have.

## General Description


__2.3 Operational Scenarios__

There are three key uses of our web application. Each of them can be accessed by any user
that utilises the application with no higher authority or permissions required. Each user can
access & implement the information & tools provided at any time of day in the year & for any
purpose that they desire. These uses cases are as follows:

__View Statistics:__

Our users will be able to navigate through our application to view statistics about numerous
aspects of Liverpool Football Club. They will be able to use our app to view results from the
clubs 2016/17 Premier League campaign & the events that occurred throughout the game
they have selected such as goals scored. Not only will they be able to view how Liverpool,
as a team, performed on the pitch throughout the season, they will also be able to select
members of the playing squad that Liverpool have registered & view the statistics of how
each of them have performed throughout the 2016/17 in each aspect of playing football,
such as offensive & defensive contributions, & showcase them using dynamic graphs &
diagrams that make the players growth and/or decline overtime.

__Compare Players:__

Using the statistics that showcase how each player has performed throughout the season as
well as our predictions for how each player can potentially play throughout the 2017/
season. We aim to have a comparison system inside of the application where users can
select any player inside of the playing squad & compare the current & potentially future
statistics of the players to contrast their performances & determine which player has been
more impressive throughout the season & which can potentially do well in the upcoming
fixtures for the club.

__Predict future performance:__

Perhaps the most unique aspect of the application is our performance predictions tool. We
aim to have an algorithmic tool in place that can go through each of the fixtures in the
2017/18 season of the Premier League campaign for Liverpool & predict how the result of
each of their matchups will end. You will then be able to view the statistics of how each of
the players are predicted to perform in each game and throughout the season as a whole &
view what starting eleven the manager will look to play in each of the fixtures and what
position each player will potentially play.


__2.4 Constraints__

__Speed__

As the system is a web application, speed is a critical constraint to keep in mind. Users won’t
be able to use the system to its’ full extent if it takes a significant period to load pages,
change between stats shown / diagram types etc. We will have to ensure that navigation
requests, database calls and updating web-pages all happen promptly to prevent the user
from exiting the application.

__Space__

Space is somewhat of a concern seeing as all the back-end data being analysed will be
stored within a SQL database. However, given the limited scope of the data being used (A
set period of the 2015/2016 football season) this shouldn’t be an issue that will be of major
concern to us.

__Reliable Data__

Although there are plenty of resources that can provide accurate statistics about the Premier
League and the results & performances of players in the league, some can have
discrepancies in certain data throughout a whole season, for example how many goals a
team has conceded. This will become a major issue regarding the accuracy of our statistics
& the predictive data we generate.

__2.5 Predictive Tool Testing__

Related to our time frame for data, we aim to run a sort of simulation to gauge the accuracy
of our predictive statistic tool when it is implemented. For our statistical pages, the data will
be based on the 2016/2017 Premier League Season. However, we will take the data from
2017/2018 and use it as a pseudo live season to simulate an actual season in real time. By
using an already completed data set it allows us far more flexibility for testing purposes than
using the current (2018/2019) Premier League season which would need to be updated on a
weekly basis.


# 3 Functional Requirements

__3.1 Navigate the application__

- __Description__

    The application must allow the user to navigate between its’ different components
    quickly and easily. The system must be able to keep up with the user’s navigation
    requests and carry them out in real time. The User-Interface also must be easy to
    use and intuitive to offer a good user experience.

- __Criticality__

    A web-based application must be both visually appealing while remaining functional.
    This is an extremely important aspect of this project that will require a lot of research.
    Things such as colour schemes, fonts, font sizes, images, overall layout and
    accessibility must be considered when designing an effective User-Interface.

- __Technical issues__

    Handling the user’s request quickly and accurately is vital to ensuring that the user
    does not become frustrated while using the application. It should also be obvious to
    the user what will occur upon actions such as clicking a button in the navigation bar,
    for example.

- __Dependencies__

    This is the main navigation point for the entire application. Without it users will not be
    able to interact with the various other components of the system. As such it is a given
    that all other functional requirements depend on this requirement.

__3.2 View Previous Results__

- __Description__

    The user should be able to view the team’s past matches and the score of that
    match. In this specific case, a user should be able to see all of Liverpool’s games in
    the 2015/2016 season.

- __Criticality__

    We feel that this is one of the most important features that would draw users in to use
    the application. It also serves as a nice introduction into many of the other statistics
    that the system will display.

- __Technical issues__

    The results will most likely be displayed in some sort of table or diagram, so ensuring
    that there are no issues with this displaying on different browsers, resolutions etc. is
    very important. Naturally it also needs to be correct. Otherwise it would be quite
    redundant.

- __Dependencies__

    This aspect of the application is dependent on the database containing results from
    the 2016/17 season with data attributes such as the score line, players appearing in
    the match & their contributions. The presence of this data inside the database is
    required not only to view details about the results, but to compute statistics in other
    aspects of the application.


__3.3 View upcoming fixtures__

- __Description__

    The user should be able to view the team’s upcoming games in the season and the
    location at which they will be taking place. In this specific case, a user should be able
    to see Liverpool’s games in the 2016/2017 season.

- __Criticality__

    Like the above requirement, we feel that is is also a drawing point to get users to use
    the system. It also serves as a nice introduction to the predictive aspect of the
    application.

- __Technical issues__

    Again, similar to the requirement found in section 3.2, this information will likely be
    displayed in some sort of graph or diagram. Being able to display this information is
    very important and will likely require testing later.

- __Dependencies__

    The fixtures feature of the application is dependent on the presence & accuracy of
    the fixture list for the 2017/18 Premier League season. This requires having the
    correct dates & kick-off times for each game in the clubs thirty-eight game season as
    well as having the venue of the home & away matches.

__3.4 View team statistics__

- __Description__

    The user should be able to view Liverpool FC’s general statistics. This data will be
    displayed in some form of table or graph. The specific data being shown include
    things such as total goals throughout a season, free kicks, penalties and corners. It
    will be general information that anyone looking to find data on their favourite team
    would like to see.

- __Criticality__

    Like 3.2 and 3.3, it is a key draw point for a user. User’s will want to know the above
    information and more and displaying it in a way that is user friendly and dynamic is a
    very important goal to try and accomplish.

- __Technical issues__

    Data reliability comes in to play with this requirement a lot more than the previous
    two as it relies on the source heavily. This is one section where having data taken
    from multiple locations and aggregating it is a good idea in our minds.
    Due to more data needing to be displayed in this section it is important to possibly
    look at the display on different resolution browsers or devices if possible.

- __Dependencies__

    Viewing the statistics of the performances of Liverpool is dependent on section 3.
    of the application. To generate statistics about the club’s performances in each
    match there must be data available showing each result of the 2016/17 season of
    Liverpool and the events that occurred throughout each 90 minutes in said season.


__3.4 View Individual Player Statistics__

- __Description__

    The user should be able to navigate to some sort of selection page where they can
    specify to the application which players’ statistics they would like to view. They
    should be able to choose more than one player at a time to compare if they so wish
    (Discussed in more detail in 3.6).

- __Criticality__

    Like 3.4, this kind of information is very important to those users who have an interest
    in the numbers and data that make football such an intriguing sport to watch. This
    information is also vital to have as it will heavily influence the predictive element of
    the application with regards to suggested squads and formations.
    Information such as Goals scored, Shots on Target, Tackles made, and goals will be
    displayed here through a variety of mediums.

- __Technical Issues__

    Data objectivity is crucial to maintaining the integrity of the application with regards to
    specific player information. Choosing sources that are known to be objective (in that
    they don’t cherry-pick information to make specific players look good or bad) is a vital
    step to take. For example, we felt that using Liverpool FC’s own website, although
    insightful for this area, could compromise the integrity of the data that underlies this
    whole project.

- __Dependencies__

    To have statistics of each player in the Liverpool squad readily available then each
    registered player will have to be present inside of a dataset. There also must be
    information provided from features such as the results section in Section 3.2 about
    which players played in each match in the 2016/17 season & what each of the
    players contributed to each match that they have played in.

__3.6 Compare Players__

- __Description__

    Should a user select more than one player’s information to view, they are also given
    an option to compare those players. Although comparing a Goalkeeper with a Striker
    may not be that beneficial, a user might wish to compare two defenders to see which
    player is currently or historically the ‘better’ player. Our application will attempt to help
    them make this decision by providing reliable and objective information.

- __Criticality__

    This requirement links in heavily with 3.5 and as such does not need a huge amount
    of expansion.

- __Technical Issues__

    It is important to ensure that the information being pulled is for the correct players
    and doesn’t get mixed up or muddled when displayed.

- __Dependencies__

    Much like Section 3.5, the system for comparing players will require having data
    about each player in the squad & their contributions. These will need to be available
    for each aspect, such as offence or defence, that the user wants to compare players
    in.


__3.7 View predictions for upcoming matches__

- __Description__

    By using the predictive tool element of the application, the user should be able to
    view the predicted score for a chosen game.

- __Criticality__

    As this is the second core feature of our project it is important that we implement this
    in an effective manner. However, due to the nature of football and predictive analysis
    in general, we are not expecting it to be entirely accurate. This will of course be made
    known to the user at the earliest intervention.

- __Technical issues__

    A lot of research into predictive analysis algorithms will need to take place before
    attempting to implement this feature. Due to a wide range of choices with regards to
    these algorithms it will be important to identify which one will best suit our needs for
    the task at hand.

- __Dependencies__

    Research into algorithms & implementation of said analysis algorithms will be
    required to compute the predictions for each upcoming match in the fixture list of
    Liverpool. But it will also depend on the accuracy & presence of the fixtures system in
    Section 3.3 for accurate analysis of each fixture.

__3.8 View predictions for player performances__

- __Description__

    Building from requirement 3.7, the user should be able to view specific player
    predictions. They will be scored on some sort of metric that as of right now is to be
    determined.

- __Criticality__

    This is an important feature to be able to implement for the user’s benefit, however it
    is not as critical as other sections such as simply being able to see the system’s
    predicted score for a given match.

- __Technical issues__

    Like 3.7 while also being one step more difficult in that more data must be given to
    and taken from the predictive tool.

- __Dependencies__

    This will be much like section 3.7 in that it will depend on implementing analytical
    algorithms to compute each player potential statistics, but it will also depend on the
    presences of the players details & previous statistics in Section 3.5 to ensure that
    accurate statistics can be generated for each player in the squad.


__3.9 View system suggestions for formation / starting team__

- __Description__

    The user should be able to see the tool’s recommended starting team, substitutes
    and team formation for the selected fixture.

- __Criticality__

    This is a feature that we would like to see implemented during the time frame we
    have however due to the complexity of it it is more of a desire rather than a vital
    feature to have.

- __Technical issues__

    Like 3.7 and 3.8, it will require a significant amount of research into the required
    analytical algorithms while also ensuring that the players used by the manager are
    used correctly in their desired position, if not, then in the pitch they have the most
    experience in. For example, making sure that defenders are always part of a
    defensive back line of 3, 4 or 5 defenders.

- __Dependencies__

    Again, this will be quite similar section 3.7 and 3.8 as it will depend on implementing
    analytical algorithms to generate the potential on pitch system that the manager uses
    but it will also depend on the accuracy of both the player statistics system & the
    results system in section 3.3 & 3.5 to ensure that the formation implemented & the
    positions taken by the players are consistent with how the manager has set up in
    previous.


# 4 System Architecture

__4. 1 System Architecture Design Diagram__




<img src="/Images/system.png" alt="system"
	title="System" width="650" height="400" />

Fig 4.1


Fig 4.1 above illustrates the overall architecture of the system. As the above diagram shows
there are three distinct aspects to the architecture. The first is the
website (front end. What the users see), then the Application Framework (which queries the
database and returns the content to populate pages) and finally the MYSQL database (which
stores the statistics tables).

__4. 2 Website__

The website as shown in the above diagram is the front end of the application, or what the
user will see. This is what they will interact with the view the requested statistics and data for
a variety of subjects. This will be the least technical element of the product, however will still
involve research for functional UI design techniques and dynamic dashboarding methods.


__4.3 Application Framework__

The second component of the application consists of the application framework. We plan to
use some sort of web-based Python framework (e.g. Flask) to deal with pipeline code. This
framework will have two main functions. The aim is to have this component handle requests
from the user and grab the necessary data from the MySQL Database (4.3). This information
will then be formatted into different forms to be displayed on the front end.

This framework will also contain the predictive statistic tool as described before. Although as
of right now we don’t know which algorithms will be used for this tool, we hope to source
python implementations that can serve our needs for this.

__4.4 MySQL Database__

Lastly is the back-end database. This will contain the raw information taken from our data
sources to be used by the framework and displayed via the website.


# 5 High-Level Design

__5.1 High-Level Design Diagram__

<img src="/Images/HighLevel.png" alt="HighLevel"
	title="High Level" width="250" height="2500" />

Fig 5.1


__5.2 High-Level Design Diagram Description__

Fig 5.1 is explained below.

- __Step 1: Navigate to Home Page__

    Simply a starting point for the user. From here they can choose from several options.

- __Step 2: View Team Stats__

    One of the fundamental statistics the user may want to see. In this case Liverpool
    FC’s current overall statistics would be displayed.

- __Step 3: View Team Fixtures / Results__

    Here the user would see the current league position, Win / Loss Ratio, upcoming
    matches & their locations.

- __Step 4: View Player List__

    The user is presented with some form of squad list to choose from.

- __Step 5: View Player Stats__

    The user may view a single players’ season statistics or compare multiple players to
    analyse performance differences.

- __Step 6: Navigate to Prediction Tool__

    The user can also navigate to the predictive statistic tool located in another area of
    the application. From here they can choose one of the features that the tool will offer.

- __Step 7: View Match Predictions__

    The core feature that the tool would provide would be a simple Win / loss and score
    prediction for a given match.

- __Step 8: View Player Performance Predictions__

    The tool also aims to be able to give expected player performances based on both
    historical and current form data.

- __Step 9: View Formation Suggestions__

    The tool may lastly be able to offer some suggestions for formation and tactics based
    on their opponent as well as their own strengths & weaknesses.


# 6 Preliminary Schedule

__6.1 GANTT Charts__

<img src="/Images/Part1.png" alt="Schedule"
	title="The Schedule" width="750" height="500" />

Fig 6.1

<img src="/Images/Part2.png" alt="Schedule"
	title="The Schedule" width="750" height="500" />

Fig 6.2


# 7 Appendices


Squawka statistics website - http://www2.squawka.com/football-stats/

Official Premier League statistics website - https://www.premierleague.com/stats

Official Premier League Fantasy Football website - https://fantasy.premierleague.com/

Official National Football League Fantasy Football website - https://fantasy.nfl.com/

MySQL Official Website - https://www.mysql.com/


