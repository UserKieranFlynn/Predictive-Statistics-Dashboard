##
# Technical Manual

# CA326 Predicive Football Statistics Dashboard

**By Kieran Flynn & Eoin O'Brien**

## 0. Table of contents

##

- [1. Introduction](#1-introduction)

- [2. System Architecture](#2-system-architecture)

- [3. High Level Design](#3-high-level-design)

- [4. Problems & Resolutions](#4-problems-&-resoultions)

- [5. Instalation Guide](#5-instalation-guide)

## 1. Introduction

**1.1 Overview**

Our project is a predictive football statistics dashboard that is accessed via an internet browser. The dashboard will allow users to access a user interface ran by Flask that holds statistics about clubs &amp; players in the English Premier League for the 2017/2018 season. It uses graphs modelled in Javascript to display the growth of clubs across the previous 2016/17 season in statistics such as points earned and win and loss rates. It also allows users to compare statistics of players by selecting players of their choice &amp; compare the contributions one selected player made to matches in the 2016/17 season versus the other players contributions. You can also view a predicted starting lineup for each team based on how much football each player in each position on the pitch played in the previous season &amp; how often they contributed to the games scoreline in terms of goals and assists. The dashboard also contains a prediction system for predicting results of fixtures throughout the Premier League season based around Poisson Distribution. Our program takes the results &amp; goals each team scored in the previous season &amp; uses it to determine the probabilities of certain teams winning, drawing or losing against an opposing team either at a home game or an away game.

**1.2 Glossary**

**Flask**

_Flask_ which is a microframework for Python based on Werkzeug and Jinja 2 with the aim of allowing the user to build lightweight web applications.

**Jinja 2**

_Jinja2_ is a modern and designer-friendly templating language for Python, modelled after Django&#39;s templates.

**Poisson Distribution**

In probability theory and statistics, the _Poisson Distribution_ is adiscrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space.

**Javascript**

JavaScript is a programming language commonly used in webdevelopment alongside HTML and CSS.

##

##

## 2. System Architecture

The system is primarily written in Python using the Flask web framework with the front-end being an adaptation of the free Sb-Admin-2 Bootstrap Template( A copy of the theme&#39;s License detailing that permission is given to all to use the template, is located in the Code/static directory).

The framework of the application is implemented using Flask. It uses URL routing to determine the content that the user sees which proved to be exceedingly easy to use to allow the user to view similar statistics for multiple players and teams.

The front end of the application is an adaptation of a Bootstrap Template that consists of HTML / CSS, JavaScript / Jquery, Chart.js and other visual aids such as Font Awesome icons. The template consists of a series of custom cards and button components which were ideal for separating data and displaying it in a user friendly manner.

The back-end, or actual data, is contained in a series of MySQL tables. These tables are named &#39;players&#39;, &#39;keepers&#39; and &#39;standings&#39;. The first two contain data about every player and goalkeeper that played in the 2016/2017 English Premier League season. The standings table contains data about the teams that competed in the season as well as their finishing rank.

The last component of the application, and arguably the most important, is a python application built around the Poisson distribution system which makes use of a number of modules described in section 4.1. The application is called via the Flask app when needed and is fed the inputs, such as teams, needed to perform the necessary calculations.

**2.1 System Architecture Diagram**

<img src="/technical_manual/Diagrams/SystemArchitectureDiagram.png" alt="Architecture"
	title="Architecture" width="800" height="500" />


## 3. High-Level Design

**3.1 Context Diagram**

<img src="/technical_manual/Diagrams/ca326ContextDiagram.png" alt="context"
	title="context" width="800" height="500" />

**3.2 Data Flow Diagram - Level One**

<img src="/technical_manual/Diagrams/ca326DFDDiagram.png" alt="dfd"
	title="dfd" width="800" height="500" />

**3.3 Data Flow Diagram - Level Two**

<img src="/technical_manual/Diagrams/PredictionLevelTwo.png" alt="dfd2"
	title="dfd2" width="800" height="500" />


##

##

##

## 4. Problems and Resolution

**4.1 Efficiency of match prediction system**

When researching into prediction systems in terms of statistical analysis &amp; sports predictions in general, we quickly established that a system based around Poisson distribution was the best approach we could take as using modules such as statsmodel, scipy &amp; numpy would make the process of generating probabilities in Python very simple. In saying that, there came an issue in regards to how efficiently the program could take our data &amp; generate these outcomes in a timely manner. There were times when implementing the system where it would take a significant amount of time to generate a result for a given match.

We established the cause of this issue by using the poisson model to summarise that data &amp; the number of iterations taken throughout. We then took measures to reduce the number of calls &amp; iterations throughout our code &amp; we were successful in making the predictions system much more efficient.

**4.2 Data Manipulation & Usage**

We settled upon using MySQL Databases to store our data as it allowed us a lot of flexibility around pulling data that we wanted on a case by case (or page by page) basis. In terms of convenience, directly accessing CSV&#39;s would have been far simpler however it&#39;s not particularly scalable and given many application pages require data from multiple different tables we felt that it was worth doing extra work on the system architecture for benefits down the line. This extra ground work means that should additional years of data, additional leagues or teams, or anything similar be added, the logic used is the same and the application can still rapidly query across large datasets.

**4.3 Sourcing Accurate & Relevant Data**

With the bases of this project being around data analysis &amp; statistical display, sourcing our data was always going to be key to the success of the project. There are a number of sources that can be used to source data about the Premier League but there were a lot of factors to be considered when accessing said data. The data had to contain accurate details &amp; statistics about not only the teams in the league and how they performed throughout the league, but also details on the players they have &amp; the signings they have made for the 2017/2018 season. We were able to source our data from a number of different sources such as kaggle &amp; FBRef &amp; use the csv files they provide to hold our data for the dashboard. However, we feel that too much time was spent normalising the data set &amp; ensuring its accuracy &amp; in hindsight, it would have been an easier approach to simply parse the data from the Premier League website early in the development cycle.

## 5. Installation Guide

Below are a series of steps split into two parts. The first part can be used to simply run the application successfully and use the prediction tool built into the application. The second set of steps are necessary to make use of the statistical display aspect of the application.

**5.1 Getting the application running**

1. Download / pull code from git
2. Install python and add to path (3.6.6 was used throughout development) (&quot;sudo apt update&quot;) (&quot;sudo apt-get install python3.6&quot;)
3. Install python mysql connector (&quot;python -m pip install mysql-connector- **python&quot;** ) - Note the &quot;-python&quot; at the end of the mysql-connector module name.
4. Install flask (&quot;pip install flask&quot;)
5. Install pandas (&quot;pip install pandas&quot;)
6. Install scipy (&quot;pip install scipy&quot;)
7. Install statsmodels (pip install statsmodels)

The application should now be functional and can be run via the command line using the command "**python (or python3) application.py&quot;**" while in the project/Code subdirectory

**5.2 Importing the MySQL tables**

1. Download and Install mysql - [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/) (Should include MySQL Workbench)
2. Make note of root username and password if installing as it is needed to query the database.
3. Create an empty database using root account and make note of the name (**CREATE DATABASE 'databaseName'&quot;**)
4. We found that using MySQL Workbench&#39;s built in tools was the easiest way to import the data needed.
5. Within Workbench select the database to be used

6. Right click Tables \ Table Data Import Wizard

<img src="/technical_manual/InstallationGuideScreenshots/tableimportwizard.png" alt="dfd2"
	title="dfd2" width="800" height="500" />


7. Chose the file path \ Navigate to the project folder and choose &quot;Data/Keepers.csv&quot;
8. Select the option titled &quot;Create new table&quot; and name it &quot;keepers&quot;
9.  Select the Encoding option &quot;latin1&quot;
10. Import the data.
11. Repeat the above steps for Players.csv (naming it &quot;players&quot;) & epl20162017.csv (naming it &quot;standings&quot;)
12. The application should now work as intended.