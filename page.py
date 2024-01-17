from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == 'POST':
        print(request.form)
    return render_template('diplom.html')

@app.route("/about")
def about():
    return "<h1>О сайте</h1>"

if __name__ == "__main__":
    app.run(debug=True)