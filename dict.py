import json
import difflib
from difflib import *

datae=json.load(open('data.json'))
def translate(word):

    if word in datae:
        return datae[word]

    elif word !='x':
        if len(get_close_matches(word,datae.keys()))>0:
            yn=input("Did you mean %s instead? Enter Y is yes or N if no:" % get_close_matches(word,datae.keys())[0])
            if yn=='y':
                return datae[get_close_matches(word,datae.keys())[0]]
            elif yn=='n':
                return 'word doesnot exist please cross verify'
            else:
                return 'sorry!!we did not understand your entry'
    else:
        exit()
wordd = ''
while wordd !='x':
    if wordd=='x':
        break
    else:
        if wordd=='x':
            break
        else:
            wordd = input('enter a word')
            wordd = wordd.lower()
            wordd=translate(wordd)
            if type(wordd)==list:
                for i in wordd:
                    print(i)
            else:
                print(wordd)