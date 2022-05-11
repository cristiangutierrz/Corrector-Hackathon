from flask import Flask, request, redirect, url_for, session,render_template
from flask_session import Session

app = Flask(__name__)

SECRET_KEY = "changeme"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/', methods=['GET', 'POST'])
def root():
    text_in = ''
    if request.method == 'POST':
        if request.form.to_dict()['submit_button'] == 'Corregir':
            text_in = request.form['input'] if len(request.form['input']) > 0 else ''
        session['log'] = text_in
        return redirect(url_for('root'))
    saved = session.pop('log', None)
    return render_template('index.html', input='' if saved is None else saved, output='' if saved is None else saved)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
