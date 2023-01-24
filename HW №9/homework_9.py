from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    """Страница вывода списка"""
    return render_template("list.html", candidates=utils.load_candidates_from_json("candidates.json"))


@app.route("/candidate/<int:x>/")
def page_candidates(x):
    """Страница вывода кандидата по id"""
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("card.html", candidate=candidates[x])


@app.route("/search/<candidate_name>/")
def page_candidates_name(candidate_name):
    """Страница вывода кандидата по name"""
    candidate_names = utils.get_candidate_by_name(candidate_name)
    return render_template("search.html", candidates=candidate_names, length=len(candidate_names))


@app.route("/skill/<candidate_skill>/")
def page_candidates_skill(candidate_skill):
    """Страница вывода кандидата по skill-ам"""
    candidate_skills = utils.get_candidate_by_skill(candidate_skill)
    return render_template("skill.html", candidates=candidate_skills, length=len(candidate_skills), candidate_skill=candidate_skill)


@app.route("/cat-bio/")
def page_cat_bio():
    """Страница с базовой версткой"""
    return render_template('index.html')


app.run()
