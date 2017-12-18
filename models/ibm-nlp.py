# ./models/ibm-nlp.py
import os
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

# api keys 
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username= os.getenv('ibm_nlp_user'),
  password= os.getenv('ibm_nlp_pass'),
  version='2017-02-27')

#

response = natural_language_understanding.analyze(
  text='ISO 639-1 code indicating the language to use for the analysis. This code overrides the automatic language detection performed by the service. Valid codes are ar (Arabic), en (English), fr (French), de (German), it (Italian), pt (Portuguese), ru (Russian), es (Spanish), and sv (Swedish). For more information about which features are supported in each language, se',
  features=Features(
    entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2)))

print(json.dumps(response, indent=2))