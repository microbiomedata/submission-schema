import pprint
import re

pipeds_strings_lines = """EMSL_store_temp|project_ID|replicate_number|sample_shipped|sample_type|technical_reps



dna_absorb1|dna_absorb2|dna_collect_site|dna_concentration|dna_cont_type|dna_cont_well|dna_container_ID|dna_dnase|dna_isolate_meth|dna_organisms|dna_project_contact|dna_samp_ID|dna_sample_format|dna_sample_name|dna_seq_project|dna_seq_project_PI|dna_seq_project_name|dna_volume|proposal_dna
dnase_rna|proposal_rna|rna_absorb1|rna_absorb2|rna_collect_site|rna_concentration|rna_cont_type|rna_cont_well|rna_container_ID|rna_isolate_meth|rna_organisms|rna_project_contact|rna_samp_ID|rna_sample_format|rna_sample_name|rna_seq_project|rna_seq_project_PI|rna_seq_project_name|rna_volume"""

pipeds_strings_list = pipeds_strings_lines.split('\n')


def fix_lines(line):
        pipeds_string_lower = line.lower()
        underscored = re.sub('[\\s\-\(\)]+', '_', pipeds_string_lower)
        pipeds_list = underscored.split('|')
        pipeds_set = set(pipeds_list)
        new_list = list(pipeds_set)
        new_list.sort()
        new_string = '|'.join(new_list)
        return new_string


final_list = []
for line in pipeds_strings_list:
    new_string = fix_lines(line)
    final_list.append(new_string)

pprint.pprint(final_list)

#
# final_string = '!'.join(final_list)
#
# pprint.pprint(final_string)
