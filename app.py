'''Replace me with your flask app'''
from flask import Flask
from ProductionCode.get_top_by_age import get_most_common_top_activity
from ProductionCode.getActivityByCategory import load_category_data
from ProductionCode.getActivityByCategory import get_list_of_categories
from ProductionCode.getActivityByCategory import get_list_of_subcategories
from ProductionCode.getActivityByCategory import get_activities_from_subcategory
app = Flask(__name__)

@app.route('/')
def homepage():
    '''Purpose: Homepage provides instructions for what URL to go to see the data you choose'''
    return "This is the homepage:"\
    "1) TO GET the top activity for a certain age, go to /get-top/'<'age'>'"\
    ".... Note: for dummy data age options are: 23, 57, 80, 71, 40, 56, 18 "\
    "2) TO GET a list of all category options, go to /get-all-categories "\
    "....  NOTE: for now you can only shoose these categories: "\
    "Personal Care Activities or Household Activities"\
    "3) TO GET a list of subcategory options from a category,"\
    " go to /get-subcategories/'<'category'>'"\
    "....  NOTE: for now lowkey just use Personal Care Activities as Category "\
    "becuase the test data is incomplete"\
    "4) TO GET a list of activities from a subcategory, "\
    "go to /get-activities/'<'category'>'/'<'subcategory'>'"\
    "....  NOTE: basically choose Personal Care Activities and Sleeping "\
    "because of incomplete test data"

@app.route('/get-top/<age>')
def get_top_by_age(age):
    '''param: age, the age you want to see the top category for
    returns a string that gives the information for the top activity for an age group'''
    top=get_most_common_top_activity(age, 1)[0]
    return "the top activity for people age " + str(age) + " is " + str(top)

@app.route('/get-all-categories')
def get_all_categories():
    '''returns a list of category options'''
    data_for_get_category = load_category_data()
    category_list =get_list_of_categories(data_for_get_category)
    return "the categoy options are: " + str(category_list)

@app.route('/get-subcategories/<category>')
def get_subcategories_for_category(category):
    ''' param: category, the category you want more info about(subcategories for)
    returns a list of subcategories for a given category'''
    sub_list = get_list_of_subcategories(category)
    return f"these are the subcategories: {sub_list} for {category}"

@app.route('/get-subcategories/')
def cat_missing_for_get_sub():
    '''returns an error message if you forget to add the category'''
    return "Error: please include a category /get-subcategories/add-your-category"

@app.route('/get-activities/<category>/<subcategory>')
def get_activities_from_sub(category, subcategory):
    ''' param: category, the category you want to look at 
    param: subcategory, the subcategory you want more info about (activities for)
    returns a list of activities from a subcategory'''
    activities = get_activities_from_subcategory(category, subcategory)
    return f"here are the activities for {subcategory} in {category}: {activities}"

@app.errorhandler(404)
def page_not_found(e):
    '''returns error message if the page wasn't found'''
    return f"{e} ... refer to homepage (/) for options "

@app.errorhandler(500)
def python_bug(e):
    ''' returns a message to let you know if there's an internal error/bug'''
    return f"{e} a bug!"

if __name__ == '__main__':
    app.run()
