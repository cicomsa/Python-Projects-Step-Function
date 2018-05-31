import json
import requests

class Error(Exception):
    pass
class WrongInput(Error):
    pass
    
source = 'en'
text = input("Translate from English: ")
while text.isalpha() == False:
    try:
        raise WrongInput(text)
    except WrongInput:
        print("Words to include only letters. Please try again!")
        text = input("Translate from English: ")
        
target = input("To 'Spanish', 'French', 'Portuguese' or 'Arabic': ")
while True: 
    try:
        if target.title() == 'Spanish':
            target = 'es'
            break
        elif target.title() == 'French'.title():
            target = 'fr'
            break
        elif target.title() == "Portuguese".title():
            target = 'pt'
            break
        elif target.title() == "Arabic".title():
            target = 'ar'
            break
        else:
            raise WrongInput(target)
    except WrongInput:
        print("Wrong input! Please type 'Spanish', 'English', 'French' or 'Portuguese' for the desired language in which text to be translated in.")
        target = input("To 'Spanish', 'English', 'French' or 'Portuguese': ") 
            
            
    
username = "USERNAME" 
password = "PASSWORD" 
url = "https://gateway.watsonplatform.net/language-translator/api/v2/translate"
query_string = {"text":text,"model_id":"{0}-{1}-conversational".format(source,target)}
    
    
def translate():
    response = requests.get(url,auth=(username, password),params=query_string)
    return response


while True:
    try:
        translate()
        status = translate().reason
        if status == "OK":
            print(translate().text)
            break
        elif status != "OK":
            raise WrongInput(text)
    except WrongInput:
        print("Error: Something went wrong. Please check for errors!")
        break