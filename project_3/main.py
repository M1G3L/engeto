"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Michal Vetr
email: michal.vetr@gmail.com
discord: michalvetr
"""

import requests as re
from bs4 import BeautifulSoup

import sys
import functions as fun


if __name__ == "__main__":
    
    url = str()
    output = str() 

    if len(sys.argv) > 2:

        # check if URL and output are valid
        if not fun.is_valid_url(sys.argv[1]):
            print(f"Invalid URL: {sys.argv[1]}")
            sys.exit(1)

        elif not fun.is_valid_csv(sys.argv[2]): 
            print(f"Invalid output: {sys.argv[2]}, must be .csv file")
            sys.exit(1)

        # both URL and output are valid
        url = sys.argv[1]
        output = sys.argv[2]
        base_url = fun.get_base_url(url)

        if re.get(url).status_code == 200:
            
            # get html page
            html = re.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            cislo_tds = soup.find_all('td', class_='cislo')
            city_link_codes = fun.get_city_link_codes(cislo_tds , base_url)
            city_link_data = []

            # loop through city links 
            for code in city_link_codes:

                city_link = fun.get_city_link_data(city_link_codes, code)
                city_link_data.append(city_link)

            fun.write_data_to_file(city_link_data, output)            

    else:
        print("Not enough arguments, please try it again.")
        sys.exit(1)
