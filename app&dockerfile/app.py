# Task: Build a simple application that gets data from open source API and visualize it by simple page.
import requests, os
from flask import Flask, render_template, request
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()


exchange_rates = requests.get(f"{os.getenv('ENDPOINT')}?app_id={os.getenv('APP_ID')}").json()["rates"]
currency_definition = requests.get(f"{ os.getenv('CURRENCY_DEF_ENDPOINT')}").json()


# define the  URL on application
@app.route('/', methods=['GET', 'POST'])
def home():
    currency = {}
    
    if request.method == 'POST':
        currency_name = request.form.get("currency")
        fcur = exchange_rates.get(currency_name)
        currency = { 'title': f'Actual exchange rate USD to {currency_name} ', 
                    'rates': f' 1 USD is {fcur:.3f} {currency_name}'
            }
    return render_template("home.jinja2", currency_definition=currency_definition, currency=currency) 


@app.route('/diagrama/', methods=['GET', 'POST'])
def diagrama():
    return render_template('diagrama.html')
    


# To start the server, and allow the flask receive connection.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# use this command in terminal to run that app on your localhost (you have to install python3):
# python3 app.py