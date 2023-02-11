"""
Objectives:
Use Watson APIs to create functions.
Create a function that translates English to French.
Create a function that translates French to English.
Run coding standards check against the functions above.
Write unit tests to test the above functions.
Run unit tests and interpret the results.
Package the above functions and tests as a standard python package.
"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    """
    This function takes in a string in  English and returns a string in French.
    """
    frenchtext = language_translator.translate(text=englishtext,model_id='en-fr').get_result()
    frenchtext = frenchtext.get("translations")[0].get("translation")
    return frenchtext

def frenchtoenglish(frenchtext):
    """
    This function takes in a string in French and returns a string in English.
    """
    englishtext = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    englishtext = englishtext.get("translations")[0].get("translation")
    return englishtext
