# SPARQL for ResearchSpace

## TOC
### Entry/Search - tbd
### Results - tbd
### [Person Page](#person)
#### [Person Data Box](#person-data-box)

- [tbd: Birth Date](#birth-date)
- [tbd: Birth Place](#birth-place)
- [tbd: Death Date](#death-date)
- [tbd: Death Place](#death-place)
- [tbd: Life Events](#life-events)
- [tbd: Occupation](#occupation)
- [tbd: Party Affiliations](#party-affiliation)

#### [Person Text Box](#person-text-box)
- [tbd: Authored Texts](#authored-texts)

#### [Person Mentions Box](#person-mentions-box)
- [tbd: Person Mentions](#person-mentions)


## Preface
All queries must be (re-)designed to meet the following criteria: 
- For all the central entities (F22, F24, E21), equivalents might exist in other named graphs. Every query has to give all the results relating to instances of this entity in all named graphs (e.g.: a person's date of birth, but also the date of birth of the equivalent person in another named graph).
- All of these query results must come with their named graph's metadata. 

This document is structured according to the SK_First_MockUp PDF file.

## Entry/Search - tbd
## Results - tbd
## Person

### Person Data Box 

#### Birth Date
Select time-span of birth of context-person as well as of persons linked to context-person via owl:sameAs.

Add named graph URI to every result.

- [ ] Query
- [ ] Knowledge Pattern
- [ ] Implemented

Query:
```
(tbd)
```

(outdated:)

~~https://sk.acdh-dev.oeaw.ac.at/fieldDefinition/birth_date~~
```
SELECT ?value WHERE { 
?person crm:P98i_was_born ?birth_event. 
?birth_event crm:P4_has_time-span ?timespan. 
?timespan rdfs:label ?value.
 } 
```


#### Birth Place 

Select place of birth of context-person as well as of persons linked to context-person via owl:sameAs.

Add named graph URI to every result.

- [ ] Query
- [ ] Knowledge Pattern
- [ ] Implemented

Query:
```
(tbd)
```


(outdated:)

~~https://www.researchspace.org/fieldDefinition/birth_place~~
```
SELECT ?value ?label WHERE { 
$subject crm:P98i_was_born ?birth_event. 
?birth_event crm:P7_took_place_at ?value. 
?value rdfs:label ?label. } 
```

#### Death Date

Select date of death of context-person as well as of persons linked to context-person via owl:sameAs.

Add named graph URI to every result.

- [ ] Query
- [ ] Knowledge Pattern
- [ ] Implemented

Query:
```
(tbd)
```


(outdated:)

~~https://sk.acdh-dev.oeaw.ac.at/death_date~~
```
SELECT ?value WHERE { 
$subject crm:P100i_died_in ?death_event.
?death_event crm:P4_has_time-span ?timespan. 
?timespan rdfs:label ?value.
 } 
 ```
#### Death Place 
Select place of death of context-person as well as of persons linked to context-person via owl:sameAs.

Add named graph URI to every result.

- [ ] Query
- [ ] Knowledge Pattern
- [ ] Implemented

Query:
```
(tbd)
```


(outdated:)

~~https://sk-app.acdh.oeaw.ac.at/fieldDefinition/death_place~~ 

```
SELECT ?value ?label WHERE { 
  $subject crm:P100i_died_in ?death_event. 
  ?death_event crm:P7_took_place_at ?value. 
  ?value rdfs:label ?label. 
} 
```


#### Life Events
Selects life event labels and timespan labels.

(Life events cover events like deportation, burial, gone missing, etc.)

https://sk.acdh-dev.oeaw.ac.at/fieldDefinition/life_event
```
SELECT ?value ?typeLabel ?timespanLabel  WHERE { 
?event crm:P11_had_participant $subject.
?event rdfs:label ?value.
  OPTIONAL {
?event crm:P4_has_time-span ?timespan.
  ?timespan rdfs:label ?timespanLabel.
  }
  OPTIONAL {
?event crm:P2_has_type ?type.
    ?type rdfs:label ?typeLabel.
  }
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
 


### Person Texts Box
#### Authored Texts
 – No field URI yet –

Selects text and legal document labels as well as labels of bibliographically relevant time spans (creation, publication, performance).

```

SELECT ?value ?timespanCreation ?timespanPublication ?timespanPerformance WHERE { 
  {?textCreation crm:P14_carried_out_by ?person.}
  UNION
  {?textCreation crm:P14_carried_out_by ?sameperson.
  ?sameperson owl:sameAs ?person.}
  
  {
    ?textCreation crm:P94_has_created ?text .
  }
  UNION
  {
    ?textCreation frbroo:R17_created ?text .
  }
  ?text rdfs:label ?value .
  OPTIONAL {
  ?textCreation crm:P4_has_time-span ?time .
    ?time rdfs:label ?timespanCreation .
  }
  OPTIONAL {
    ?text crm:P165i_is_incorporated_in ?publtext .
    ?publ frbroo:R24_created ?publtext .
    ?publ crm:P4_has_time-span ?time .
    ?time rdfs:label ?timespanPublication .
  }
  
  OPTIONAL {
    ?text frbroo:R66i_had_a_performed_version_through ?performance .
  ?performance crm:P4_has_time-span ?time .
    ?time rdfs:label ?timespanPerformance .
  }
 } 
```

### Person Mentions Box
#### Person Mentions (passage, passage label, text label)

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

