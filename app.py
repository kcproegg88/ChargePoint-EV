from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', value = os.getenv('API_KEY'))

if __name__ == '__main__':
    app.run(debug=True)