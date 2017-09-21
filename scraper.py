from bs4 import BeautifulSoup
import requests
import pandas as pd


class Scraper():

    def __init__(self, base_url):
        self.url_base = base_url
        self.soup = None
        self.url_options = {}

    def build_url(self, base_url, year, week, pos_string, rules):
        pass

    def parse_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'lxml')
            return [(table['id'], self.parse_html_table(table)) for table in soup.find_all('table')]
        else:
            raise BaseException("Response returned status code:", response.status_code)
            exit(1)

    def parse_html_table(self, table):
        nrow = 0
        ncol = 0
        col_names = []

        # iterate over all table rows
        for tr_tag in table.find_all('tr'):

            td_tags = tr_tag.find_all('td')

            if len(td_tags) > 0:
                nrow += 1

                if ncol == 0:
                    # set number of columns based on the number of td tags in the header
                    ncol = len(td_tags)

            th_tags = tr_tag.find_all('th')

            if len(th_tags) > 0 and len(col_names) == 0:
                for th in th_tags:
                    col_names.append(th.get_text())


base_url = "http://www.footballdb.com/fantasy-football/index.html?"
# rules = 1 for standard, 2 for ppr
rules = "2"
# year
year = "2017"
# week = 1 - 16
week = "2"

sample_url = "http://www.footballdb.com/fantasy-football/index.html?pos=QB%2CRB%2CWR%2CTE&yr=2016&wk=1&rules=2"

response = requests.get(sample_url)

#print(response)
#print(response.status_code)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.table)
table = soup.table





