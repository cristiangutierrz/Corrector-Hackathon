from flask import Flask, request, redirect, url_for, session,render_template
from flask_session import Session
from src import spellcheck_local as sp

app = Flask(__name__)
app.secret_key = "Some"
app.config['SESSION_COOKIE_NAME'] = "my_session"

@app.route('/', methods=['GET', 'POST'])
def root():
    text_in = ''
    if request.method == 'POST':
        if request.form.to_dict()['submit_button'] == 'Corregir':
            text_in = request.form['input'] if len(request.form['input']) > 0 else ''
            session['log'] = text_in
        return redirect(url_for('root'))
    local = session.pop('log', None)
    # Si tenemos input ejecutamos pyspellchecker
    if local is not None:
        if local and len(local)>0:
            word_D = sp.spell(local)
    return render_template('index.html', input='' if local is None else local, output='' if local is None else local + "\n\n" + str(word_D))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)