# ./app.py
from google.cloud import language 
from google.cloud.language import types
from google.cloud.language import enums


def language_analysis(doc):
	client = language.LanguageServiceClient()
	sent_analysis = client.analyze_sentiment(document=doc).document_sentiment
	ent_analysis = client.analyze_entities(document=doc).document_entities
	

	return sent_analysis.score

text = 'I love you'

document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)



print(language_analysis(document))



# Analizes massages

# Symantic analysis

# Category analysis 

# Sentiment analysis	 