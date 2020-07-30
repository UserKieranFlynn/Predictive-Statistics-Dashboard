##
# User Guide

# CA326 Predicive Football Statistics Dashboard

**By Kieran Flynn & Eoin O'Brien**

## 0. Table of contents

##

- [1. Statistics Dashboard](#1-statistics-dashboard)

- [2. Predictive Tool](#2-prediction-tool)



The following are a set of instructions and guidelines for using the CA326 Football Statistics Dashboard &amp; Predictive tool.
It is assumed that the application has been installed as intended and is running correctly. Details of this can be found in the Installation Guide in the technical manual.


## 1. Statistics Dashboard

**1.1 Team Stats**

Navigating from the Home Page, the user can visit the Teams or Players sections of the application. These can be navigated to via the NavBar on the left side of the screen. As shown below, left clicking the &quot;Team Statistics&quot; button  will open a dropdown menu containing the Teams link. Left click it to continue.

<img src="/user_manual/Screenshots/TeamsNavbar.png" alt="Navigation Bar Team Statistics Button"
	title="Team Stats" width="240" height="150" />

From here you can choose a team from the dropdown menu or search for a specific once if you don&#39;t see your favourite team.

<img src="/user_manual/Screenshots/TeamsDropDown.png" alt="Teams Dropdown Search Bar"
	title="Team Dropdown Search Bar" width="240" height="480" /> <img src="/user_manual/Screenshots/TeamsSearchBar.png" alt="A team being searched for in the bar"
	title="Teams Dropdown Search Bar" width="240" height="150" />
	



At this point you can see the selected Team&#39;s dashboard. In the top row you have the teams Wins, Draws, Losses and overall Win percentage throughout the 2016/2017 season. Below that are two graphs depicting the points gained throughout the season as well as the wins draws and losses in a doughnut chart.

In the very top right corner of the dashboard is a button to return to the previous team selection page should you wish to view another team&#39;s statistics.

<img src="/user_manual/Screenshots/Returnbutton.png" alt="A Return Button"
	title="Return Button" width="240" height="80" />
	
At the very bottom are a number of other statistics as well as a button allowing you to view the suggested formation and squad based on past performances.

<img src="/user_manual/Screenshots/SquadButton.png" alt="A button to view the suggested squad"
	title="View Suggested Lineup" width="240" height="100" />

By left clicking the  &quot;View Suggested Lineup&quot; button as shown above, you are taken to the squad page. Here you can see the suggested players to field based on past performances. By default the formation is 4:5:1 with a goalkeeper included.

<img src="/user_manual/Screenshots/TeamFormation.png" alt="Suggested Squad and Formation"
	title="Suggsted Squad" width="1000" height="500" />
	
Similar to the previous section, there is a button in the top right corner to return to the team statistics page.


**1.2 Player Statistics**

By navigating to the Players page (The exact same way as &#39;Teams&#39;. Simply left click the &quot;Player Statistics&quot; Menu and select &quot;Players&quot;) you can see a table containing data about all players in our database. Using the custom cards at the top you can even search for specific players or search a team to view all of that team&#39;s players.

<img src="/user_manual/Screenshots/playerName.png" alt="Input box to search for a specific player"
	title="Player Search Bar" width="800" height="200" />
	
<img src="/user_manual/Screenshots/PlayerTeam.png" alt="Input box to search for a specific team's players"
	title="Team Player Search Bar" width="400" height="240" />


**1.3 Goalkeeper Statistics**

The keepers page is functionally the same as the players page with the added ability to search for the Top X (Any number you like) goalkeepers in the given season.

For example, to look at the Top 10 Goalkeepers you would simply enter 10 into the text box as shown below.

<img src="/user_manual/Screenshots/topXKeepers.png" alt="Input box to search for top X Keepers"
	title="Top X Keepers" width="480" height="200" />

## 2. Poisson Prediction Tool

**2.1 Navigating to the Tool**

The prediction tool that is built into the application is extremely easy to locate. Simply left click the &quot;Prediction Tool&quot; button located in the left hand side nav bar to visit the page.

<img src="/user_manual/Screenshots/predictiontool.png" alt="Prediction Tool Navbar Button"
	title="How to navigate to the prediction tool" width="240" height="150" />
	
**2.2 Using the tool**

On the prediction tool page there are 3 input boxes as seen below.

<img src="/user_manual/Screenshots/predictiontoolboxes.png" alt="The input boxes on the prediction tool page"
	title="Prediction Tool input boxes" width="480" height="300" />
	
The first, labelled &#39;Home Team:&#39; is where you enter the home team.

The second, labelled &#39;Away Team:&#39; is where you enter the away team.

The last is where you can enter what probability you want to check. The likelihood of the home/away team winning or the likelihood of a draw.

Should you wish to check the odds of the home team winning, enter -1 into the box.

Should you wish to check the odds of the away team winning, enter &quot; into the box.

Lastly, should you wish to check the odds of the two teams drawing, enter 0 into the box.


**2.3 Working Examples**

Seen below are some examples of the tool being used.

This case is looking for the odds of Chelsea winning at home versus Arsenal.

<img src="/user_manual/Screenshots/ChelseaArsenalHomeWin.png" alt="Chelsea v Arsenal Example"
	title="Chelsea Home Win versus Arsenal" width="600" height="300" />
	
This example is looking for the odds of Liverpool drawing at home versus Manchester United.

<img src="/user_manual/Screenshots/liverpoolManUnitedDraw.png" alt="Liverpool v Man United Example"
	title="Liverpool Draw versus Man United" width="600" height="300" />
	
An example of the output produced by our Poisson application.

<img src="/user_manual/Screenshots/liverpoolManUnitedDrawResult.png" alt="Result of the liverpool v Man United input"
	title="Poisson Prediction Tool output" width="800" height="50" />
	
We hope that the above set of guidelines are comprehensive enough to allow you to fully enjoy our application.

