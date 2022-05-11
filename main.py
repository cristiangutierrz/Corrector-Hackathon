from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    text_in = ''
    if request.method == 'POST':
        if request.form.to_dict()['submit_button'] == 'Corregir':
            text_in = request.form['input'] if len(request.form['input']) > 0 else ''
    text_out = text_in

    return render_template('index.html', input='' if text_in is None else text_in, output='' if text_out is None else text_out)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)