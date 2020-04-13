# Predicting NFL In-Game Win Probabilities

Our goal is to develop a model for in-game win probability for American football games. The code in this repository uses logistic regression, random forests, and k-nearest neighbor regression, taking into account factors such as current score, ball possession, field position, and the two teams' skill difference, to predict win probability. 

## Description of most relevant files

* nfl-elo-game-master: data/nfl_games.csv contains ELO rating data for all past NFL games from FiveThirtyEight
* nfl-score-and-betting-data: self-explanatory, contains historical NFL betting data (spread, over/under) from Kaggle
* elo stuff.ipynb: cleans the FiveThirtyEight and Kaggle data, combines it into one data frame, compares Elo ratings, QB-adjusted ELO ratings, and spread
* clean logistic.ipynb: logistic regression models
* random forests.ipynb: random forest regression models
* k nearest neighbors.ipynb: k nearest neighbor regression models
* logistic with time dependent coefficients.ipynb: time-dependent logistic regression models
