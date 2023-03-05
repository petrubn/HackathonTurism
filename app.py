from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/questions.html')
def questions():
    return render_template('questions.html')

@app.route('/templates/notfound.html')
def notfound():
    return render_template('notfound.html')

@app.route('/templates/maps.html')
def maps():
    return render_template('maps.html')    

if __name__ == "__main__":
    app.run(debug=True)