"""
This script contains functions that convert general style bibtex into cogcomp styles
(See ccg.bib for more details)

"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
import copy

test_bib_file = "test.bib"
ccg_bib = "../ccg.bib"

ACRONYMS = {}

with open(ccg_bib) as fin:
    ccg_db = bibtexparser.load(fin)
    for key, val in ccg_db.strings.items():
        ACRONYMS[key.upper()] = val


def convert_entry_to_ccg_style(bib_str):
    """
    Load all entries (@article, @book, @inproceedings etc.) and convert them into ccg style

    Note:
    1.  This function only looks for entries, so the output won't include other items, such as @string, @comments

    2.  (TODO) In some cases, there might be two version of a publication with identical key (because they have
        the same author and year).

    :param bib_str: a string which contains one or more entry

    :return:    A list of triples, each triple corresponds to one entry from the input.

                Each triple has the form (old_key, new_key, new_bib) --

                old_key: the old entry key
                new_key: the new ccg-style entry key
                new_bib: converted ccg-style entry in string form
    """
    parser = BibTexParser()
    parser.ignore_nonstandard_types = False

    bib_db = bibtexparser.loads(bib_str, parser)

    result_list = []
    for entry in bib_db.entries:
        old_key = entry["ID"]
        new_key, new_entry  = _entry_to_ccg_style(entry)
        new_entry_str = _entry_to_str(new_entry)
        result_list.append((old_key, new_key, new_entry_str))

    return result_list


def _entry_to_ccg_style(entry):
    """
    Convert a dictionary entry
    :param entry:
    :return:    a tuple (new_key, new_entry)

                new_key: new ccg-style key
                new_entry: new entry instance
    """

    new_entry = copy.deepcopy(entry)

    # STEP 1: Replace old key with ccg style key
    author_list = _parse_author_string(entry["author"])

    if len(author_list) > 3:
        new_key = "".join([name[-1][0] for name in author_list])
    else:
        new_key = author_list[0][-1] + "".join([name[-1][:2] for name in author_list[1:]])

    if "year" in entry:
        new_key += entry["year"][-2:]

    new_entry["ID"] = new_key

    # STEP 2: Unify the way we display author, for example, change "Roth, Dan" to "Dan Roth"
    _author =  " and ".join([first_name + " " + last_name for first_name, last_name in author_list])

    new_entry["author"] = _author

    # STEP 3: Add double bracket to title, so that latex will know that we should keep capitalization there
    if "title" in entry:
        new_entry["title"] = "{" + new_entry["title"] + "}"

    # STEP 4: Expand acronyms in booktitle or journal (e.g. ACM to Association for Computing Machinery)
    if "booktitle" in entry:
        if entry["booktitle"] in ACRONYMS:
            new_entry["booktitle"] = ACRONYMS[new_entry["booktitle"]]

    if "journal" in entry:
        if entry["journal"] in ACRONYMS:
            new_entry["journal"] = ACRONYMS[new_entry["journal"]]


    return new_key, _fix_capitalization(new_entry)


def _fix_capitalization(entry):
    """
    The bibtexparser package automatically lower case all entry keys and value titles, we need to fix this
    """
    new_entry = {}
    for key, val in entry.items():
        if key.isupper():
            new_entry[key] = copy.deepcopy(val)
        else:
            new_entry[key.capitalize()] = copy.deepcopy(val)

    if new_entry["ENTRYTYPE"].lower() == "inproceedings":
        new_entry["ENTRYTYPE"] = "InProceedings"
    else:
        new_entry["ENTRYTYPE"] = new_entry["ENTRYTYPE"].capitalize()

    return new_entry


def _entry_to_str(entry):
    """
    Convert an entry (dictionary) to string form
    :param entry:
    :return:
    """

    dummy_db = BibDatabase()
    dummy_db.entries = [entry]

    return bibtexparser.dumps(dummy_db)


def _parse_author_string(author_string):
    """
    parse raw author string into (first name + middle name, last name) tuples
    :param author_string:
    :return: list of (first name + middle name, last name) tuples
    """

    authors = [a.strip() for a in author_string.split("and")]

    author_list = []

    for name in authors:
        # First fix cases like "Pan, Peter" to "Peter Pan"
        name_parts = [p.strip() for p in name.split(",")]
        if len(name_parts) > 1:
            name_parts.insert(0, name_parts.pop())
            name = " ".join(name_parts)

        name_parts = name.split(" ")
        last_name = name_parts.pop()
        first_name = " ".join(name_parts)

        author_list.append((first_name, last_name))

    return author_list


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert a bib file to CCG format, and output a mapping between old and new key for each converted item.")

    parser.add_argument("input_bib_file", type=str, help="path to input .bib file")
    parser.add_argument("output_bib_path", type=str, help="path for the output .bib file")
    parser.add_argument("output_mapping_path", type=str, help="path for the ouput key mapping")
    args = parser.parse_args()

    original_bib_file = args.input_bib_file
    new_bib_output_path = args.output_bib_path
    mapping_output_path = args.output_mapping_path

    results = convert_entry_to_ccg_style(open(original_bib_file).read())

    with open(new_bib_output_path, 'w', encoding='UTF-8') as new_bib_out, open(mapping_output_path, 'w', encoding='UTF-8') as mapping_out:
        for old_key, new_key, new_entry_str in results:
            new_bib_out.write(new_entry_str)
            new_bib_out.write('\n\n')

            mapping_out.write(old_key)
            mapping_out.write('\t')
            mapping_out.write(new_key)
            mapping_out.write('\n')