from bs4 import BeautifulSoup
import urllib2

class Scraper:
    def __init__(self):
        self.url = urllib2.urlopen \
            ("http://www.uesp.net/wiki/Skyrim:Ingredients")
        soup = BeautifulSoup(self.url)
        self.soup_td = soup.find("table", class_="wikitable").find_all("td")
        
    def print_ingredients(self):
        for i in range(1, len(self.soup_td)):
            if i % 10 == 1:
                print self.soup_td[i].a.text

    def print_effects(self):
        for i in range(2, len(self.soup_td)):
            if i % 10 == 3 or i % 10 == 4 or i % 10 == 5 or i % 10 == 6:
                print self.soup_td[i].a['title']

    def create_list(self):
        output={}
        current=''
        for i in range(1, len(self.soup_td)):
            if i % 10 == 1:
                current=self.soup_td[i].a.text.__str__()
            elif i % 10 == 3 or i % 10 == 4 or i % 10 == 5 or i % 10 == 6:
                try:
                    output[current].append(self.soup_td[i].a['title'].__str__())
                except:
                    output[current] = [self.soup_td[i].a['title'].__str__()]
        return output

class Commands:
    def __init__(self):
        self.data = Scraper()
        
    def list_ingredients(self):
        return self.data.print_ingredients()

    def list_effects(self):
        return self.data.print_effects()

    def effect(self,i):
        """gives all effects for ingredient i"""
        #i = string, ingredient
        d = self.data.create_list()
        try:
            return d[i]
        except:
            return "No such ingredient"

    def similar_ingredients(self,i):
        """prints other ingredients that have the same effects
        as the ones in i."""
        #i = string, ingredient
        d = self.data.create_list()
        print "SIMILAR INGREDIENTS:\n"
        for ingredient, effect in d.iteritems():
            for e in d[i]:
                if e in effect:
                    print ingredient
                    break
        return "\nEND OF SIMILAR INGREDIENTS"

    def recipe(self,e):
        """prints ingredients needed for effect e"""
        #e = list, effects
        d = self.data.create_list()
        print "ALL INGREDIENTS WITH " + str(e) + " EFFECT(S):\n"
        for ingredient, effect in d.iteritems():
            for effects in e:
                if effects not in effect:
                    break
            else:
                print ingredient
        return "\nEND OF INGREDIENTS WITH " + str(e) + " EFFECT(S)"

def run_program(cmd):
    print "type help for a list of commands\n"
    while True:
        q = raw_input("Enter a command: ")
        if q == "help":
            print "list ingredients (lists all ingredients)\
            \nlist effects (lists all effects)\
            \neffect (effect for <ingredient>)\
            \nsimilar (ingredients with same effect as <ingredient>)\
            \nrecipe (ingredients for <effect(s)>)\
            \nexit (exit program)"
        elif q == "list ingredients":
            print cmd.list_ingredients()
        elif q == "list effects":
            print cmd.list_effects()
        elif q == "effect":
            i = raw_input("Enter an ingredient: \n")
            print cmd.effect(i)
        elif q == "similar":
            i = raw_input("Enter an ingredient: \n")
            print cmd.similar_ingredients(i)
        elif q == "recipe":
            e = raw_input("Enter one or more effects separated by commas: \n")
            remove_space = e.replace(', ', ',')
            split_e = remove_space.split(',')
            print cmd.recipe(split_e)
        elif q == "exit":
            break
        else:
            print "Not a valid command"
        print "==============================================================="
        
run_program(Commands())
