# ./models/ibm-nlp.py
import os
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, RelationsOptions, ConceptsOptions

  # api keys 
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username= os.getenv('ibm_nlp_user'),
  password= os.getenv('ibm_nlp_pass'),
  version='2017-02-27')

class analyzer:
  def emotions(self, text):
    response = natural_language_understanding.analyze(
      text=text,
      features=Features(
        entities=EntitiesOptions(
          emotion=True,
          sentiment=True,
          limit=50),
        keywords=KeywordsOptions(
          emotion=True,
          sentiment=True,
          limit=50),
        relations=RelationsOptions(),
        concepts=ConceptsOptions()))

    return(json.dumps(response, indent=2))

x = analyzer()
sometxt = "Hey, man I had a bad day. I had to go to work and it sucked. The principal asked me to work on boring ass project. So boring that I wanted to kill myself."
print(x.emotions(sometxt))