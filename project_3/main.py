"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Michal Vetr
email: michal.vetr@gmail.com
discord: michalvetr
"""

import requests as re
import csv
from bs4 import BeautifulSoup

import sys
from urllib.parse import urlparse


def is_valid_url(url) -> bool:
    """Checks if URL is valid"""
    parse_url = urlparse(url)
    return all([parse_url.scheme, parse_url.netloc, parse_url.path])

def is_valid_csv(output) -> bool:
    """Checks if output is valid"""
    if output.endswith(".csv"):
        return True
    else:
        return False

def get_base_url(url: str) -> str:
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the base part (scheme + netloc + path up to the last '/')
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{'/'.join(parsed_url.path.split('/')[:-1])}/"
    
    return base_url

def get_city_link_codes(data: object) -> dict:
    city_link_codes = {}

    for td in data:
        link_tag = td.find('a')
        link = link_tag['href']  # Extract the href attribute (link)
        city_number = link_tag.text  # Extract the city number (text in <a>)
        link = base_url + link

        # create dictionary with city number and link
        city_link_codes[city_number] = link
    
    return city_link_codes

def get_data_by_header(soup, headers: str) -> str:
    value = soup.find('td', class_='cislo', headers=headers)
    if value:
        result = value.get_text().replace('\xa0', '')
        numeric_value = int(result)

        return numeric_value


def get_table_data(soup):

    tables = [table for table in soup.find_all('table', class_='table') if not table.get('id')]
    
    # Initialize a list to store results
    party_data = []

    # Iterate through each table
    for i, table in enumerate(tables):
        # Loop through each row in the current table (skipping header rows)
        for row in table.find_all('tr')[2:]:
            columns = row.find_all('td')
            if columns:
                name = columns[1].text.strip()
                votes = columns[2].text.strip().replace('\xa0', '')
                
                # Append row data to the current table's list
                party_data.append({
                    'name': name,
                    'votes': votes,
                })

    return party_data

def get_city_link_data(city_link_codes, code) -> dict:

    html = re.get(city_link_codes[code]).text
    soup = BeautifulSoup(html, 'html.parser')
    location = soup.find('h3', string=lambda x: x and "Obec" in x).text

    city_link = {}

    city_link['code'] = code
    
    # split city name in to dictionary
    location = location.split(":")
    location = location[1].strip()
    city_link['location'] = location

    # registered in list
    registered = get_data_by_header(soup, 'sa2')
    city_link['registered'] = registered

    # envelopes
    envelopes = get_data_by_header(soup, 'sa3')
    city_link['envelopes'] = envelopes
    
    # valid
    valid = get_data_by_header(soup, 'sa6')
    city_link['valid'] = valid

    # get table data
    party_data = get_table_data(soup)

    for party in party_data:
        city_link[party['name']] = party['votes']

    return city_link
def write_data_to_file(data, file_path):

    with open(file_path, mode='w', newline='') as file:
    # Create a CSV DictWriter object, using the keys of the first dict as fieldnames
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        
        # Write the header row
        writer.writeheader()
        
        # Write each dictionary as a row in the CSV file
        writer.writerows(data)


if __name__ == "__main__":
    
    url = str()
    output = str() 

    if len(sys.argv) > 2:

        # check if URL and output are valid
        if not is_valid_url(sys.argv[1]):
            print(f"Invalid URL: {sys.argv[1]}")
            sys.exit(1)

        elif not is_valid_csv(sys.argv[2]): 
            print(f"Invalid output: {sys.argv[2]}, must be .csv file")
            sys.exit(1)

        # both URL and output are valid
        url = sys.argv[1]
        output = sys.argv[2]
        base_url = get_base_url(url)

        if re.get(url).status_code == 200:
            
            # get html page
            html = re.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            cislo_tds = soup.find_all('td', class_='cislo')
            city_link_codes = get_city_link_codes(cislo_tds)
            city_link_data = []

            # loop through city links 
            for code in city_link_codes:

                city_link = get_city_link_data(city_link_codes, code)
                city_link_data.append(city_link)

            write_data_to_file(city_link_data, output)

                    

    else:
        print("Not enough arguments, please try it again.")
        sys.exit(1)
