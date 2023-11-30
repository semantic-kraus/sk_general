from SPARQLWrapper import SPARQLWrapper, JSON
import os
import json


USER = os.environ.get('SK_USER')
PSSWD = os.environ.get('SK_PSSWD')

sparql = SPARQLWrapper("https://triplestore.acdh-dev.oeaw.ac.at/sk/sparql")
sparql.setCredentials(user=USER, passwd=PSSWD)
sparql.setReturnFormat(JSON)

# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
# sparql.setQuery("""
# PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX sk: <https://sk.acdh.oeaw.ac.at/project/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

# SELECT DISTINCT ?eThisGraph ?eOtherGraph ?thisGraph ?otherGraph
# WHERE {
  
#   FILTER (?thisGraph IN (sk:dritte-walpurgisnacht , sk:legal-kraus, sk:fackel ))
  
#   GRAPH ?thisGraph {
#     ?eThisGraph a ?entity_type ;
#               crm:P1_is_identified_by ?identifier .
#                 FILTER (?entity_type IN (crm:E21_Person , crm:E53_Place))
#     ?identifier a crm:E42_Identifier ;
#                   rdf:value ?value ;
#                   crm:P2_has_type ?type .
#                   FILTER (?type IN (<https://sk.acdh.oeaw.ac.at/types/idno/URL/wikidata>, <https://sk.acdh.oeaw.ac.at/types/idno/URL/gnd> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/pmb> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/fackel> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/geonames> ) )                                                                                                                                                                                                
#   }
#   GRAPH ?otherGraph {
#     ?eOtherGraph a ?entity_type2 ;
#               crm:P1_is_identified_by ?identifier2 .
#             FILTER (?entity_type2 IN (crm:E21_Person , crm:E53_Place))
#     ?identifier2 a crm:E42_Identifier ;
#                   rdf:value ?value2 ;
#                   crm:P2_has_type ?type2 .
#                   FILTER (?type2 IN (<https://sk.acdh.oeaw.ac.at/types/idno/URL/wikidata>, <https://sk.acdh.oeaw.ac.at/types/idno/URL/gnd> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/pmb> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/fackel> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/geonames> ) )                                                                                                                                                                                                
#   }
#   FILTER (?type = ?type2 && ?value = ?value2)
#   FILTER (?thisGraph != ?otherGraph)
# }

# """
# )

sparql.setQuery("""
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sk: <https://sk.acdh.oeaw.ac.at/project/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?eThisGraph ?thisGraph ?identifier ?value ?type
WHERE {
  
  FILTER (?thisGraph IN (sk:dritte-walpurgisnacht , sk:legal-kraus, sk:fackel ))
  
  GRAPH ?thisGraph {
    ?eThisGraph a ?entity_type ;
              crm:P1_is_identified_by ?identifier .
                FILTER (?entity_type IN (crm:E21_Person , crm:E53_Place))
    ?identifier a crm:E42_Identifier ;
                  rdf:value ?value ;
                  crm:P2_has_type ?type .
                  FILTER (?type IN (<https://sk.acdh.oeaw.ac.at/types/idno/URL/wikidata>, <https://sk.acdh.oeaw.ac.at/types/idno/URL/gnd> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/pmb> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/fackel> , <https://sk.acdh.oeaw.ac.at/types/idno/URL/geonames> ) )                                                                                                                                                                                                
  }
}

"""
)

try:
    ret = sparql.queryAndConvert()
    with open("query_dump.json", "w") as f:
        json.dump(ret, f, indent=2)
except Exception as e:
    print(e)