# create dictionary of the hello and its orgin
# case one
# create an endless loop
# take input of string
# check if string has a key in dictionary and output appropriately
#if not, print ("unknown")
# increment case
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ _


catalog = {"HALLO" : "GERMAN", "BONJOUR" : "FRENCH", "CIAO" : "ITALIAN", "ZDRAVSTVUJTE" : "RUSSIAN", "HELLO" : "ENGLISH", "HOLA" : "SPANISH"}
case = 1
while True:
    string = str(input())
    if string == "#":
        break
    if string in catalog:
        print ("Case {}: {}".format(case,catalog[string])) 
    else:
        print("Case {}: UNKNOWN".format(case))
    case += 1
        

