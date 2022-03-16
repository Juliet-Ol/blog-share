from app import app
import urllib.request,json
from app import quote

Quote = quote.Quote

# Getting the quote base url
random_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json' # app.config['RANDOM_QUOTES_URL']

def get_random_quotes():

    get_quotes_url = random_quotes_url
    
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quote_data = url.read()
        # get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'
        get_quote_response = json.loads(get_quote_data)

        if get_quote_response:

            quote_results = get_quote_response
            
        return quote_results
            

def process_results(quote_list):
    quote_results = []

    for quote_item in quote_list:
        url = quote_item.get('url')
        
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')

        quote = Quote(url, author, id, quote, permalink)

        quote_results.append(quote)

    return quote_results