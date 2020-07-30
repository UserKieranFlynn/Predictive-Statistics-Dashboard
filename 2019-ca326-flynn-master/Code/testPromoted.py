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
    def testAwayLoss1(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_mid = simulate_match(poisson_model, "Liverpool", "Middlesbrough")
        lfc_hull = simulate_match(poisson_model, "Liverpool", "Hull")
        lfc_burn = simulate_match(poisson_model, "Liverpool", "Burnley")

        homewin = (np.sum(np.tril(lfc_mid, -1)) + np.sum(np.tril(lfc_hull, -1)) + np.sum(np.tril(lfc_burn, -1)))/3
        awaywin = (np.sum(np.triu(lfc_mid, 1)) + np.sum(np.triu(lfc_hull, 1)) + np.sum(np.triu(lfc_burn, 1)))/3
        self.assertGreater(homewin, awaywin)

    def testAwayLoss2(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lec_mid = simulate_match(poisson_model, "Leicester", "Middlesbrough")
        lec_hull = simulate_match(poisson_model, "Leicester", "Hull")
        lec_burn = simulate_match(poisson_model, "Leicester", "Burnley")

        homewin = (np.sum(np.tril(lec_mid, -1)) + np.sum(np.tril(lec_hull, -1)) + np.sum(np.tril(lec_burn, -1)))/3
        awaywin = (np.sum(np.triu(lec_mid, 1)) + np.sum(np.triu(lec_hull, 1)) + np.sum(np.triu(lec_burn, 1)))/3
        self.assertGreater(homewin, awaywin)

    def testAwayWin1(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        sou_mid = simulate_match(poisson_model, "Southampton", "Middlesbrough")
        sou_hull = simulate_match(poisson_model, "Southampton", "Hull")
        sou_burn = simulate_match(poisson_model, "Southampton", "Burnley")

        awaywin = (np.sum(np.triu(sou_mid, -1)) + np.sum(np.triu(sou_hull, -1)) + np.sum(np.triu(sou_burn, -1)))/3
        homewin = (np.sum(np.tril(sou_mid, -1)) + np.sum(np.tril(sou_mid, -1)) + np.sum(np.tril(sou_mid, -1)))/3
        self.assertLess(homewin, awaywin)

    def testHomeWin1(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        mid_lfc = simulate_match(poisson_model, "Middlesbrough", "Liverpool")
        hull_lfc = simulate_match(poisson_model, "Hull", "Liverpool")
        burn_lfc = simulate_match(poisson_model, "Burnley", "Liverpool")

        homewin = (np.sum(np.tril(mid_lfc, -1)) + np.sum(np.tril(hull_lfc, -1)) + np.sum(np.tril(burn_lfc, -1)))/3
        awaywin = (np.sum(np.triu(mid_lfc, 1)) + np.sum(np.triu(hull_lfc, 1)) + np.sum(np.triu(burn_lfc, 1)))/3
        self.assertLess(homewin, awaywin)

    def testHomeWin2(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        mid_sou = simulate_match(poisson_model, "Middlesbrough", "Southampton")
        hull_sou = simulate_match(poisson_model, "Hull", "Southampton")
        burn_sou = simulate_match(poisson_model, "Burnley", "Southampton")

        homewin = (np.sum(np.tril(mid_sou, -1)) + np.sum(np.tril(hull_sou, -1)) + np.sum(np.tril(burn_sou, -1)))/3
        awaywin = (np.sum(np.triu(mid_sou, 1)) + np.sum(np.triu(hull_sou, 1)) + np.sum(np.triu(burn_sou, 1)))/3
        self.assertLess(homewin, awaywin)

    def testHomeWin3(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        mid_lec = simulate_match(poisson_model, "Middlesbrough", "Leicester")
        hull_lec = simulate_match(poisson_model, "Hull", "Leicester")
        burn_lec = simulate_match(poisson_model, "Burnley", "Leicester")

        homewin = (np.sum(np.tril(mid_lec, -1)) + np.sum(np.tril(hull_lec, -1)) + np.sum(np.tril(burn_lec, -1)))/3
        awaywin = (np.sum(np.triu(mid_lec, 1)) + np.sum(np.triu(hull_lec, 1)) + np.sum(np.triu(burn_lec, 1)))/3
        self.assertLess(homewin, awaywin)

    def testPromVProm1(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        mid_hull = simulate_match(poisson_model, "Middlesbrough", "Hull")
        hull_mid = simulate_match(poisson_model, "Hull", "Middlesbrough")
        burn_mid = simulate_match(poisson_model, "Burnley", "Middlesbrough")
        mid_burn = simulate_match(poisson_model, "Middlesbrough", "Burnley")
        hull_burn = simulate_match(poisson_model, "Burnley", "Hull")
        burn_hull = simulate_match(poisson_model, "Hull", "Burnley")

        homewin = (np.sum(np.tril(mid_burn, -1)) + np.sum(np.tril(mid_hull, -1)))/2
        awaywin = (np.sum(np.triu(mid_burn, 1)) + np.sum(np.triu(mid_hull, 1)))/2
        self.assertGreater(homewin, awaywin)

    def testPromVProm2(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        mid_hull = simulate_match(poisson_model, "Middlesbrough", "Hull")
        hull_mid = simulate_match(poisson_model, "Hull", "Middlesbrough")
        burn_mid = simulate_match(poisson_model, "Burnley", "Middlesbrough")
        mid_burn = simulate_match(poisson_model, "Middlesbrough", "Burnley")
        hull_burn = simulate_match(poisson_model, "Burnley", "Hull")
        burn_hull = simulate_match(poisson_model, "Hull", "Burnley")

        homewin = (np.sum(np.tril(hull_mid, -1)) + np.sum(np.tril(hull_burn, -1)))/2
        awaywin = (np.sum(np.triu(hull_mid, 1)) + np.sum(np.triu(hull_burn, 1)))/2
        self.assertGreater(homewin, awaywin)

    def testPromVProm3(self):
        
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        mid_hull = simulate_match(poisson_model, "Middlesbrough", "Hull")
        hull_mid = simulate_match(poisson_model, "Hull", "Middlesbrough")
        burn_mid = simulate_match(poisson_model, "Burnley", "Middlesbrough")
        mid_burn = simulate_match(poisson_model, "Middlesbrough", "Burnley")
        hull_burn = simulate_match(poisson_model, "Burnley", "Hull")
        burn_hull = simulate_match(poisson_model, "Hull", "Burnley")

        homewin = (np.sum(np.tril(burn_hull, -1)) + np.sum(np.tril(burn_mid, -1)))/2
        awaywin = (np.sum(np.triu(burn_hull, 1)) + np.sum(np.triu(burn_mid, 1)))/2
        self.assertGreater(homewin, awaywin)



    def testDraw1(self):
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lfc_mid = simulate_match(poisson_model, "Liverpool", "Middlesbrough")
        lfc_hull = simulate_match(poisson_model, "Liverpool", "Hull")
        lfc_burn = simulate_match(poisson_model, "Liverpool", "Burnley")

        homewin = (np.sum(np.tril(lfc_mid, -1)) + np.sum(np.tril(lfc_hull, -1)) + np.sum(np.tril(lfc_burn, -1)))/3
        draw = (np.sum(np.diag(lfc_mid)) + np.sum(np.diag(lfc_hull)) + np.sum(np.diag(lfc_burn)))/3
        self.assertGreater(homewin, draw)


    def testDraw2(self):
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        lec_mid = simulate_match(poisson_model, "Leicester", "Middlesbrough")
        lec_hull = simulate_match(poisson_model, "Leicester", "Hull")
        lec_burn = simulate_match(poisson_model, "Leicester", "Burnley")

        homewin = (np.sum(np.tril(lec_mid, -1)) + np.sum(np.tril(lec_hull, -1)) + np.sum(np.tril(lec_burn, -1)))/3
        draw = (np.sum(np.diag(lec_mid)) + np.sum(np.diag(lec_hull)) + np.sum(np.diag(lec_burn)))/3
        self.assertGreater(homewin, draw)

    def testDraw3(self):
        results = pd.read_csv("../Data/results.csv")
        results = results[['HomeTeam','AwayTeam','FTHG','FTAG']]
        results = results.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
        results_data = pd.concat([results[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}), results[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])

        poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=results_data, family=sm.families.Poisson()).fit()

        sou_mid = simulate_match(poisson_model, "Southampton", "Middlesbrough")
        sou_hull = simulate_match(poisson_model, "Southampton", "Hull")
        sou_burn = simulate_match(poisson_model, "Southampton", "Burnley")

        awaywin = (np.sum(np.triu(sou_mid, -1)) + np.sum(np.triu(sou_hull, -1)) + np.sum(np.triu(sou_burn, -1)))/3
        draw = (np.sum(np.diag(sou_mid)) + np.sum(np.diag(sou_hull)) + np.sum(np.diag(sou_burn)))/3
        self.assertGreater(awaywin, draw)

    

if __name__ == "__main__":
    unittest.main()
