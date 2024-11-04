notebooks/gold-soils.tsv: local/goldterms.db local/envo.db
	poetry run sqlite3 -header -separator '	' $(word 1, $^) "\
	ATTACH DATABASE '$(word 2, $^)' AS envo; \
	select \
	s.subject sub , s.predicate pred , COALESCE(s.object, s.value) AS object_or_value \
	from \
	entailed_edge ee \
	join statements s on \
	ee.subject = s.subject \
	where \
	ee.predicate = 'rdfs:subClassOf' \
	and  \
	s.predicate not in ('rdf:type', 'rdfs:subClassOf', 'oio:hasExactSynonym', 'owl:equivalentClass' ) \
	and \
	ee.object = 'GOLDTERMS:4212'" > $@

#  http://35.173.42.85/repository goldterms-with-support
#PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
 #PREFIX : <http://purl.obolibrary.org/obo/gold.owl#>
 #PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
 #PREFIX owl: <http://www.w3.org/2002/07/owl#>
 #PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
 #PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
 #select  ?s ?p ?o ?olab
 ##?p (count(?s) as ?count)
 #where {
 #    ?s rdfs:subClassOf* <https://w3id.org/gold.path/4212> ;
 #                      ?p ?o .
 #    optional {
 #        ?o rdfs:label ?olab
 #    }
 #    minus {
 #        ?s rdfs:subClassOf ?o
 #    }
 #    minus {
 #        ?s rdf:type ?o
 #    }
 #    minus {
 #        ?s owl:equivalentClass ?o
 #    }
 #    minus {
 #        ?s oboInOwl:hasExactSynonym ?o
 #    }
 #    minus {
 #        ?s skos:closeMatch ?o
 #    }
 #    minus {
 #        ?s skos:exactMatch ?o
 #    }
 #}
 ##group by ?p