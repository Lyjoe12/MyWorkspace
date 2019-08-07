from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/rp_calc/')
def rp_calc():
    return render_template('rp_calc.html')


if __name__ == '__main__':
    app.run(debug=True)
