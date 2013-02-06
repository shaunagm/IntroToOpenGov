# Capitol Words API query! #

from sunlight import capitolwords
import json
import urllib

# using erin's sunlight API key 
SUNLIGHT_API_KEY = 'ce429200f22a42c68bdf8bfa611bd085'

# enter words seperated by a +
phrase = 'united+states'

#enter dates in form YYYY-MM-DD
start_date = '2012-01-01'
end_date = '2012-01-31'

BASE_URL = 'http://capitolwords.org/api/1/dates.json?'
query = BASE_URL+'phrase={phrase}&start_date={start_date}&end_date={end_date}&granularity=month&apikey={SUNLIGHT_API_KEY}'
query = query.format(phrase=phrase, start_date=start_date, end_date=end_date, SUNLIGHT_API_KEY=SUNLIGHT_API_KEY)

data = urllib.urlopen(query).read()
results = json.loads(data)

#print all the results
print results

# print the count!
print 'number of results =', results['results'][0]['count']