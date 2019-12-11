from flask import Flask, render_template, abort, request
from multi_rake import Rake

app = Flask(__name__)

PRODUCTS = {
    'iphone': {
        'name': 'iPhone 5S',
        'category': 'Phones',
        'price': 699,
    },
    'galaxy': {
        'name': 'Samsung Galaxy 5',
        'category': 'Phones',
        'price': 649,
    },
    'ipad-air': {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649,
    },
    'ipad-mini': {
        'name': 'iPad Mini',
        'category': 'Tablets',
        'price': 549
    }
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    keywords = []
    text = request.form['text_to_process']
    max_kw_length = int(request.form['max_kw_length'])

    if not text:
        abort(404)

    if request.method == 'POST':
        f = open("data/stopwords.txt", "r")
        sw = f.read()
        rake = Rake(language_code='id', max_words=max_kw_length, stopwords=set(sw.split("\n")))
        keywords = rake.apply(text)

    return render_template('process.html', keywords=keywords, text=text, max_kw_length=max_kw_length)
