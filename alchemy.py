def load_ingredients_file():
    f = open('ingredients.txt', 'r')
    return f

def read_ingredients():
    """read ingredients file and store in dict"""
    d = {}
    f = load_ingredients_file()
    for line in f:
        read_line = line.rstrip().split(':')
        key = read_line[0]
        val = read_line[1].split(',')
        d[key] = val
    return d

def list_all_ingredients():
    f = load_ingredients_file()
    print f.read()

def effect(i):
    """gives all effects for ingredient i"""
    #i = string, ingredient
    d = read_ingredients()
    try:
        return d[i]
    except:
        return "No such ingredient"

def similar_ingredients(i):
    """prints other ingredients that have the same effects
    as the ones in i."""
    #i = string, ingredient
    d = read_ingredients()
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
    d = read_ingredients()
    print "ALL INGREDIENTS WITH " + str(e) + " EFFECT(S):\n"
    for ingredient, effect in d.iteritems():
        for effects in e:
            if effects not in effect:
                break
        else:
            print ingredient
    return "\nEND OF INGREDIENTS WITH " + str(e) + " EFFECT(S)"

###examples
#print list_all_ingredients()
#print effect("Blue Mountain Flower")
#print similar_ingredients("Giant's Toe")
#print ingredients_with_effects(["Fortify Health", "Restore Health"])
