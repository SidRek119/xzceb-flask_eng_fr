#Language Translator
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)
#Converts English to French
def english_to_french(english_text):
    translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    json_string=json.dumps(translation, indent=2, ensure_ascii=False)
    #The below built-in function converts the JSON string into a dictionary
    json_dictionary=json.loads(json_string) 
    french_translated=[] #Empty list to extract the values in the dictionary
    for i in json_dictionary:
        french_translated.append(json_dictionary[i])
    #The below line obtains the inner dictionary which contains the translation
    translated=french_translated[0][0] 
    french_text=translated["translation"] #The translation
    return french_text
#The below code converts French to English
def french_to_english(french_text):
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    json_string=json.dumps(translation, indent=2, ensure_ascii=False)
    #The below built-in function converts the JSON string into a dictionary
    json_dictionary=json.loads(json_string) 
    english_translated=[] #Empty list to extract the values in the dictionary
    for i in json_dictionary:
        english_translated.append(json_dictionary[i])
    #The below line obtains the inner dictionary which contains the translation
    translated=english_translated[0][0] 
    english_text=translated["translation"] #The translation
    return english_text

