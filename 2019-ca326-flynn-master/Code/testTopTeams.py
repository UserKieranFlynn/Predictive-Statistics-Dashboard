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
    def testLivManU(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_manu = simulate_match(poisson_model, "Liverpool", "Man United")
        
        homewin = np.sum(np.tril(lfc_manu, -1))
        awaywin = np.sum(np.triu(lfc_manu, 1))
        self.assertGreater(homewin, awaywin)

    def testManULiv(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        manu_lfc = simulate_match(poisson_model, "Man United", "Liverpool")
        
        homewin = np.sum(np.tril(manu_lfc, -1))
        awaywin = np.sum(np.triu(manu_lfc, 1))
        self.assertGreater(homewin, awaywin)

    def testManCLiv(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        manc_lfc = simulate_match(poisson_model, "Man City", "Liverpool")
        
        homewin = np.sum(np.tril(manc_lfc, -1))
        awaywin = np.sum(np.triu(manc_lfc, 1))
        self.assertGreater(homewin, awaywin)

    def testLivManc(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_manc = simulate_match(poisson_model, "Liverpool", "Man City")
        
        homewin = np.sum(np.tril(lfc_manc, -1))
        awaywin = np.sum(np.triu(lfc_manc, 1))
        self.assertGreater(homewin, awaywin)

    def testManuManc(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        manu_manc = simulate_match(poisson_model, "Man United", "Man City")
        
        homewin = np.sum(np.tril(manu_manc, -1))
        awaywin = np.sum(np.triu(manu_manc, 1))
        self.assertGreater(homewin, awaywin)

    def testMancManu(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        manc_manu = simulate_match(poisson_model, "Man City", "Man United")
        
        homewin = np.sum(np.tril(manc_manu, -1))
        awaywin = np.sum(np.triu(manc_manu, 1))
        self.assertGreater(homewin, awaywin)

    def testChelEver(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        chel_eve = simulate_match(poisson_model, "Chelsea", "Everton")
        
        homewin = np.sum(np.tril(chel_eve, -1))
        awaywin = np.sum(np.triu(chel_eve, 1))
        self.assertGreater(homewin, awaywin)

    def testEverChel(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        eve_chel = simulate_match(poisson_model, "Everton", "Chelsea")
        
        homewin = np.sum(np.tril(eve_chel, -1))
        awaywin = np.sum(np.triu(eve_chel, 1))
        self.assertLess(homewin, awaywin)

    def testArsSpurs(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        ars_spurs = simulate_match(poisson_model, "Arsenal", "Tottenham")
        
        homewin = np.sum(np.tril(ars_spurs, -1))
        awaywin = np.sum(np.triu(ars_spurs, 1))
        self.assertLess(homewin, awaywin)

    def testSpursArs(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        spurs_ars = simulate_match(poisson_model,  "Tottenham", "Arsenal")
        
        homewin = np.sum(np.tril(spurs_ars, -1))
        awaywin = np.sum(np.triu(spurs_ars, 1))
        self.assertGreater(homewin, awaywin)


if __name__ == "__main__":
    unittest.main()
