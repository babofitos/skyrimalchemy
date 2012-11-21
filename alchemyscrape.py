from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen \
    ("http://www.ign.com/wikis/the-elder-scrolls-5-skyrim/List_of_Ingredients_with_Effects")
soup = BeautifulSoup(url)
soup_tds = soup.find_all('td')
def scrape():
    """ls lists ingredients and effects if set to True"""
    output={}
    current=''
    for i in range(460):
        stripped = soup_tds[i].text.lstrip().rstrip().__str__()
        if i % 5 == 0:   
            current=stripped
        else:
            try:
                output[current].append(stripped)
            except:
                output[current] = [stripped]
    return output

def list_ingredients():
    for i in range(460):
        stripped = soup_tds[i].text.lstrip().rstrip().__str__()
        if i % 5 == 4:
            print stripped+"\n"
        else:
            print stripped
    return "Done"
