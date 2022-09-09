from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/address/<vardas>")
def address(vardas):
    return render_template('address.html', vardas=vardas)

if __name__ == "__main__":
    app.run(debug=True)
