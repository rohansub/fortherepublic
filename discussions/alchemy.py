from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='f31c888075ffa4d4014b930551da5e1435435110')

## returns an  array with concepts and relevance number (max 3). lol, not really, actually returns a lot more than that. Details here: https://www.ibm.com/watson/developercloud/alchemy-language/api/v1/?python#date_extraction
def returnConcepts (issue):
	return alchemy_language.concepts(text=issue, max_items = 3, linked_data = 0)

## returns an array with taxonomy and relevance number
def returnTaxonomy (issue):
	return alchemy_language.taxonomy(text=issue)

def returnSentiment (issue):
	return alchemy_language.sentiment(text=issue)

##testing
#issue1 = "Healthcare is spiraling out of control in this country."
#issue2 = "Abortion is ruining the United States. We must outlaw this despicable practice!"

#print returnConcepts(issue1)
#print ("\n")
#print returnConcepts(issue2)["concepts"]
#print ("\n")
#print returnTaxonomy(issue1)
#print ("\n")
#print returnTaxonomy(issue2)
#print ("\n")
