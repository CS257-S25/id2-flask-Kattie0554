'''Replace me with your flask app'''
from flask import Flask
import csv
from ProductionCode.loadData import load_data
from ProductionCode.get_top_by_age import *
from ProductionCode.getActivityByCategory import load_activity_data, load_category_data, load_subcategory_data

app = Flask(__name__)
@app.route('/')
def homepage():
     return "This is the homepage"

def load_data():
    data_for_get_top = load_data() 
    data_for_get_category = load_category_data()
    data_for_get_subcategory = load_subcategory_data()
    data_for_get_activity = load_activity_data()

@app.route('/get-top/<age>')
def get_top_by_age(age):
    return "the top activity for people age" + str(age) + " is " + str(get_most_common_top_activity(age, 1))

@app.errorhandler(404)
def page_not_found(e):
    return "sorry, wrong format, do this instead: /get-top/<age>"

@app.errorhandler(500)
def python_bug(e):
    return "a bug!"

if __name__ == '__main__':
    app.run()