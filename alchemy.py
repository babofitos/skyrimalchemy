import alchemyscrape

def load_ingredients_file():
    f = open('ingredients.txt', 'r')
    return f

def read_ingredients_file():
    """read ingredients file and store in dict"""
    d = {}
    f = load_ingredients_file()
    key=True
    current=f.readline()
    for i,line in enumerate(f):
        strip_newline = line.rstrip()
        if strip_newline == '':
            key = False
        elif key:
            try:
                d[current].append(strip_newline)
            except:
                d[current] = [strip_newline]
        else:
            current=strip_newline
            key = True
    return d

def read_ingredients_web():
    return alchemyscrape.scrape()

def is_local():
    f = open('config.txt', 'r')
    for line in f:
        if line[0] == '#':
            pass
        else:
            if line[-1] == '0':
                return False
            return True
        
if is_local():
    print "LOADING INGREDIENTS FROM INGREDIENTS.TXT"
    READ_METHOD = read_ingredients_file()
else:
    print "LOADING INGREDIENTS FROM THE WEB"
    READ_METHOD = read_ingredients_web()

def list_ingredients():
    if is_local():
        f = load_ingredients_file()
        print f.read()
        return "\nDone"
    else:
        return alchemyscrape.list_ingredients()

def effect(i):
    """gives all effects for ingredient i"""
    #i = string, ingredient
    d = READ_METHOD
    try:
        return d[i]
    except:
        return "No such ingredient"

def similar_ingredients(i):
    """prints other ingredients that have the same effects
    as the ones in i."""
    #i = string, ingredient
    d = READ_METHOD
    print "SIMILAR INGREDIENTS:\n"
    for ingredient, effect in d.iteritems():
        for e in d[i]:
            if e in effect:
                print ingredient
                break
    return "\nEND OF SIMILAR INGREDIENTS"

def ingredients_with_effects(e):
    """prints all ingredients that have the same effects as e"""
    #e = list, effects
    d = READ_METHOD
    print "ALL INGREDIENTS WITH " + str(e) + " EFFECT(S):\n"
    for ingredient, effect in d.iteritems():
        for effects in e:
            if effects not in effect:
                break
        else:
            print ingredient
    return "\nEND OF INGREDIENTS WITH " + str(e) + " EFFECT(S)"

###examples
#print list_ingredients()
#print effect("Blue Mountain Flower")
#print similar_ingredients("Giant's Toe")
#print ingredients_with_effects(["Fortify Health", "Restore Health"])
