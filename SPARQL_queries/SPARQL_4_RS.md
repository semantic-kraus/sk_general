# SPARQL for ResearchSpace

## TOC
- [Person Biographical](#person-biographical)
    - [Birth Date](#birth-date)
    - [Birth Place](#birth-place)
    - [Death Date](#death-date)
    - [Death Place](#death-place)
    - tbd: Events
    - [Occupation](#occupation)
    - [Party Affiliations](#party-affiliation)
    - tbd: Legal Activities
    - tbd: Data Provenance
- [Person Textual](#person-textual)
    - tbd: [Person Mentions](#person-mentions)
    - tbd: [Person Authorship](#person-authorship)
- Person References


## Person

### Person Biographical

#### Birth Date
Selects label of birth's time-span.

https://sk.acdh-dev.oeaw.ac.at/fieldDefinition/birth_date
```
SELECT ?value WHERE { 
?person crm:P98i_was_born ?birth_event. 
?birth_event crm:P4_has_time-span ?timespan. 
?timespan rdfs:label ?value.
 } 
```


#### Birth Place 

https://www.researchspace.org/fieldDefinition/birth_place
```
SELECT ?value ?label WHERE { 
$subject crm:P98i_was_born ?birth_event. 
?birth_event crm:P7_took_place_at ?value. 
?value rdfs:label ?label. } 
```
#### Death Date
Selects death's time span label.

https://sk.acdh-dev.oeaw.ac.at/death_date
```
SELECT ?value WHERE { 
$subject crm:P100i_died_in ?death_event.
?death_event crm:P4_has_time-span ?timespan. 
?timespan rdfs:label ?value.
 } 
 ```
#### Death Place 

https://sk-app.acdh.oeaw.ac.at/fieldDefinition/death_place 

```
SELECT ?value ?label WHERE { 
  $subject crm:P100i_died_in ?death_event. 
  ?death_event crm:P7_took_place_at ?value. 
  ?value rdfs:label ?label. 
} 
```
#### Occupation
Selects pursuit label as well as, if available, time-span label and employer label (the employer being modeled as the period of its existence).

https://sk.acdh-dev.oeaw.ac.at/fieldDefinition/occupation

```
SELECT ?value ?timespanLabel ?instLabel WHERE { 
$subject crm:P14i_performed ?pursuit.
?pursuit a frbroo:F51_Pursuit.
?pursuit rdfs:label ?value.
      OPTIONAL {
?pursuit crm:P4_has_time-span ?timespan.
  ?timespan rdfs:label ?timespanLabel.
}
      OPTIONAL {
?pursuit crm:P10_falls_within ?inst.
  ?inst rdfs:label ?instLabel.
}
 } 
 ```
 
#### Party Affiliation
Selects party label as well as joining and leaving date labels

https://sk.acdh-dev.oeaw.ac.at/fieldDefinition/affiliation
```
SELECT ?value ?fromLabel ?toLabel WHERE { 
$subject crm:P143i_was_joined_by ?joining.
?joining crm:P144_joined_with ?group.
  ?group rdfs:label ?value.
  OPTIONAL {
?joining crm:P4_has_time-span ?timespan.
  ?timespan rdfs:label ?fromLabel.
  }
  OPTIONAL {
$subject crm:P145i_left_by ?leaving.
    ?leaving crm:P146_separated_from ?group.
    ?leaving crm:P4_has_time-span ?timespan.
  ?timespan rdfs:label ?toLabel.
  }
 } 
 ```
 


### Person Textual
#### Person Mentions
##### (passage, passage label, text label:)

https://sk.acdh.oeaw.ac.at/fieldDefinition/pers_mentions

``` 
SELECT ?value ?label ?textlabel WHERE {  
$subject crm:P67i_is_referred_to_by ?reference . 
?reference <https://w3id.org/lso/intro/beta202210#R17_feature_actualized_in> ?actualization .
?actualization <https://w3id.org/lso/intro/beta202210#R18_actualization_found_on> ?value . 
?value rdfs:label ?label .
?value <https://w3id.org/lso/intro/beta202210#R10_is_Text_Passage_of> ?text .
?text rdfs:label ?textlabel .}
```
#### Person Authorship
