# CCG-style BibTex converter

This tool will help you format new BibTex citations into CCG style before adding them into cited.bib.

## What it does / doesn't
The tool is basically a simple function that takes one or more bib entries as input, and output them with correct CCG format (correct keys, author names, conference/journal names, etc.).
- It doesn't go to the .tex and fix the keys for you. It has to be done manually (or programmatically) by yourself.
- It's not a full .bib parser. It can parse the whole .bib file but it only outputs entries (@article, @proceedings, etc). It won't retain @string or @preamble after the conversion.

## Workflow
TL;DR -- Whenever you have one or more new BibTex citations, first run them through the converter (Currently hosted on http://macniece.seas.upenn.edu:4006/, email Sihao if it's down :) before adding them to `cited.bib`. You can also do the conversion programmatically.

### Workflow 1 (**Recommended**)
Whenever you want to include a new citation that doesn't exist in cited.bib, format it first before citing it in your .tex --
1. Grab its BibTex and run it through the interface, (or equivalently `convert_entry_to_ccg_style()` in `ccg_style_bib_converter.py`)
2. Add the converted BibTex to your fork of the `cited.bib`.
3. Repeat 1. and 2. for every new citation.
4. Merge `cited.bib` to master after finishing your paper.

### Workflow 2
In case you have a lot of citations to fix, this tool won't save you a lot of time, because it doesn't go to .tex and fix the keys for you. You can still do this programatically by --
1. Run the whole .bib file through `convert_entry_to_ccg_style()`
2. You will get the corrected entries and mappings from every old key to its new key.
3. Use the mapping, write a short script to fix keys in .tex .

## Programmatic Usage
In `ccg_style_bib_converter.py`, the `convert_entry_to_ccg_style()` takes a raw string containing one or more entries (e.g. @inproceeding{...}), and output list of triples, one for each entry, `(old_key, new_key, new_bib)`.

- `old_key`: The original key for the input bib entry
- `new_key`: the new CCG style key
- `new_bib`: the bib entry in CCG style


Note that:
- The function only deals with entries and ignores other items such as @string or @comments. In other words it doesn't convert the full .bib file.

## How to Run the Demo Server Locally
`converter_server.py` contains a demo-server written in [Flask](http://flask.pocoo.org/docs/1.0/tutorial/). To run it you have to first install Flask
```sh
$ pip install Flask
```

Then run the server

```sh
$ export FLASK_APP=converter_server.py
$ flask run --host=127.0.0.1 --port=5000
 * Running on http://127.0.0.1:5000/
```
## Problems/Feature Requesst
please email Sihao