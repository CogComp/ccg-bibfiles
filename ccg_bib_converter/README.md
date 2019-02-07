# CCG-style BibTex converter

Converts any general format BibTex entries into CCG style
### Instructions
In `ccg_style_bib_converter.py`, the `convert_entry_to_ccg_style()` takes a raw string containing one or more entries (@inproceeding, @article), and output a triple for each entry, `(old_key, new_key, new_bib)`.

- `old_key`: The entry key for the input bib entry
- `new_key`: the output CCG style key for the bib entry
- `new_bib`: the output CCG style bib entry in string form

Note that:
- The function only deals with entries and ignores other items such as @string or @comments. In other words it doesn't convert the full .bib file.

### Server
`converter_server.py` contains a demo-server written in [Flask](http://flask.pocoo.org/docs/1.0/tutorial/). To run it you have to first install Flask
```sh
$ pip install Flask
```

Then run the server

```sh
$ export FLASK_APP=converter_server.py
$ flask run --host=127.0.0.1
 * Running on http://127.0.0.1:5000/
```