from app import *
import unittest

class TestApp(unittest.TestCase):
    def test_route_home(self):
        self.app=app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"This is the homepage:" \
            b"1) TO GET the top activity for a certain age, go to /get-top/'<'age'>'" \
            b".... Note: for dummy data age options are: 23, 57, 80, 71, 40, 56, 18 " \
            b"2) TO GET a list of all category options, go to /get-all-categories "\
            b"....  NOTE: for now you can only shoose these categories: Personal Care Activities or Household Activities"\
            b" 3) TO GET a list of subcategory options from a category, go to /get-subcategories/'<'category'>'"\
            b"....  NOTE: for now lowkey just use Personal Care Activities as Category becuase the test data is incomplete"\
            b"4) TO GET a list of activities from a subcategory, go to /get-activities/'<'category'>'/'<'subcategory'>'"\
            b"....  NOTE: basically choose Personal Care Activities and Sleeping because of incomplete test data", response.data )
        
    