import pprint
import re

pipeds_strings_lines = """EMSL_store_temp|project_ID|replicate_number|sample_shipped|sample_type|technical_reps



dna_absorb1|dna_absorb2|dna_collect_site|dna_concentration|cont_type|cont_well|container_name|dnase|dna_isolate_meth|dna_organisms|jgi_samp_ID|jgi_sample_format|jgi_sample_name|jgi_seq_project|jgi_seq_project_name|jgi_sample_volume
dnase|rna_absorb1|rna_absorb2|rna_collect_site|rna_concentration|cont_type|cont_well|container_name|rna_isolate_meth|rna_organisms|jgi_samp_ID|jgi_sample_format|jgi_sample_name|jgi_seq_project|jgi_seq_project_name|jgi_sample_volume"""

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
