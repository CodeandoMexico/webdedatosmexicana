import requests

url = os.getenv('AIRTABLE_URL')
key = os.getenv('AIRTABLE_KEY')

def pide_todo():
    req = requests.get(url, params=data)
    if req.status_code != 200
        print('tira un error')
    else
        if req.json()['records'][0]['fields']['Wikidata']
            url_wikidata = req.json()['records'][0]['fields']['Wikidata'][0]
            dispara_wikidata(url_wikidata)
        if req.json()['records'][0]['fields']['API Gobernantes']
            url_api_gob = req.json()['records'][0]['fields']['API Gobernantes'][0]
            dispara_api_gob(url_api_gob)
        if req.json()['records'][0]['fields']['QQW']
            url_wikidata = req.json()['records'][0]['fields']['QQW'][0]
            dispara_qqw(url_qqw)

def dispara_wikidata(args):
    # todo aquí va el script de wikidata

def dispara_api_gob(args):
    # todo aquí va el script de api_gob

def dispara_qqw(args):
    # todo aquí va el script de qqw
    

# todo en dónde guardamos la info?