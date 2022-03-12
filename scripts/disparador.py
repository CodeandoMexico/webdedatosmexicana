import requests, os, urllib
#from wikidata.client import Client
#wikidataclient = Client()  

url = os.getenv('AIRTABLE_URL')
key = os.getenv('AIRTABLE_KEY')


def pide_todo():
    req = requests.get(url, params=key)
    if req.status_code != 200:
        print('tira un error')
        print(req.url)
    else:
        print("hizo el request a airtable")
        objs = []
        records = req.json()['records'];
        for r in records:
            fields = r['fields'];
            obj = {"wikidata": None, "api_gob": None, "qqw": None}
            if 'Wikidata' in fields:
                url_wikidata = fields['Wikidata'][0]
                obj["wikidata"] = dispara_wikidata(url_wikidata)
            if 'API Gobernantes' in fields:
                url_api_gob = fields['API Gobernantes'][0]
                obj["api_gob"] = dispara_api_gob(url_api_gob)
            if 'QQW' in fields:
                url_wikidata = fields['QQW'][0]
                obj["qqw"] = dispara_qqw(url_qqw)
        
            objs.append(obj);
        return objs


def dispara_wikidata(args):
    # todo aquí va el script de wikidata
    ##Recibe una URL
    ##Devuelve un archivo de datos (en el formato que sea) para llevar al front
    #entity = wikidataclient.get(args[0], load=True)
    #return entity
    return ""

def dispara_api_gob(args):
    # todo aquí va el script de api_gob
    ##Recibe una URL
    ##Devuelve un archivo de datos (en el formato que sea) para llevar al front
    response = urllib.request.urlopen(args)
    data = response.read()
    return data

def dispara_qqw(args):
    #Read JSON data into python
    #response = urllib2.urlopen(args[0])
    #data = json.loads(response.read()) 
    data = ""
    return data

    ##Recibe una URL
    ##Devuelve un archivo de datos (en el formato que sea) para llevar al front

# todo en dónde guardamos la info?
objs = pide_todo()
print (objs)
