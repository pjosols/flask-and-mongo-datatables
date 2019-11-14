# Flask and mongo-datatables
A sample website that shows how to use mongo-datatables with Flask.

----


## Get started

You can install with pip:

      git clone git@github.com:pauljolsen/flask-and-mongo-datatables.git flask-demo
      cd flask-demo
      virtualenv -p python3 ~/.venvs/flask-demo
      source ~/.venvs/flask-demo/bin/activate
      pip install -r requirements.txt 
      flask run -p 5005


## DataTables static files

These are the packages I linked to from DataTables. Note that I have excluded the Editor from
this demo because you have to pay to use Editor.  If you go that route, you'll have to download
DataTables static files and plug them into your Flask app.

![datatables static files](datatables_packages.png)


## mongo-datatables

Find mongo-datatables at <https://github.com/pauljolsen/mongo-datatables>.

[![Downloads](http://pepy.tech/badge/mongo-datatables)](http://pepy.tech/project/mongo-datatables)