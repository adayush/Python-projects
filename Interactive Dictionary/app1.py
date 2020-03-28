import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        cond = input("Did you mean %s instead? Yes[Y] or No[N]:\n" % get_close_matches(w, data.keys())[0])
        if cond == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif cond == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for _ in translate(word):
        print("&s" & _)
else:
    print(output)
