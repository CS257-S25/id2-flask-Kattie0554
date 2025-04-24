'''file: test_id2.py'''
import unittest
from app import *

class TestApp(unittest.TestCase):
    def test_route_home(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"This is the homepage:"\
            b"1) TO GET the top activity for a certain age, go to /get-top/'<'age'>'"\
            b".... Note: for dummy data age options are: 23, 57, 80, 71, 40, 56, 18 "\
            b"2) TO GET a list of all category options, go to /get-all-categories "\
            b"....  NOTE: for now you can only shoose these categories: "\
            b"Personal Care Activities or Household Activities"\
            b"3) TO GET a list of subcategory options from a category,"\
            b" go to /get-subcategories/'<'category'>'"\
            b"....  NOTE: for now lowkey just use Personal Care Activities as Category "\
            b"becuase the test data is incomplete"\
            b"4) TO GET a list of activities from a subcategory, "\
            b"go to /get-activities/'<'category'>'/'<'subcategory'>'"\
            b"....  NOTE: basically choose Personal Care Activities and Sleeping "\
            b"because of incomplete test data", response.data )
    def test_route_top_by_age(self):
        self.app = app.test_client()
        response = self.app.get('/get-top/23', follow_redirects=True)
        self.assertEqual(b"the top activity for people age 23 is T020901", response.data)

    def test_get_all_categories(self):
        self.app = app.test_client()
        response = self.app.get('/get-all-categories', follow_redirects=True)
        self.asserEqual(b"the categoy options are: ['Personal Care Activities', 'Household Activities', " \
            b"'Caring For & Helping Household (HH) Members', 'Caring For & Helping Nonhousehold (NonHH) Members', " \
            b"'Work & Work-Related Activities', 'Education', 'Consumer Purchases', 'Professional & Personal Care Services', " \
            b"'Household Services', 'Government Services & Civic Obligations', 'Eating and Drinking', " \
            b"'Socializing, Relaxing, and Leisure', 'Sports, Exercise, & Recreation', 'Religious and Spiritual Activities', " \
            b"'Volunteer Activities', 'Telephone Calls', 'Traveling']", response.data)