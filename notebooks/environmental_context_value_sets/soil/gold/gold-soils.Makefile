TASK_ROOT=notebooks/environmental_context_value_sets/soil/gold/

UP_FOUR=../../../..

gold-soils-by-semsql.tsv: $(UP_FOUR)/local/goldterms.db $(UP_FOUR)/local/envo.db
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

gold-soils-by-semsql-wide.tsv: gold-soils-by-semsql.tsv
	poetry run python gold_soils_by_semsql_wide.py \
		--input-file $< \
		--output-file $@
