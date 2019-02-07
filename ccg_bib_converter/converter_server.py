from flask import Flask, request, render_template
from ccg_style_bib_converter import convert_entry_to_ccg_style

app = Flask(__name__)


@app.route("/")
def render_demo():
    return render_template("index.html")

@app.route("/convert", methods=['POST'])
def api_convert():
    lists = convert_entry_to_ccg_style(request.get_data())
    print(request.data)
    print(lists)
    res_data =  "\n\n".join([_str for _, _, _str in lists])
    return res_data