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

def recipe(e):
    """prints ingredients needed for effect e"""
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

def run_program():
    print "type help for a list of commands\n"
    while True:
        cmd = raw_input("Enter a command: ")
        if cmd == "help":
            print "list (lists all ingredients)\
            \neffect (effect for <ingredient>)\
            \nsimilar (ingredients with same effect as <ingredient>)\
            \nrecipe (ingredients for <effect(s)>)\
            \nexit (exit program)"
        elif cmd == "list":
            print list_ingredients()
        elif cmd == "effect":
            i = raw_input("Enter an ingredient: \n")
            print effect(i)
        elif cmd == "similar":
            i = raw_input("Enter an ingredient: \n")
            print similar_ingredients(i)
        elif cmd == "recipe":
            e = raw_input("Enter one or more effects separated by commas: \n")
            remove_space = e.replace(', ', ',')
            split_e = remove_space.split(',')
            print recipe(split_e)
        elif cmd == "exit":
            break
        else:
            print "Not a valid command"
        print "==============================================================="
        
run_program()
