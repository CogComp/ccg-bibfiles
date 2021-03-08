import sys
from collections import Counter
import ccg_bib_converter.ccg_style_bib_converter as ccg_style_bib_converter

"""Convert yuor bib file in to CCG format bib files.

python convert_bib_file.py ${YOUR_BIB_FILE} ${OUTPUT_BIB_FILE} ${OUPUT_MAP_TSV}

The output file will contain bib entries in CCG format, and the output map tsv
will contain "OLD_KEY \t NEW_KEY" to manually use to convert old keys in .tex
files to the new ones.

The output .bib file might contain duplicates that the user needs to fix by hand
The list of duplicate keys is printed on terminal
"""

# Input bib file by user in their own format
old_bib_file = sys.argv[1]
# Output bib file in CCG format
# (might contain duplicate entries which need to be fixed by hand; see below)
new_bib_file = sys.argv[2]
# Output file containing mapping from your keys to CCG keys
mapping_file = sys.argv[3]

with open(old_bib_file) as f:
    old_bib_text = f.read()

# List containing tuples of the kind (old_key, new_key, new_bib_item)
results = ccg_style_bib_converter.convert_entry_to_ccg_style(old_bib_text)

output_bib_fp = open(new_bib_file, 'w')
output_map_fp = open(mapping_file, 'w')

# Now there could be duplicate keys in results --
#  it could mean the exact same entry OR
#  same key but different entries

# First convert results to a unique entry list
unique_results = []
unique_new_items = set()

for (old_key, new_key, new_bib_item) in results:
    if new_bib_item not in unique_new_items:
        unique_results.append((old_key, new_key, new_bib_item))

new_key_count = Counter([x[1] for x in unique_results])
new_key_count = {k: v for (k, v) in new_key_count.items() if v > 1}

print("New bib keys with more than one entry; these need to be fixed manually")
print("\n".join(list(new_key_count.keys())))

"""
TODO(): Now if we have the same new key,
        add `a`, `b` to the key for different old keys.
"""

for (old_key, new_key, new_bib_item) in unique_results:
    output_map_fp.write("{}\t{}\n".format(old_key, new_key))
    output_bib_fp.write("{}".format(new_bib_item))

output_bib_fp.close()
output_map_fp.close()
