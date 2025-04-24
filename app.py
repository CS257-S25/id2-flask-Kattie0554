'''Replace me with your flask app'''
from flask import Flask
import csv
from ProductionCode.loadData import load_data
from ProductionCode.get_top_by_age import *
from ProductionCode.getActivityByCategory import *
app = Flask(__name__)
@app.route('/')
def homepage():
    return "This is the homepage:" \
    "1) To get the top activity for a certain age, go to /get-top/'<'age'>'" \
    ".... Note: for dummy data age options are: 23, 57, 80, 71, 40, 56, 18 " \
    "2) to get a list of all category options, go to /get-all-categories "\
    "....  NOTE: for now you can only shoose these categories: Personal Care Activities or Household Activities"

def load_data():
    data_for_get_top = load_data() 
    data_for_get_category = load_category_data()
    data_for_get_subcategory = load_subcategory_data()
    data_for_get_activity = load_activity_data()

#route that uses paramater "age" 
@app.route('/get-top/<age>')
def get_top_by_age(age):
    return "the top activity for people age " + str(age) + " is " + str(get_most_common_top_activity(age, 1)[0])

# need app.route(/get-all-categories) will return personal care, household, etc
@app.route('/get-all-categories')
def get_all_categories():
    data_for_get_category = load_category_data()
    return "the categoy options are: " + str(get_list_of_categories(data_for_get_category))

# need app.route(/get-subcategories/<category>) will return the subcategories for that category
@app.route('/get-subcategories/<category>')
def get_subcategories_for_category(category):
    data_for_get_subcategories = load_subcategory_data()
    sub= get_category_from_data(data_for_get_subcategories)
    return "the subcategory options for your chosen category: " + str(get_list_of_subcategories(data_for_get_subcategories, category))

# need app.route(/get-activity/<category>/<subcategory>) will return the activities for that subcategory
@app.errorhandler(404)
def page_not_found(e):
    return "sorry, wrong format, do this instead: /get-top/<age>"

@app.errorhandler(500)
def python_bug(e):
    return "a bug!"

if __name__ == '__main__':
    app.run()