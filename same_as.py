import json
from rdflib import Graph, Namespace, URIRef, plugin, ConjunctiveGraph, OWL
from rdflib.store import Store
from acdh_cidoc_pyutils.namespaces import CIDOC, FRBROO

with open("query_dump.json", "r") as f:
    ret = json.load(f)

unique = {}
for r in ret["results"]["bindings"]:
    try:
        if r["value"]["value"] in unique.keys():
            unique[r["value"]["value"]].append(
                {
                    "identifier": r["eThisGraph"]["value"],
                    "graph": r["thisGraph"]["value"]
                }
            )
        else:
            unique[r["value"]["value"]] = [
                {
                    "identifier": r["eThisGraph"]["value"],
                    "graph": r["thisGraph"]["value"]
                }
            ]
    except KeyError:
        unique[r["value"]["value"]] = [
                {
                    "identifier": r["eThisGraph"]["value"],
                    "graph": r["thisGraph"]["value"]
                }
            ]

with open("same_as_unique.json", "w") as f:
    json.dump(unique, f, indent=2)

same_as = {}
for u in unique.keys():
    if len(unique[u]) > 1:
        same_as[u] = unique[u]

with open("same_as.json", "w") as f:
    json.dump(same_as, f, indent=2)


LK = Namespace("https://sk.acdh.oeaw.ac.at/project/legal-kraus")
FA = Namespace("https://sk.acdh.oeaw.ac.at/project/fackel")
DW = Namespace("https://sk.acdh.oeaw.ac.at/project/dritte-walpurgisnacht")
domain = "https://sk.acdh.oeaw.ac.at/"
SK = Namespace(domain)

store = plugin.get("Memory", Store)()
project_store = plugin.get("Memory", Store)()
project_uri = URIRef(f"{SK}project/legal-kraus")
g_lk = Graph(identifier=project_uri, store=project_store)
g_lk.bind("cidoc", CIDOC)
g_lk.bind("frbroo", FRBROO)
g_lk.bind("sk", SK)
g_lk.bind("lk", LK)
g_lk.bind("owl", OWL)

project_uri = URIRef(f"{SK}project/fackel")
g_fa = Graph(identifier=project_uri, store=project_store)
g_fa.bind("cidoc", CIDOC)
g_fa.bind("frbroo", FRBROO)
g_fa.bind("sk", SK)
g_fa.bind("fa", FA)
g_fa.bind("owl", OWL)

project_uri = URIRef(f"{SK}project/dritte-walpurgisnacht")
g_dw = Graph(identifier=project_uri, store=project_store)
g_dw.bind("cidoc", CIDOC)
g_dw.bind("frbroo", FRBROO)
g_dw.bind("sk", SK)
g_dw.bind("dw", DW)
g_dw.bind("owl", OWL)

for y in same_as.values():
    identifier1 = URIRef(y[0]["identifier"])
    identifier2 = URIRef(y[1]["identifier"])
    graph1 = y[0]["graph"]
    graph2 = y[1]["graph"]
    named_graph_lk = "https://sk.acdh.oeaw.ac.at/project/legal-kraus"
    named_graph_fa = "https://sk.acdh.oeaw.ac.at/project/fackel"
    named_graph_dw = "https://sk.acdh.oeaw.ac.at/project/dritte-walpurgisnacht"
    try:
        graph3 = y[2]["graph"]
    except IndexError:
        continue
    try:
        identifier3 = URIRef(y[2]["identifier"])
    except IndexError:
        continue
    if graph1 == named_graph_lk:
        g_lk.add((identifier1, OWL["sameAs"], identifier2))
        if graph2 == named_graph_fa:
            g_fa.add((identifier2, OWL["sameAs"], identifier1))
        elif graph2 == named_graph_dw:
            g_dw.add((identifier2, OWL["sameAs"], identifier1))
        try:
            g_lk.add((identifier1, OWL["sameAs"], identifier3))
            if graph3 == named_graph_fa:
                g_fa.add((identifier3, OWL["sameAs"], identifier1))
            elif graph3 == named_graph_dw:
                g_dw.add((identifier3, OWL["sameAs"], identifier1))
        except IndexError:
            continue
    elif graph1 == named_graph_fa:
        g_fa.add((identifier1, OWL["sameAs"], identifier2))
        if graph2 == named_graph_lk:
            g_lk.add((identifier2, OWL["sameAs"], identifier1))
        elif graph2 == named_graph_dw:
            g_dw.add((identifier2, OWL["sameAs"], identifier1))
        try:
            g_fa.add((identifier1, OWL["sameAs"], identifier3))
            if graph3 == named_graph_lk:
                g_lk.add((identifier3, OWL["sameAs"], identifier1))
            elif graph3 == named_graph_dw:
                g_dw.add((identifier3, OWL["sameAs"], identifier1))
        except IndexError:
            continue
    elif graph1 == named_graph_dw:
        g_dw.add((identifier1, OWL["sameAs"], identifier2))
        if graph2 == named_graph_lk:
            g_lk.add((identifier2, OWL["sameAs"], identifier1))
        elif graph2 == named_graph_fa:
            g_fa.add((identifier2, OWL["sameAs"], identifier1))
        try:
            g_dw.add((identifier1, OWL["sameAs"], identifier3))
            if graph3 == named_graph_lk:
                g_lk.add((identifier3, OWL["sameAs"], identifier1))
            elif graph3 == named_graph_fa:
                g_fa.add((identifier3, OWL["sameAs"], identifier1))
        except IndexError:
            continue

g_all = ConjunctiveGraph(store=project_store)
g_all.serialize("same_as.trig", format="trig")