# bin/bash

echo "add namedgraph same_as.trig"
curl $R_ENDPOINT_V \
    -H 'Content-Type: application/x-trig; charset=UTF-8' \
    -H 'Accept: text/boolean' \
    -d @same_as.trig
