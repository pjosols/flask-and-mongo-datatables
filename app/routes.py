from flask import render_template, request, jsonify
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


@app.route('/mongo/<collection>', methods=['POST'])
def api_db(collection):
    data = request.get_json()
    results = DataTables(mongo, collection, data).get_rows()
    return jsonify(results)
