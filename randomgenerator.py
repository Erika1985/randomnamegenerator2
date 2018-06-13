from random import choice, randint
adjective = [ 'all-devouring', 'all-night','all-round', 'alluring', 'amazed', 'amazing',
'ambitious','amiable', 'amicable', 'amused', 'amusing', 'ancient', 'angelic', 'angry',
'animated', 'annoyed', 'annoying', 'anxious', 'appreciative', 'apprehensive', 'arrogant',
'artificial','artistic', 'ashamed','assertive','attentive','attracted', 'attractive',
'average', 'awesome', 'awful', 'awkward' 'bad', 'balanced', 'barbaric', 'barbecued',
'bare-ass','bare-assed', 'bean-shaped','beatable', 'beaten', 'beautiful', 'beefed-up',
'beetle-browed', 'belated', 'believing', 'bell-bottom', 'belligerent', 'below average',
'beneficent', 'best', 'best-known', 'best-selling', 'better', 'bewildered','big',
'big-shouldered', 'bigheaded', 'bighearted', 'biting', 'bitter', 'biweekly', 'bizarre']
noun = ['family','government', 'health','system', 'computer','meat','year', 'thanks'
'music', 'person','reading', 'method', 'data', 'food','understanding','theory''law',
'bird', 'literature', 'problem', 'software', 'control', 'knowledge', 'power', 'ability', 
'economics', 'love', 'internet', 'television', 'science', 'library', 'nature','fact', 'product',
'idea', 'temperature','investment', 'area', 'society', 'activity','story', 'industry',
'media','thing','oven','community','definition','safety']

first_word = choice(adjective)
second_word = choice(noun)
first_digit = str(randint(0,10))
second_digit = str(randint(0,10)) 

username = (first_word + second_word + first_digit + second_digit)
print(username)

