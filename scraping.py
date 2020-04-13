import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

while True:
	url = "https://sportsbook.draftkings.com/leagues/football/3?category=game-lines&subcategory=game"

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
	req = Request(url, headers=headers)
	html = urlopen(req)
	soup = BeautifulSoup(html, "lxml")

	spans = soup.findAll("span", attrs = {"class" : ["event-cell__name", "sportsbook-outcome-cell__line", 
	                                                 "sportsbook-odds american default-color", "event-cell__time",
	                                                 "event-cell__period", "event-cell__score"]}) 

	games = []
	team_count = 0
	new_spans = []
	for s in spans:
	    # check if it's a new game, i.e. a team name
	    if s.attrs["class"][0] == "event-cell__name":
	        team_count += 1
	        if team_count == 3:
	            break
	    new_spans.append(s.text)

	new_spans.append("\n")
	    
	with open('week9.csv', 'a') as f:
	    writer = csv.writer(f)
	    writer.writerow(new_spans)
	f.close()

	print(time.time())

	time.sleep(60)