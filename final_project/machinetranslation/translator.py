'''Project to convert french text to english and vice-versa using watson API'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#instance of IBM Watson Language Translation
authenticator = IAMAuthenticator('7dtp2gXAfAqHiMNYsHolyJhgSd5W0_7r6PLYK76YSDXp')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6a76f247-2085-43ed-8df8-73edd2733993')

def english_to_french(english_text):
    '''Function to translate english text to French'''
    french_text = language_translator.translate(
        text = english_text,
        model_id = 'en-fr',
        source = 'en',
        target = 'fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    french_text=french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Function to translate French text to English'''
    english_text = language_translator.translate(
        text = french_text,
        model_id = 'fr-en',
        source = 'fr',
        target = 'en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    english_text=english_text['translations'][0]['translation']
    return english_text
