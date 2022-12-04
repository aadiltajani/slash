import sys
sys.path.append('../')
from flask import Flask, render_template, request
from google_scrapper import searchGoogle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_products', methods=['POST'])
def get_products():
    input = request.form.values()
    val = list(input)[0]
    print('Searching for', val)

    products1 = searchGoogle(val)

    return render_template('index.html', res1=products1['inline_shopping_results'], res2 = products1['shopping_results'])


if __name__ == "__main__":
    app.run(debug=True)
