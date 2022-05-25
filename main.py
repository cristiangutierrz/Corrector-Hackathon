from flask import Flask, request, redirect, url_for, session,render_template
from flask_session import Session
from src import spellcheck_local as sp
import requests
import json
import google.oauth2.id_token
import google.auth.transport.requests
import os

app = Flask(__name__)
app.secret_key = "Some"
app.config['SESSION_COOKIE_NAME'] = "my_session"

@app.route('/', methods=['GET', 'POST'])
def root():
    text_in = ''

    if request.method == 'POST':
        if request.form.to_dict()['submit_button'] == 'Corregir':
            text_in = request.form['input'] if len(request.form['input']) > 0 else ''
            method = request.form['method'] if len(request.form['method']) > 0 else ''
            session['log'] = text_in
            session['method'] = method
        return redirect(url_for('root'))
    
    local = session.pop('log', None)
    method = session.pop('method', None)

    # Si tenemos input ejecutamos pyspellchecker
    if local is not None:
        if local and len(local)>0:
            print("Local: ", local)
            if method is not None:
                if method and len(method)>0:
                    if method == "Typewrite":
                        word_D = test_api(local)
                    elif method == "PySpellchecker":
                        word_D = pyspellchecker(local)
            print("Response: ", word_D)
        else:
            local = None
    print(method)
    return render_template('index.html', input='' if local is None else local, output='' if local is None else word_D, method=method)

def test_api(text_in):
    print("text_in: ", text_in)
    # TO-DO: Try-catch
    # Cuando se trabaja en local debera leer el fichero credentials .json
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './corrector-sm-9ef8799680bd.json'
    request = google.auth.transport.requests.Request()
    audience = 'https://europe-west3-corrector-sm.cloudfunctions.net/corregir'
    TOKEN = google.oauth2.id_token.fetch_id_token(request, audience)
    r = requests.post(
        'https://europe-west3-corrector-sm.cloudfunctions.net/corregir', 
        headers={'Authorization': f"Bearer {TOKEN}", "Content-Type": "application/json"},
        data=json.dumps({"message":text_in})  # possible request parameters
    )

    # HTTP 200 - OK
    if r.status_code == 200:
        json_response = json.loads(r.content.decode("utf-8"))

        # Este metodo te convierte todo en una lista
        # ['Hola', 'ke', ['que', 'qué'], 'tal']
        lista_palabras = generarFrase(json_response)

        # Esta funcion SE HA DE COMENTAR, la he hecho para que muestre
        # "Hola ke (que qué) tal"
        # lista_palabras = convert_to_sentence(lista_palabras)

        
        return lista_palabras

    return ""

def generarFrase(json_response):
    list_sentence = []
    for word in json_response['tokens']:
        list_sentence += [word['original_word']]
        if len(word['suggestions']) > 0:
            if word['original_word'] != word['suggestions'][0]['correction']:
                list_suggest = []
                if word['suggestions'][0]['score'] < 0.75:
                    for suggestion in word['suggestions'][:3]:
                        list_suggest += [suggestion['correction']]
                else:
                    list_suggest = [word['suggestions'][0]['correction']]
                list_sentence += [list_suggest]
    return list_sentence

def convert_to_sentence(list_sentence):
    text_out = ""
    for w in list_sentence:
        if isinstance(w, list):
            text_out += "(" + ' '.join(w) + ") "
        else:
                text_out += w + " "
    return text_out[:-1]

def pyspellchecker(local):
    return sp.spell(local)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)