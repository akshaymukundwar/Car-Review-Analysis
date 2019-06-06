from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tablib
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['GET', 'POST'])
def search():
    df = pd.read_csv("car1.csv")
    if request.method == 'POST':
        _brand = request.form['brand']
        name = df.loc[df['BRAND'] == _brand]
        return name.to_html()
    return render_template('index.html')

@app.route('/enter', methods=['GET', 'POST'])
def model():
    df = pd.read_csv("car1.csv")
    if request.method == 'POST':
        _brand = request.form['brand1']
        _model = request.form['model']
        model = df.loc[(df['BRAND'] == _brand) & (df['MODEL'] == _model)]
        return model.to_html()
        #return render_template('df.html', data=[df.to_html()])
    return render_template('index.html')

dataset = tablib.Dataset()
with open( 'comments.csv',encoding="utf-8") as f:
    dataset.csv = f.read()

@app.route('/review.html')
def review():
    data = dataset.html
    return render_template('review1.html', data=data)

@app.route('/back',methods=['GET', 'POST'])
def back():
    if request.method == 'POST':
        return render_template('index.html')


@app.route('/comparision.html')
def comparision():
    return render_template('comparision.html')

@app.route('/back1',methods=['GET', 'POST'])
def back1():
    if request.method == 'POST':
        return render_template('comparision.html')


@app.route('/dropdown.html')
def dropdown():
    return render_template('dropdown.html')

@app.route('/performance')
def performance():
    df4 = pd.read_csv("performance.csv")
    height = df4['performance']
    bars = ('BMW', 'Audi', 'Acura', 'Mercedes', 'Honda')
    y_pos = np.arange(len(bars))
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.bar(y_pos, height, color='lightblue')
    plt.xticks(y_pos, bars)
    plt.title("Performance")
    plt.savefig("C:/Users/Akshay/edmunds/flaskapplication/static/performance.png")
    return render_template('performance.html')

@app.route('/styling')
def styling():
    df4 = pd.read_csv("performance.csv")
    height = df4['styling']
    bars = ('BMW', 'Audi', 'Acura', 'Mercedes', 'Honda')
    y_pos = np.arange(len(bars))
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.bar(y_pos, height, color='lightblue')
    plt.xticks(y_pos, bars)
    plt.title("Styling")
    plt.savefig("C:/Users/Akshay/edmunds/flaskapplication/static/styling.png")
    return render_template('styling.html')

@app.route('/comfort')
def comfort():
    df4 = pd.read_csv("performance.csv")
    height = df4['comfort']
    bars = ('BMW', 'Audi', 'Acura', 'Mercedes', 'Honda')
    y_pos = np.arange(len(bars))
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.bar(y_pos, height, color='lightblue')
    plt.xticks(y_pos, bars)
    plt.title("Comfort")
    plt.savefig("C:/Users/Akshay/edmunds/flaskapplication/static/comfort.png")
    return render_template('comfort.html')

@app.route('/safety')
def safety():
    df4 = pd.read_csv("performance.csv")
    height = df4['safety']
    bars = ('BMW', 'Audi', 'Acura', 'Mercedes', 'Honda')
    y_pos = np.arange(len(bars))
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.bar(y_pos, height, color='lightblue')
    plt.xticks(y_pos, bars)
    plt.title("Safety")
    plt.savefig("C:/Users/Akshay/edmunds/flaskapplication/static/safety.png")
    return render_template('safety.html')

@app.route('/aspiring.html')
def aspiring():
    values = [1.44, 1.85, 2.44, 2.12, 1.84]
    colors = ['b', 'g', 'r', 'c', 'm']
    labels = ['BMW', 'Audi', 'Acura', 'Mercedes', 'Honda']
    explode = (0, 0, 0.1, 0, 0)
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.pie(values, colors=colors, labels=labels, explode=explode, autopct='%1.1f%%', counterclock=False, shadow=True)
    plt.title('Population Density Index')
    plt.savefig("C:/Users/Akshay/edmunds/flaskapplication/static/aspiring.png")
    return render_template('aspiring.html')

@app.route('/topbrand.html')
def topbrands():
    top_15_brands_bar = pd.read_csv('topbrands.csv')
    label = top_15_brands_bar.iloc[:, 0]
    freq = top_15_brands_bar.iloc[:, 1]
    index = np.arange(len(label))
    plt.figure(figsize=(5, 5), facecolor=None)
    plt.bar(index, freq)
    plt.xlabel('Brands', fontsize=12)
    plt.ylabel('Frequencies', fontsize=12)
    plt.xticks(index, label, fontsize=7, rotation=45)

    plt.savefig("C:/Users/Akshay/edmunds/flaskapplication/static/topbrand.png")
    return render_template('topbrand.html')

if __name__ == '__main__':
    app.run(debug=True)