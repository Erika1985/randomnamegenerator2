from random import choice, randint
adjective = [ 'all-devouring', 'all-night',
'ambitious',
'animated', 'annoyed', 'annoying', 'anxious', 'appreciative', 'apprehensive', 'arrogant',
'artificial',
'average', 'awesome', 'awful', 'awkward' 'bad', 'balanced', 'barbaric', 'barbecued',
'bare-ass',
'beetle-browed', 'belated', 'believing', 'bell-bottom', 'belligerent', 'below average',
'beneficent', 'best', 'best-known', 'best-selling', 'better', 'bewildered',
'big-shouldered', 'bigheaded', 'bighearted', 'biting', 'bitter', 'biweekly', 'bizarre']
noun = ['family',
'music', 'person',
'bird', 'literature', 'problem', 'software', 'control', 'knowledge', 'power', 'ability', 
'economics', 'love', 'internet', 'television', 'science', 'library', 'nature','fact', 'product',
'idea', 'temperature','investment', 'area', 'society', 'activity','story', 'industry',
'media',

first_word = choice(adjective)
second_word = choice(noun)
first_digit = str(randint(0,10))
second_digit = str(randint(0,10)) 

username = (first_word + second_word + first_digit + second_digit)
print(username)
