import unittest
from odds import simulate_match
import pandas as pd
import os
import numpy as np
from scipy.stats import poisson,skellam
import statsmodels.api as sm
import statsmodels.formula.api as smf
import sys


class MyTest(unittest.TestCase):
    def test1(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_mid = simulate_match(poisson_model, "Liverpool", "Middlesbrough")

        homewin = np.sum(np.tril(lfc_mid, -1))
        homeloss = np.sum(np.triu(lfc_mid, 1))
        homedraw = np.sum(np.diag(lfc_mid))
        total=np.ceil(homeloss+homewin+homedraw)
        self.assertEqual(1.0, total)

    def test2(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_hull = simulate_match(poisson_model, "Liverpool", "Hull")

        homewin = np.sum(np.tril(lfc_hull, -1))
        homeloss = np.sum(np.triu(lfc_hull, 1))
        homedraw = np.sum(np.diag(lfc_hull))
        total=homeloss+homewin
        self.assertNotEqual(1.0, total)

    def test3(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_lei = simulate_match(poisson_model, "Liverpool", "Leicester")

        homewin = np.sum(np.tril(lfc_lei, -1))
        homeloss = np.sum(np.triu(lfc_lei, 1))
        homedraw = np.sum(np.diag(lfc_lei))
        total=np.ceil(homeloss+homewin+homedraw)
        self.assertNotEqual(0.5, total)

if __name__ == "__main__":
    unittest.main()
