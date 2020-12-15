import json
from difflib import  get_close_matches
data = json.load(open("data.json")) #opening the json file containing data for dictionary
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0: #
        yn = input(f'Did you mean {get_close_matches(w, data.keys())[0]} Enter y for Yes and n for No: ') #since indexing to 0 we only grabs the first possiility
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The Word You entered doesn't exist"
        else:
            return "unable to understand the word you entered"
    else:
        return "the word doesn't exist on the db"
word = input('Enter the word: ')
output = translate(word)
if type(output) == list:
    #inorder to display the list as text instead of a list
    for item in output:
        print(item)
else:
    print(output)
