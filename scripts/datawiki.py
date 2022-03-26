
from __future__ import print_function
from qwikidata.sparql import return_sparql_query_results


import csv

query_string = """#List of organizations 

SELECT ?org ?orgLabel
WHERE
{
  ?org wdt:P31 wd:Q4830453. #instance of organizations
  ?org wdt:P17 wd:Q96. #Mexico country

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en"}
}"""

results = return_sparql_query_results(query_string)
print(results)

bindings = results['results']['bindings']
sparqlVars = ['org', 'orgLabel']
metaAttribute = 'value'
with open('wikidata.csv', 'w', newline='') as csvfile :
    writer = csv.DictWriter(csvfile, fieldnames=sparqlVars)
    writer.writeheader()
    for b in bindings :
        writer.writerow({var:b[var][metaAttribute] for var in sparqlVars})