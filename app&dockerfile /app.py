# Task: Build a simple application that gets data from open source API and visualize it by simple page.
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "042ee935522c4ac7851c410321a8cbff"

# Variables and data for connection with open source API.
APP_ID = "042ee935522c4ac7851c410321a8cbff"
ENDPOINT = "https://openexchangerates.org/api/latest.json"
CURRENCY_DEF_ENDPOINT = "https://openexchangerates.org/api/currencies.json"

# assign variables for get data from API
exchange_rates = requests.get(f"{ENDPOINT}?app_id={APP_ID}").json()["rates"]
currency_definition = requests.get(f"{CURRENCY_DEF_ENDPOINT}").json()


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


@app.route('/diagrama/')
def diagrama():
    return f"Hello everyone!"
    return render_template("diagrama.jinga2")
    

# To start the server, and allow the flask receive connection.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# use this command in terminal to run that app on your localhost (you have to install python3):
# python3 app.py