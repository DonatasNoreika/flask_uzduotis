from flask import Flask, render_template
from calendar import isleap

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/address/<vardas>")
def address(vardas):
    return render_template('address.html', vardas=vardas)

@app.route("/keliamieji")
def keliamieji():
    masyvas = [metai for metai in range(1900, 2100) if isleap(metai)]
    return render_template('keliamieji.html', metai=masyvas)

if __name__ == "__main__":
    app.run(debug=True)
