# SPARQL for the Search Field on Page 1: Values the search should be applied to and what to do with them

Inverse relations are not included here, also: should not be necessary as soon as data contains all inverse triples.

Paths to result values are Proto-SPARQL (meaning: need some translation to SPARQL, but should be understandable).

## crm:E35_Title rdf:value [value]
A text title. 
### Desired result line:
An F22 or E73 represented as `AUTHOR - TEXT TITLE - (Optional:) TEXT SUBTITLE - DATE`

### Proto-SPARQL:
```
[value] ^rdf:value/crm:P102i_is_title_of [F22 or E73] .    
[F22 or E73] (frbroo:R17i_was_created_by|crm:P94i_was_created_by)/crm:P14_carried_out_by [AUTHOR]
[TEXT TITLE] crm:P102i_is_title_of [F22 or E73] ;
crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/title/main>.
[TEXT SUBTITLE] crm:P102i_is_title_of [F22 or E73] ;
crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/title/sub>.
{[F22 or E73] (frbroo:R17i_was_created_by|crm:P94i_was_created_by)/crm:P4_has_time-span [DATE]}
UNION
{[F22 or E73] crm:P165i_is_incorporated_in*/frbroo:R24i_was_created_through/crm:P4_has_time-span [DATE]}
UNION
{[F22 or E73] frbroo:R66i_had_a_performed_version_through/crm:P4_has_time-span [DATE]}
```

## crm:E90_Symbolic_Object rdf:value [value]
A part of a text appellation (kind of title for F24 Publication Expressions). 
### Desired result line:
An F24 represented as `APPELLATION PART 1 - (Optional:) PART 2 - (Optional:) PART 3 ... `
### Proto-SPARQL:
```
[value] ^rdf:value/crm:P106i_forms_part_of/crm:P1i_identifies [F24] .    
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 1] .
[PART 1] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/title/main>.
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 2] .
[PART 2] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/title/sub>.
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 3] .
[PART 3] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/num/issue>.
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 4] .
[PART 4] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/num/volume>.
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 5] .
[PART 5] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/num/date>.
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 6] .
[PART 6] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/num/place>.
[Text] crm:P1_is_identified_by/crm:P106_is_composed_of [PART 7] .
[PART 7] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/appellation/num/ed>.
```

## crm:E33_E41_Linguistic_Appellation rdf:value [value]
A person name, a place name. 
### Desired result line 1:
An E21 Person represented as `PERSON NAME - BIRTH DATE - DEATH DATE`
### Proto-SPARQL:
```
[value] ^rdf:value/crm:P1i_identifies [E21_Person] .
[E21_Person] crm:P1_is_identified_by [PERSON NAME] ;
    a crm:E21_Person .
[PERSON NAME] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/person/persname/pref> .
[E21_PERSON] P98i_was_born/crm:P4_has_time-span [BIRTH DATE] ;
    P100i_died/crm:P4_has_time-span [DEATH DATE] .
```
### Desired result line 2:
A E53_Place represented as `Place Name`
### Proto-SPARQL:
```
[value] ^rdf:value/crm:P1i_identifies [E53_Place] .
[E53_Place] crm:P1_is_identified_by [PLACE NAME] ;
    a crm:E53_Place .
[PLACE NAME] crm:P2_has_type <https://sk.acdh.oeaw.ac.at/types/place/placename/pref>
```

## From here on: tbd.
## crm:E42_Identifier rdf:value [value]
An entity's identifier. Desired result line:

`Entity Label - Identifier value - Identifier Type`

## crm:E52_Time-Span [any data property] [value]
An event's time-span. 
### Desired result line 1:
`Author Name - Text Title - (Optional:) Text Subtitle - Date`
### Desired result line 2:
`Person Name - Birth Date - Death Date`
### Desired result line 3:
`Legal Case Label - Legal Case Date`

