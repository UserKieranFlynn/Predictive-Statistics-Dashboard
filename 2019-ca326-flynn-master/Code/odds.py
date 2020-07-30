import pandas as pd
import os
import numpy as np
from scipy.stats import poisson,skellam
import statsmodels.api as sm
import statsmodels.formula.api as smf
import sys

def simulate_match(model, homeTeam, awayTeam, max_goals=12):

    home_goals = model.predict(pd.DataFrame(data={'team': homeTeam, 'opponent': awayTeam,'home':1}, index=[1])).values[0]
    away_goals = model.predict(pd.DataFrame(data={'team': awayTeam, 'opponent': homeTeam,'home':0}, index=[1])).values[0]
    prediction = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals, away_goals]]
    return(np.outer(np.array(prediction[0]), np.array(prediction[1])))


def main(homeTeam, awayTeam, selectedOption):

    results = pd.read_csv("../Data/results.csv")
    results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
    results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
    results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

    poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()


    lfc_mid = simulate_match(poisson_model, "Liverpool", "Middlesbrough")
    lfc_hull = simulate_match(poisson_model, "Liverpool", "Hull")
    lfc_burn = simulate_match(poisson_model, "Liverpool", "Burnley")
    burn_hull = simulate_match(poisson_model, "Liverpool", "Burnley")

    #promoted_home=(np.sum(np.tril(lfc_mid, -1))+np.sum(np.tril(lfc_hull, -1))+np.sum(np.tril(lfc_burn, -1)))/3
    #print(promoted_home)

    #Prediction Page
    #Application.py passes the two values from the webpage to the main function for the program to use    
    home_away = simulate_match(poisson_model, homeTeam, awayTeam)
    if selectedOption == -1: 
        webpage_Input = np.sum(np.tril(home_away, -1))
    elif selectedOption == 0:
        webpage_Input = np.sum(np.diag(home_away, 0))
    elif selectedOption == 1:
        webpage_Input = np.sum(np.triu(home_away, 1))
    return(webpage_Input)        

if __name__ == "__main__":
    main()


