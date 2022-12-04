# __author__      =
# "Aadil Tajani, Dhruvish Patel,
# Kaustubh Deshpande, Aastha Singh, Arpit Chaudhary"
# __copyright__      = "Open source libraries"

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
    val = request.form['product']
    print(val)
    email = request.form['email']
    print('Searching for', val, '  Email found:', email)

    products1 = searchGoogle(val)

    return render_template('index.html', res1=products1['inline_shopping_results'])


if __name__ == "__main__":
    app.run(debug=True)
