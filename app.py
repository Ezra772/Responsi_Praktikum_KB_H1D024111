import sys, os

# Tambahkan direktori femboy_social_system ke sys.path
_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'femboy_social_system')
sys.path.insert(0, _base)

from flask import Flask, render_template, request
from fuzzy_engine import analyze_fuzzy
from expert_engine import analyze_expert, get_questions, get_categories

app = Flask(
    __name__,
    template_folder=os.path.join(_base, 'templates'),
    static_folder=os.path.join(_base, 'static'),
    static_url_path='/static'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fuzzy', methods=['GET', 'POST'])
def fuzzy():
    if request.method == 'POST':
        data = {
            'eksposur_media':  float(request.form.get('eksposur_media', 5)),
            'latar_budaya':    float(request.form.get('latar_budaya', 5)),
            'lingkungan_sosial': float(request.form.get('lingkungan_sosial', 5)),
            'tingkat_empati':  float(request.form.get('tingkat_empati', 5))
        }
        result = analyze_fuzzy(data)
        return render_template('fuzzy_result.html', result=result, data=data)
    return render_template('fuzzy.html')

@app.route('/expert', methods=['GET', 'POST'])
def expert():
    questions  = get_questions()
    categories = get_categories()
    if request.method == 'POST':
        answers = {}
        for q_id in questions.keys():
            answers[q_id] = request.form.get(q_id) == 'ya'
        result = analyze_expert(answers)
        return render_template('expert_result.html', result=result, answers=answers)

    questions_list = [{"id": k, "text": v} for k, v in questions.items()]
    return render_template('expert.html', questions=questions_list, categories=categories)

if __name__ == '__main__':
    app.run(debug=False, port=5001)
