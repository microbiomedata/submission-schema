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
