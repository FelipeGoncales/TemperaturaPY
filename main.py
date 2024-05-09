from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    temp = float(request.form['temperatura'])
    if (temp <= 37.2):
        mensagem = 'Temperatura Normal'
    elif (temp > 37.2) and (temp <= 38):
        mensagem = 'Estado febril'
    elif (temp > 38) and (temp <= 39):
        mensagem = 'Febre'
    else:
        mensagem = 'Febre Alta'
    return render_template('index.html', msg=mensagem)

if (__name__) == ('__main__'):
    app.run(debug=True)