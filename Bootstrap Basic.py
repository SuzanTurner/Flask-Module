from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/somewhere')
def go_somewhere():
    return "<h1> Hey, you've come somewhere"

if __name__ == "__main__":
    app.run(debug = True)