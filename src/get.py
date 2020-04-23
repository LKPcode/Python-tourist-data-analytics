
import requests
import os
from bs4 import BeautifulSoup


#Get html Files
def download_html_files():
    for year in range(2011 ,2015):
        if not os.path.exists("./html/" + str(year) + "/"):
            os.makedirs(os.path.dirname( "./html/" + str(year) + "/"))
        for trimino in range(1 , 5):
            #Create URLs to download the html pages
            url =  str(year) + "-Q" + str(trimino) 
            print("Downloading HTML: " + url)
            
            #Download the html pages
            html = 'https://www.statistics.gr/el/statistics/-/publication/STO04/' + url
            r = requests.get(html, allow_redirects=True)

            #save it in its coresponding folder
            open('./html/' + str(year)  + '/' + str(trimino) + '.html', 'wb').write(r.content)


#Get Excel files
def download_excel_files():
    for year in range(2011 ,2015):
        for trimino in range(1 , 5):
            if not os.path.exists("./excel/" + str(year) + "/" + str(trimino) + "/" ):
                #make folders if they do not exist
                os.makedirs(os.path.dirname( "./excel/" + str(year) + "/" + str(trimino) + "/" ))
            
            #Parse html and get URLs for excel files
            soup = BeautifulSoup(open("./html/" + str(year) + "/" + str(trimino) + ".html", encoding='utf8'), 'html.parser')
            href = soup.findAll("table", {"class": "documentsTable"})[2].find_all("a")[2]["href"]
            print("Downloading excel file for year :" + str(year) + " and trimester: " + str(trimino))

            #Download the excel files
            excel = href
            r = requests.get(excel, allow_redirects=True)
            
            #save them in their coresponding folder
            open('./excel/' + str(year)  + '/' + str(trimino) + "/" +  '1.xls', 'wb').write(r.content)
