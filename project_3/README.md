# Project 3 - Elections scraper

The script is designed to scrape structured data from an HTML page and output it in a structured format (CSV). The CSV file could be usable for further analysis, allowing you to view the election data in a spreadsheet program like Excel or Google Sheets.

## Installation
Use the package manager [pip] (https://pip.pypa.io/en/stable/) to install necessary requirements.

```bash
pip install -r .\requirements.txt
```

## Usage
The main.py script is taking two arguments:
1. URL
2. Output file in csv format

```bash
python main.py \""<URL>\"" "<output_file>"
```

## Example
```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" output.csv
```

## Result of CSV Output

Below is an example of the CSV file format:

```csv
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociální demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.čsl. M.Sládka,Křesť.demokr.unie-čs.str.lid.,Česká strana národní sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529303,Benešov,13104,8485,8437,1052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
530743,Bílikovice,170,121,118,7,0,0,15,0,8,18,0,2,0,0,0,3,0,0,2,47,1,0,6,0,0,0,0,9,0
532380,Blažejovice,96,80,77,6,0,0,5,0,3,11,0,0,3,0,0,5,1,0,0,29,0,0,6,0,0,0,0,8,0
532096,Borovnice,73,54,53,2,0,0,2,0,4,4,1,0,1,0,0,3,0,0,1,29,0,0,5,0,0,0,0,1,0
