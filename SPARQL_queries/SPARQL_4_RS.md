# SPARQL for ResearchSpace

## Field Definitions 

### Person

#### Birth Date - tbc
#### Birth Place 

https://www.researchspace.org/fieldDefinition/birth_place
```
SELECT ?value ?label WHERE { 
$subject crm:P98i_was_born ?birth_event. 
?birth_event crm:P7_took_place_at ?value. 
?value rdfs:label ?label. } 
```
#### Death Date - tbc
#### Death Place 

https://sk-app.acdh.oeaw.ac.at/fieldDefinition/death_place 

```
SELECT ?value ?label WHERE { 

  $subject crm:P100i_died_in ?death_event. 

  ?death_event crm:P7_took_place_at ?value. 

  ?value rdfs:label ?label. 

} 
```

#### Person mentions

"https://sk.acdh.oeaw.ac.at/fieldDefinition/pers_mentions", 
``` 
SELECT ?value ?label ?textlabel WHERE {  
$subject crm:P67i_is_referred_to_by ?reference . 
?reference <https://w3id.org/lso/intro/beta202210#R17_feature_actualized_in> ?actualization .
?actualization <https://w3id.org/lso/intro/beta202210#R18_actualization_found_on> ?value . 
?value rdfs:label ?label .
?value <https://w3id.org/lso/intro/beta202210#R10_is_Text_Passage_of> ?text .
?text rdfs:label ?textlabel .}

```
