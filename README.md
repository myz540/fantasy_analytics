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
The above method was incorporated into a function. Utilizing query strings and the methods from Part 1, a Python script looped through  all 16 weeks and generated 16 .csv files corresponding to each week of the NFL season. The individual frames were then stacked vertically to create a massive data frame representing all 16 weeks. The initial data frame lacks position information for each player, an attribute that will eventually be used to stratify the population for sampling means. As such, this was considered necessary information that needed to be filled in. A separate data frame was roughly scraped from a separate website containing two columns, the player name and position. An inner join was performed on the two tables using the player name as the key. This merged data frame was then saved and will serve as the starting point for all further analyses.
See 'my_scraper.py'
#### Part 3) Cleaning Data and Filling Missing Values
The data frame from part 2 was inspected for missing values. Several players were missing their position column value due to inconsistent naming between the data sources, use of nicknames, or as a result of the parsing schema. Due to my knowledge of the NFL, the 5 missing players' positions were added manually to the data frame. 
See 'fill_player_pos.ipynb'
#### Part 4) Analysis Performed per Project Requirements
The following analysis was performe: Examine two categorical variables and visualize distributions, examine one continuous variable and visualize distributions, then stratify the data by one of the categorical variables and examine the distribution of the continuous variable. Next, explore simple random sampling and stratified sampling methods, illustrate the central limit theorem. Compare means and standard deviations with the population. Lastly, use the boot library to generate bootstrap distributions of resampled means and medians, computing 90% and 80% confidence intervals for both statistics. 
See 'R_Analysis1.ipynb'
#### Part 5) Additional Analysis Performed But Not Required By Project, this work is ongoing...
See 'R_Analysis2.ipynb'


