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

GRAPHS = {
    "legal_kraus": g_lk, 
    "fackel": g_fa,
    "dritte_walpurgisnacht": g_dw
}


def assign_to_graph(*objects, graph=False, subject=False):
    for obj in objects:
        GRAPHS[graph].add((subject, OWL["sameAs"], obj))
    return print(f"added {len(objects)} triples to {graph}")


for y in same_as.values():
    identifier1 = URIRef(y[0]["identifier"])
    identifier2 = URIRef(y[1]["identifier"])
    identifier3 = False
    graph1 = y[0]["graph"].replace("https://sk.acdh.oeaw.ac.at/project/", "").replace("-", "_")
    graph2 = y[1]["graph"].replace("https://sk.acdh.oeaw.ac.at/project/", "").replace("-", "_")
    graph3 = False
    try:
        graph3 = y[2]["graph"].replace("https://sk.acdh.oeaw.ac.at/project/", "").replace("-", "_")
    except IndexError:
        print("error 1: no third graph")
    try:
        identifier3 = URIRef(y[2]["identifier"])
    except IndexError:
        print("error 2: no third identifier")
    if graph3:
        assign_to_graph(identifier2, identifier3, graph=graph1, subject=identifier1)
        assign_to_graph(identifier1, identifier3, graph=graph2, subject=identifier2)
        assign_to_graph(identifier1, identifier2, graph=graph3, subject=identifier3)
    else:
        assign_to_graph(identifier2, graph=graph1, subject=identifier1)
        assign_to_graph(identifier1, graph=graph2, subject=identifier2)

g_all = ConjunctiveGraph(store=project_store)
g_all.serialize("same_as.trig", format="trig")
