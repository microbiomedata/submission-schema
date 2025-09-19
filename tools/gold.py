from collections import defaultdict
from enum import Enum
from typing import Dict, Iterable, Optional, Set

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue


class PathwayLevel(Enum):
    ecosystem = "Ecosystem"
    ecosystem_category = "EcosystemCategory"
    ecosystem_type = "EcosystemType"
    ecosystem_subtype = "EcosystemSubtype"
    specific_ecosystem = "SpecificEcosystem"


class GoldTermSet:
    def __init__(
        self,
        *,
        schema_enum_suffix: str = "",
        include: Optional[Dict[PathwayLevel, Iterable[str]]] = None,
    ):
        self.schema_enum_suffix: str = schema_enum_suffix
        self.terms: Dict[PathwayLevel, Set[str]] = defaultdict(set)
        self.include: Dict[PathwayLevel, Iterable[str]] = (
            include if include is not None else {}
        )


def inject_gold_pathway_terms(schema_view: SchemaView, gold_ecosystem_tree: dict):
    """Inject gold pathway terms into the schema."""
    levels = list(PathwayLevel)
    all_terms = GoldTermSet()
    soil_terms = GoldTermSet(
        schema_enum_suffix="ForSoil",
        include={
            PathwayLevel.ecosystem: ["Environmental"],
            PathwayLevel.ecosystem_category: ["Terrestrial"],
            PathwayLevel.ecosystem_type: ["Soil"],
        },
    )
    term_sets = [all_terms, soil_terms]

    def _add_term(term_set, term, level_index):
        level = levels[level_index]
        if term_set.include.get(level) and term["name"] not in term_set.include[level]:
            return
        term_set.terms[level].add(term["name"])
        for child in term.get("children", []):
            _add_term(term_set, child, level_index + 1)

    for term_set in term_sets:
        for ecosystem in gold_ecosystem_tree["children"]:
            _add_term(term_set, ecosystem, level_index=0)

    for term_set in term_sets:
        for level in levels:
            pvs = [
                PermissibleValue(text=term) for term in sorted(term_set.terms[level])
            ]
            schema_view.add_enum(
                EnumDefinition(
                    name=level.value + term_set.schema_enum_suffix + "Enum",
                    permissible_values=pvs,
                )
            )
