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
    count=0
    for i in range(460):
        stripped = soup_tds[i].text.lstrip().rstrip().__str__()
        if count % 5 == 0:   
            current=stripped
        else:
            try:
                output[current].append(stripped)
            except:
                output[current] = [stripped]
        count+=1
    return output

def list_ingredients():
    count=0
    for i in range(460):
        stripped = soup_tds[i].text.lstrip().rstrip().__str__()
        if count % 5 == 4:
            print stripped+"\n"
        else:
            print stripped
        count+=1
    return "Done"
