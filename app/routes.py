import json

from flask import render_template, request
from mongo_datatables import DataTables

from app import app, mongo


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/table-view')
def table_view():
    return render_template('table_view.html')


@app.route('/mongo/<collection>')
def api_db(collection):
    request_args = json.loads(request.values.get("args"))
    results = DataTables(mongo, collection, request_args).get_rows()
    return json.dumps(results)
