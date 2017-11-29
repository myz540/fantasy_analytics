# Fantasy Football Analytics
## Author: Mike Zhong
### This repository contains the work for CS544 Foundations of Analytics for the Fall 2017 semester under Professor Suresh Kalathur.
#### Data Sources:
https://www.pro-football-reference.com/years/2016/fantasy.htm
http://www.footballdb.com/fantasy-football/index.html
#### Part 1) Data Scraping
Using the Requests and BeautifulSoup Python modules, HTML tables were scraped for the top 100 scoring fantasy football players for each week of the 2016-2017 NFL Season. The data contained in the HTML tables lacked the details and granularity desired for downstream analysis so certain columns were split into two, and other columns added. A sample table for one week was successfully scraped and parsed into the desired dataframe.
See 'bs4_and_requests.ipynb'
#### Part 2) Scripted Data Scraping and Wrangling
The above method was incorporated into a function. Utilizing query strings and the methods from Part 1, a Python script looped through  all 16 weeks and generated 16 .csv files corresponding to each week of the NFL season. The individual frames were then stacked vertically to create a massive data frame representing all 16 weeks. This data frame was then saved and will serve as the starting point for all further analyses.
See 'my_scraper.py'
#### Part 3) Analysis Performed per Project Requirements


