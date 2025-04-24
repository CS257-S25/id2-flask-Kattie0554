'''file: test_id2.py'''
import unittest
from app import *

class TestApp(unittest.TestCase):
    def test_route_home(self):
        '''tests that the home route returns the correct thing'''
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
        '''tests that the route to get top by age returns the right thing, given age 23'''
        self.app = app.test_client()
        response = self.app.get('/get-top/23', follow_redirects=True)
        self.assertEqual(b"the top activity for people age 23 is T020901", response.data)

    def test_get_all_categories(self):
        '''tests that the route to get all categories returns the correct thing'''
        self.app = app.test_client()
        response = self.app.get('/get-all-categories', follow_redirects=True)
        self.assertEqual(b"the categoy options are: "
            b"['Personal Care Activities', 'Household Activities', " \
            b"'Caring For & Helping Household (HH) Members', " \
            b"'Caring For & Helping Nonhousehold (NonHH) Members', " \
            b"'Work & Work-Related Activities', 'Education', " \
            b"'Consumer Purchases', 'Professional & Personal Care Services', " \
            b"'Household Services', 'Government Services & Civic Obligations', " \
            b"'Eating and Drinking', " \
            b"'Socializing, Relaxing, and Leisure', 'Sports, Exercise, & Recreation', " \
            b"'Religious and Spiritual Activities', " \
            b"'Volunteer Activities', 'Telephone Calls', 'Traveling']", response.data)

    def test_get_subcategories_for_category(self):
        '''tets that the route to get subcatefories given a category returns the right thing '''
        self.app = app.test_client()
        response = self.app.get('/get-subcategories/Personal Care Activities', follow_redirects=True)
        self.assertEqual(b"these are the subcategories: "
        b"['Sleeping', 'Grooming', 'Health-related self care', 'Personal Activities', 'Personal Care Emergencies'] "
        b"for Personal Care Activities", response.data)

    def test_get_activities_from_sub(self):
        '''tests that the route to get activities returns the correct thing '''
        self.app = app.test_client()
        response = self.app.get('/get-activities/Personal Care Activities/Sleeping', follow_redirects=True)
        self.assertEqual(b"here are the activities for Sleeping in Personal Care Activities: ['Sleeping', 'Sleeplessness']", response.data)
    #need to make tests for cases where they forget to add a thing like /category also if they spell something wrong
    
    