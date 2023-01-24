from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    str_candidates = "<pre>"
    candidates = utils.load_candidates()
    for candidate in candidates:
        str_candidates += f"{candidate['name']}\n" \
                          f"{candidate['position']}\n" \
                          f"{candidate['skills']}\n\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidate/<int:x>")
def page_candidates(x):
    str_candidate = ""
    candidates = utils.load_candidates()
    str_candidate += f"<img src={candidates[x]['picture']}>"
    str_candidate += f"<pre><br>{candidates[x]['name']}<br>" \
                     f"{candidates[x]['position']}<br>" \
                     f"{candidates[x]['skills']}<br></pre>"
    return str_candidate


@app.route("/skills/<int:x>")
def page_skills(x):
    str_candidate = ""
    candidates = utils.load_candidates()
    str_candidate += f"<img src={candidates[x]['picture']}>"
    str_candidate += f"<pre><br>{candidates[x]['name']}<br>" \
                     f"{candidates[x]['position']}<br>" \
                     f"{candidates[x]['skills']}<br></pre>"
    return str_candidate


app.run()
