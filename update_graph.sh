# bin/bash

echo "delete namedgraphs"
curl -D- -X DELETE \
     "${R_ENDPOINT_V}?c=<https://sk.acdh.oeaw.ac.at/general>&c=<https://sk.acdh.oeaw.ac.at/model>&c=<https://sk.acdh.oeaw.ac.at/provenance>"
sleep 300

echo "add namedgraph sk_model.trig"
curl $R_ENDPOINT_V \
    -H 'Content-Type: application/x-trig; charset=UTF-8' \
    -H 'Accept: text/boolean' \
    -d @rdf/sk_model.trig
sleep 600

echo "add namedgraph general.trig"
curl $R_ENDPOINT_V \
    -H 'Content-Type: application/x-trig; charset=UTF-8' \
    -H 'Accept: text/boolean' \
    -d @rdf/general.trig
sleep 600

echo "add namedgraph provenance.trig"
curl $R_ENDPOINT_V \
    -H 'Content-Type: application/x-trig; charset=UTF-8' \
    -H 'Accept: text/boolean' \
    -d @rdf/provenance.trig