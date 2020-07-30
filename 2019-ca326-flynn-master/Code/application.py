import mysql.connector
import dblogin
from flask import Flask, render_template, request, redirect, url_for
import re
import odds

app = Flask(__name__)

#Default Home page route
@app.route("/")
def homepage():
	return render_template("index.html")

@app.route("/teams/")
@app.route("/teams")
def teamsLanding():
	return render_template("teamLanding.html")

#Default team stats page
@app.route("/teams/<string:team>")
def teamsInput(team):
	try:
		selectedTeam = team
		mydb = mysql.connector.connect(
	  		host=dblogin.host.strip(),
	  		user=dblogin.user.strip(),
	  		passwd=dblogin.password.strip(),
	  		database=dblogin.database.strip()
		)
		mycursor = mydb.cursor()

		#Counts number of wins in a season and converts to int			
		winsQuery = f"SELECT Wins FROM standings WHERE Team = '{team}';"
		mycursor.execute(winsQuery)
		wins = mycursor.fetchall()

		#Takes the returned list of values and strips it to an int value
		for item in wins:			
			wins = str(item)		
		wins = int(re.sub('[(),]', '', wins))

		#Counts number of losses in a season and converts to int
		lossesQuery = f"SELECT Loss FROM standings WHERE Team = '{team}';"
		mycursor.execute(lossesQuery)
		losses = mycursor.fetchall()
		

		#Takes the returned list of data values and strips it to an int value		
		for item in losses:			
			losses = str(item)			
		losses = int(re.sub('[(),]', '', losses))

		#Queries Database for home win rate
		homeWinRateQuery = f"SELECT Home_Win_Rate FROM standings WHERE Team = '{team}';"
		mycursor.execute(homeWinRateQuery)
		homeWinRate = mycursor.fetchall()
		#Simply formats returned data to be usable				
		for item in homeWinRate:			
			homeWinRate = str(item)			
			homeWinRate = homeWinRate.replace("'", "")		
		homeWinRate = int(re.sub('[(),%]', '', homeWinRate))
					 
		
		#Queries Database for home loss rate
		homeLossRateQuery = f"SELECT Home_Loss_Rate FROM standings WHERE Team = '{team}';"
		mycursor.execute(homeLossRateQuery)
		homeLossRate = mycursor.fetchall()
		#Simply formats returned data to be usable		
		for item in homeLossRate:			
			homeLossRate = str(item)			
			homeLossRate = homeLossRate.replace("'", "")		
		homeLossRate = int(re.sub('[(),%]', '', homeLossRate))

		#Queries Database for away win rate
		awayWinRateQuery = f"SELECT Away_Win_Rate FROM standings WHERE Team = '{team}';"
		mycursor.execute(awayWinRateQuery)
		awayWinRate = mycursor.fetchall()
		#Simply formats returned data to be usable		
		for item in awayWinRate:			
			awayWinRate = str(item)			
			awayWinRate = awayWinRate.replace("'", "")		
		awayWinRate = int(re.sub('[(),%]', '', awayWinRate))
			
		#Queries Database for away loss rate
		awayLossRateQuery = f"SELECT Away_Loss_Rate FROM standings WHERE Team = '{team}';"
		mycursor.execute(awayLossRateQuery)
		awayLossRate = mycursor.fetchall()
		#Simply formats returned data to be usable		
		for item in awayLossRate:			
			awayLossRate = str(item)			
			awayLossRate = awayLossRate.replace("'", "")		
		awayLossRate = int(re.sub('[(),%]', '', awayLossRate))
		
		#Queries Database for total points
		pointsQuery = f"SELECT Points FROM standings WHERE Team = '{team}';"
		mycursor.execute(pointsQuery)
		pointsTotal = mycursor.fetchall()
		#Simply formats returned data to be usable		
		for item in pointsTotal:			
			pointsTotal = str(item)			
		pointsTotal = int(re.sub('[(),]', '', pointsTotal))		
		#Converts to percentage
		pointsPercentage = round((pointsTotal / 114 * 100), 2)

		#Calculates number of draws
		draws = 38 - (wins + losses)

		#Calculates the teams overall win %
		winPercentage = round((wins/38 *100), 2)
		listValues = [wins, losses, draws]

		if team == "Hull City" or team == "Sunderland" or team == "Middlesbrough":
			return render_template('hullTeam.html', wins=wins, losses=losses, draws=draws, homeWinRate=homeWinRate, homeLossRate=homeLossRate, awayWinRate=awayWinRate, awayLossRate=awayLossRate, pointsPercentage=pointsPercentage, listValues=listValues, winPercentage=winPercentage, selectedTeam = selectedTeam)
		return render_template('teams.html', wins=wins, losses=losses, draws=draws, homeWinRate=homeWinRate, homeLossRate=homeLossRate, awayWinRate=awayWinRate, awayLossRate=awayLossRate, pointsPercentage=pointsPercentage, listValues=listValues, winPercentage=winPercentage, selectedTeam = selectedTeam)		

	except Exception as e:
		return (str(e))

	finally:
		mydb.close()

@app.route("/teams/<string:team>/squad")
def squad(team):
	try:
		selectedTeam = team
		#Temporary fix due to Bournemouth being named differently between tables
		if selectedTeam == "AFC Bournemouth":		
			team = "Bournemouth"

		mydb = mysql.connector.connect(
	  		host=dblogin.host.strip(),
	  		user=dblogin.user.strip(),
	  		passwd=dblogin.password.strip(),
	  		database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()

		#Return top keeper for selected team
		keeperQuery = f"select ﻿Player from keepers where squad='{team}' and (In_17_18 = 'S' or In_17_18='Y') order by 'cs%' desc limit 1"		
		mycursor.execute(keeperQuery)
		keeperData = mycursor.fetchall()
		#cleans up keeperName string to be usable	
		keeperName = (re.sub('[(),]', '', str(keeperData[0]))).replace("'", "")	

		#Return top defenders for selected team
		#Temporary fix due to Bournemouth being named differently between tables
		if selectedTeam == "Leicester City":
			team = "Leicester"
		defenderQuery = f"select Player from players where club ='{team}' and Position like '%DF%' and (In_17_18 = 'F' or In_17_18='Y') order by Appearances desc limit 4;"
		mycursor.execute(defenderQuery)
		defenderData = mycursor.fetchall()
		defenderNames = []
		for item in defenderData:
			defender = re.sub('[(),]', '', str(item)).replace("'", "")
			defenderNames.append(defender)

		#Return top Midfielders for selected team
		midfieldersQuery = f"select Player from players where club = '{team}' and Position like '%MF%' and (In_17_18 = 'F' or In_17_18='Y') order by GoalsAndAssistsMinusPenaltiesPer90 desc limit 5;"
		mycursor.execute(midfieldersQuery)
		midfielderData = mycursor.fetchall()
		midfielderNames = []
		for item in midfielderData:
			midfielder = re.sub('[(),]', '', str(item)).replace("'", "")
			midfielderNames.append(midfielder)	

		#Return top Strikers for selected team
		strikerQuery = f"select Player from players where club = '{team}' and Position like '%FW%' and (In_17_18 = 'F' or In_17_18='Y') order by GoalsAndAssistsMinusPenaltiesPer90 desc limit 1;"
		mycursor.execute(strikerQuery)
		strikerData = mycursor.fetchall()
		#cleans up strikerName string to be usable	
		strikerName = (re.sub('[(),]', '', str(strikerData[0]))).replace("'", "")	
		return render_template("squad.html", selectedTeam=selectedTeam, keeperName=keeperName, defenderNames=defenderNames, midfielderNames=midfielderNames, strikerName=strikerName)
	
	except Exception as e:
		return (str(e))

	finally:
		mydb.close()

#The default keepers page displaying all players in database
@app.route("/players/")
def players():
	try:		
		mydb = mysql.connector.connect(
	  		host=dblogin.host.strip(),
	  		user=dblogin.user.strip(),
	  		passwd=dblogin.password.strip(),
	  		database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()	
		query = "SELECT * FROM players;"
		mycursor.execute(query)
		data = mycursor.fetchall()
		return render_template('players.html', data=data,)
	
	except Exception as e:
		return (str(e))

	finally:
		mydb.close()

#The rerouted page after submitting via the input boxes
@app.route("/players/input")
def playerInput():
	try:		
		mydb = mysql.connector.connect(
		  	host=dblogin.host.strip(),
		  	user=dblogin.user.strip(),
		  	passwd=dblogin.password.strip(),
		  	database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()
		#Takes the names entered into the text boxes on the player site	
		playerNameList = request.args.getlist("playername")
		query = "SELECT * FROM players WHERE Player = '" + playerNameList[0] +"'"# + "or Player = '" + request.args.get("playername","") +"'"
		for item in playerNameList[1:]:
			query += "or Player = '" + item + "'"		
		mycursor.execute(query)
		data = mycursor.fetchall()
		return render_template('players.html', data=data,)		

	except Exception as e:
		return (str(e))

	finally:
		mydb.close()

@app.route("/players/selectedTeam")
def playerSelectTeam():
	try:		
		mydb = mysql.connector.connect(
		  	host=dblogin.host.strip(),
		  	user=dblogin.user.strip(),
		  	passwd=dblogin.password.strip(),
		  	database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()
		#Takes the number entered into the Top X query
		selectedTeams = request.args.getlist("selectedTeam")		
		for item in selectedTeams:
			team = item		
		query = ""
		teams = ["Chelsea",
                  "Tottenham Hotspur",
                  "Manchester City",
                  "Liverpool",
                  "Arsenal",
                  "Manchester United",
                  "Everton",
                  "Southampton",
                  "Bournemouth",
                  "West Bromwich Albion",
                  "West Ham United",
                  "Leicester City",
                  "Stoke City",
                  "Crystal Palace",
                  "Swansea City",
                  "Burnley",
                  "Watford",
                  "Hull City",
                  "Middlesbrough",
                  "Sunderland"]
		if team in teams:			
			query = "SELECT * FROM players WHERE Club='" + team + "'"		
		mycursor.execute(query)
		teamPlayers = mycursor.fetchall()
		return render_template('players.html', data=teamPlayers,)		

	except Exception as e:
		return (str(e))

	finally:
		mydb.close()

#The default keepers page displaying all keepers in database
@app.route("/keepers")
def keepers():
	try:		
		mydb = mysql.connector.connect(
	  		host=dblogin.host.strip(),
	  		user=dblogin.user.strip(),
	  		passwd=dblogin.password.strip(),
	  		database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()	
		query = "SELECT * FROM keepers;"
		mycursor.execute(query)
		data = mycursor.fetchall()
		return render_template('keepers.html', data=data,)
	
	except Exception as e:
		return (str(e))

	finally:
		mydb.close()
		
#The rerouted page after submitting via the input boxes
@app.route("/keepers/input")
def keepersInput():
	try:		
		mydb = mysql.connector.connect(
		  	host=dblogin.host.strip(),
		  	user=dblogin.user.strip(),
		  	passwd=dblogin.password.strip(),
		  	database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()
		#Takes the names entered into the text boxes on the keeper site	and construct a query
		keeperNameList = request.args.getlist("keepername")
		query = "SELECT * FROM keepers WHERE ﻿Player = '" + keeperNameList[0] + "'"		
		for item in keeperNameList[1:]:
			query += " or ﻿Player = '" + item + "'"		
		mycursor.execute(query)
		data = mycursor.fetchall()
		return render_template('keepers.html', data=data,)		

	except Exception as e:
		return (str(e))

	finally:
		mydb.close()

@app.route("/keepers/selecttop")
def selecttopkeepers():
	try:		
		mydb = mysql.connector.connect(
		  	host=dblogin.host.strip(),
		  	user=dblogin.user.strip(),
		  	passwd=dblogin.password.strip(),
		  	database=dblogin.database.strip()
		)		

		mycursor = mydb.cursor()
		#Takes the number entered into the Top X query
		topKeepersNum = request.args.getlist("topkeepers")		
		if topKeepersNum[0] != "":
			query = "SELECT * FROM keepers WHERE Squad='" + topKeepersNum[0] + "' and (In_17_18='Y' or In_17_18='S') order by 'cs%' desc limit " + topKeepersNum[1] + ";"
		else:
			query = "SELECT * FROM keepers order by 'cs%' desc limit " + topKeepersNum[1] + ";"					
		mycursor.execute(query)
		topKeepersData = mycursor.fetchall()
		return render_template('keepers.html', data=topKeepersData,)		

	except Exception as e:
		return (str(e))

	finally:
		mydb.close()


#Prediction Tool
@app.route("/prediction")
def prediction():	
	return render_template('prediction.html')

#Prediction Tool Input to use text boxes in the prediction.html page
@app.route("/prediction/input")
def predictionInput():		
	teamNameList = request.args.getlist("teamname")
	selectedOptionList = request.args.getlist("selectedOption")	
	selectedOption = selectedOptionList[0].strip()
	selectedOption = int(selectedOption)	
	options = [0,1,-1]
	teams = ["Chelsea",
                  "Tottenham Hotspur",
                  "Man City",
                  "Liverpool",
                  "Arsenal",
                  "Man United",
                  "Everton",
                  "Southampton",
                  "Bournemouth",
                  "West Bromwich Albion",
                  "West Ham United",
                  "Leicester City",
                  "Stoke City",
                  "Crystal Palace",
                  "Swansea City",
                  "Burnley",
                  "Watford",
                  "Hull City",
                  "Middlesbrough",
                  "Sunderland"]
	returnString = ""
	if teamNameList[0] not in teams or teamNameList[1] not in teams:		
		returnString = "You must enter two valid teams in the above boxes!"
		return render_template('prediction.html', returnString=returnString)
	if selectedOption not in options:
		returnString = "You must enter a valid option as described above the text box"
		return render_template('prediction.html', returnString=returnString)
	dataReturn = str(odds.main(teamNameList[0].strip(), teamNameList[1].strip(), selectedOption))	
	if selectedOption == -1:
		selectedTeam = str(teamNameList[0].strip())
		returnString = "There is a " + dataReturn + " likelihood that " + selectedTeam + " will win."
	elif selectedOption == 1:				
		selectedTeam = str(teamNameList[1].strip())	
		returnString = "There is a " + dataReturn + " likelihood that " + selectedTeam + " will win."
	elif selectedOption == 0:
		returnString = "There is a " + dataReturn + " likelihood that " + teamNameList[0].strip() + " and " + teamNameList[1].strip() + " will draw."
	return render_template('prediction.html', returnString=returnString)

#404 Page error handler
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

#Other Section
if __name__=="__main__":
	app.run(debug=True)

'''
ToDo
- Teams Route - Combine all queries into one
- Write function to do string formatting rather than performing each time
- clean up /prediction/input route
'''